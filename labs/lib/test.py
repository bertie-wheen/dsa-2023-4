from inspect import getsourcelines, signature
import traceback
from types import FunctionType
from typing import Any, Optional

from lib.magic import are_equal, to_typed_string


class TestSource:
    def __init__(self, preamble: list[str], expect: str, setup: list[str], output: str) -> None:
        self.preamble = preamble
        self.expect = expect
        self.setup = setup
        self.output = output


class TestResult:
    def __init__(self, expect: Any, output: Any, raised: bool) -> None:
        self.expect = expect
        self.output = output
        self.raised = raised

    def is_success(self) -> bool:
        return not self.raised and are_equal(self.expect, self.output)

    def is_failure(self) -> bool:
        return not self.is_success()


class TestRun:
    def __init__(self, test: "Test", case: Optional[Any]) -> None:
        self.test = test
        self.case = case
        if self.case is None:
            preamble = []
        else:
            params = signature(self.test.func).parameters.keys()
            preamble = [f"{k} = {v!r}" for k, v in zip(params, case)]
        self.source = TestSource(preamble, self.test.expect, self.test.source, self.test.output)
        self.result = None

    def reset(self) -> None:
        self.result = None

    def run(self) -> bool:
        if self.case is None:
            run = self.test.func()
        else:
            run = self.test.func(*self.case)
        expect = next(run)
        try:
            output = next(run)
            raised = False
        except Exception as error:
            output = error
            raised = True
        self.result = TestResult(expect, output, raised)
        return self.result.is_failure()

    def __str__(self) -> str:
        preamble = ["", *self.source.preamble] if self.source.preamble else []
        expect = ["", self.source.expect, "# " + to_typed_string(self.result.expect)]
        setup = ["", *self.source.setup] if self.source.setup else []
        output = ["", self.source.output, "# " + to_typed_string(self.result.output)]
        if self.result.raised:
            traces = traceback.format_list(traceback.extract_tb(self.result.output.__traceback__)[1:])
            traces = [split for trace in traces for split in trace[:-1].split("\n")]
            output.extend(
                [
                    "# Raised by:",
                    *("# " + trace for trace in traces),
                ]
            )
        problem = [
            "",
            "# " + ("raised an incorrect exception" if self.result.raised else "returned incorrect output"),
        ]
        return "\n".join(
            [
                *preamble,
                *expect,
                *setup,
                *output,
                *problem,
            ]
        )


class Test:
    def __init__(self, func: FunctionType) -> None:
        self.func = func

        self.cases = []
        if hasattr(func, "cases"):
            for case in func.cases:
                if not isinstance(case, tuple):
                    case = (case,)
                self.cases.append(case)
        else:
            self.cases.append(None)

        self.source = getsourcelines(func)[0]
        first_yield = next(i for i, l in enumerate(self.source) if "    yield " in l)
        self.source = self.source[first_yield:]
        self.source[0] = self.source[0].replace("    yield ", "    expect = ", 1)
        self.source[-1] = self.source[-1].replace("    yield ", "    output = ", 1)
        self.source = [line[4:-1] for line in self.source]
        [self.expect, *self.source, self.output] = self.source

        self.runs = [TestRun(self, case) for case in self.cases]

    def run(self) -> Optional[TestRun]:
        for run in self.runs:
            if run.run():
                return run
        return None

    def reset(self):
        for run in self.runs:
            run.reset()

    def __len__(self) -> int:
        return len(self.runs)


def cases(*cases):
    def decorator(test):
        test.cases = cases
        return test

    return decorator


def each_index(list, and_len=False):
    for index in range(len(list) + (1 if and_len else 0)):
        yield list, index
