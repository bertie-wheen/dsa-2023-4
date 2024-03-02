# from math import log10
from collections.abc import Iterable, Iterator
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection
from time import perf_counter_ns
import traceback
from typing import Any, Optional

from lib.labs import Labs
from lib.magic import are_equal, to_typed_string
from lib.test import Test
from lib.test.case_generator import generate_test_case


class TestRunner:
    _min_time_ns: int
    _max_time_s: Optional[float]

    def __init__(self, min_time_ms: int, max_time_ms: Optional[int]):
        self._min_time_ns = min_time_ms * 1_000_000
        self._max_time_s = max_time_ms and max_time_ms / 1_000

    def run(self, test: Test) -> str:
        scale = 0
        simple = not test.parameters
        first = True
        start_time_ns = perf_counter_ns()
        while first or perf_counter_ns() - start_time_ns < self._min_time_ns:
            first = False
            result = self._run_case(test, scale)
            if result:
                return result
            if simple:
                break
            if scale == 0:
                scale = 1
            else:
                # scale += 10 ** int(log10(scale))
                scale += 1
        return ""

    def _run_case(self, test: Test, scale: int) -> Optional[str]:
        if self._max_time_s is None:
            return self._run_directly(test, scale)
        return self._run_indirectly(test, scale)

    def _run_directly(self, test: Test, scale: int) -> Optional[str]:
        case = generate_test_case(test, scale)
        if case is None:
            return None
        preamble = test.preamble(case)
        result = _run_test_case(test, case)
        return result.reason(preamble)

    def _run_indirectly(self, test: Test, scale: int) -> Optional[str]:
        recv_conn, send_conn = Pipe(False)
        process = Process(target=_indirect_test_runner, args=(send_conn, test.full_id, scale))
        process.start()
        process.join(self._max_time_s)
        preamble = recv_conn.recv()
        if preamble is None:
            return None
        timed_out = not recv_conn.poll()
        if timed_out:
            process.terminate()
            result = TimedOutTestFailure(test)
        else:
            result = recv_conn.recv()
        return result.reason(preamble)


def _indirect_test_runner(send_conn: Connection, test_full_id: str, case_scale: int) -> None:
    test = Labs.instance().test(test_full_id)
    case = generate_test_case(test, case_scale)
    if case is None:
        send_conn.send(None)
        return
    send_conn.send(test.preamble(case))
    send_conn.send(_run_test_case(test, case))


def _run_test_case(test: "Test", case: tuple) -> "TestResult":
    run = test(case)
    expect = None
    try:
        expect = next(run)
        if type(expect) is type and issubclass(expect, Exception):
            try:
                output = next(run)
            except expect:
                return TestSuccess()
        else:
            output = next(run)
        if isinstance(expect, Iterator) and isinstance(output, Iterator):
            expect_eq = list(expect)
            output_eq = list(output)
            expect = iter(expect_eq)
            output = iter(output_eq)
        else:
            expect_eq = expect
            output_eq = output
        if are_equal(expect_eq, output_eq):
            return TestSuccess()
        return UnexpectedOutputTestFailure(test, expect, output)
    # except NotImplementedError as error:
    except Exception as error:
        return UnexpectedExceptionTestFailure(test, expect, error)


class TestResult:
    pass


class TestSuccess(TestResult):
    _reason: str

    def reason(self, preamble: str) -> str:
        return ""


class TestFailure(TestResult):
    def __init__(self, reason: Iterable[str]) -> None:
        self._reason = "\n".join(reason)

    def reason(self, preamble: str) -> str:
        return "\n".join(
            [
                preamble,
                self._reason,
            ]
        )


class TimedOutTestFailure(TestFailure):
    def __init__(self, test: "Test") -> None:
        super().__init__(
            (
                *test.source_lines,
                "# Timed out (probably due to an infinite loop)",
            )
        )


# class UnimplementedTestFailure(TestFailure):
#     pass  # TODO


def _comment(multiline_string: str) -> str:
    return "\n".join(f"# {line}" for line in multiline_string.split("\n"))


class UnexpectedExceptionTestFailure(TestFailure):
    def __init__(self, test: "Test", expect: Any, error: Exception) -> None:
        error_traceback = error.__traceback__.tb_next
        tb = error_traceback
        error_offset = None
        dropping_prefix = True
        while tb is not None:
            filename = tb.tb_frame.f_code.co_filename
            if filename.endswith("tests.py") and error_offset is None:
                error_offset = tb.tb_lineno - test.source_code.first_line_number
            if dropping_prefix and not (filename.endswith("magic.py") or filename.endswith("tests.py")):
                error_traceback = tb
                dropping_prefix = False
            tb = tb.tb_next
        setup_lines = test.source_code.setup_lines
        expect_lines = test.source_code.expect_lines
        output_lines = test.source_code.output_lines
        setup_len = len(setup_lines)
        reason = []
        if error_offset is not None and error_offset < setup_len:
            reason.extend(setup_lines[: error_offset + 1])
        else:
            reason.extend(setup_lines)
            reason.extend(expect_lines)
            if error_offset is None or error_offset > setup_len:
                if type(expect) is not type or not issubclass(expect, Exception):
                    expect_str = _comment(to_typed_string(expect))
                    reason.append(expect_str)
                reason.extend(output_lines)
        reason.append(f"# Raised unexpected {to_typed_string(error)}:")
        error_traceback = traceback.format_list(traceback.extract_tb(error_traceback)[0:])
        error_traceback = [line for trace in error_traceback for line in trace[:-1].split("\n")]
        reason.extend("# " + trace for trace in error_traceback)
        super().__init__(reason)


class UnexpectedOutputTestFailure(TestFailure):
    def __init__(self, test: "Test", expect: Any, output: Any) -> None:
        super().__init__(
            (
                *test.source_code.setup_lines,
                *test.source_code.expect_lines,
                _comment(to_typed_string(expect)),
                *test.source_code.output_lines,
                _comment(to_typed_string(output)),
                "# Returned unexpected output",
            )
        )
