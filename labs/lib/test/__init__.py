from inspect import Parameter, getsourcelines, signature
import traceback
from types import FunctionType

from lib.magic import are_equal, to_repr, to_typed_string
from lib.test.cases import CasesGenerator


class Test:
    _line: int
    _setup_lines: list[str]
    _expect_line: str
    _output_line: str
    _initial_scale: int
    _parameter_names: list[str]
    _parameters: list[Parameter]

    def __init__(self, func: FunctionType) -> None:
        self._func = func

        self._initial_scale = self._func.initial_scale if hasattr(self._func, "initial_scale") else 0

        source, self._line = getsourcelines(func)
        offset = next(i for i, l in enumerate(source) if l.startswith("def "))
        offset += next(i for i, l in enumerate(source[offset:]) if l.endswith(":\n"))
        offset += 1
        self._line += offset
        source = source[offset:]
        source = [line[4:-1] for line in source]

        [*self._setup_lines, self._expect_line, self._output_line] = source

        self._expect_line = self._expect_line.replace("yield ", "expect = ", 1)
        self._output_line = self._output_line.replace("yield ", "output = ", 1)

        parameters = signature(func).parameters
        self._parameter_names = list(parameters.keys())
        self._parameters = list(parameters.values())

    def run(self, min_time: int = 25_000_000) -> str:
        for case in CasesGenerator(self._parameters, min_time, self._initial_scale):
            preamble = [f"{k} = {to_repr(v)}" for k, v in zip(self._parameter_names, case)]
            run = self._func(*case)
            success = False
            error = None
            expect = None
            output = None
            try:
                expect = next(run)
                if type(expect) is type and issubclass(expect, Exception):
                    try:
                        output = next(run)
                    except expect as e:
                        output = e
                        success = True
                else:
                    output = next(run)
                    success = are_equal(expect, output)
            except Exception as e:
                error = e
            if not success:
                setup_lines = self._setup_lines
                expect_line = self._expect_line
                output_line = self._output_line
                expect_str = "\n".join("# " + line for line in to_typed_string(expect).split("\n"))
                output_str = "\n".join("# " + line for line in to_typed_string(output).split("\n"))
                s = [""]
                s.extend(preamble)
                if error is not None:
                    error_traceback = error.__traceback__.tb_next
                    tb = error_traceback
                    error_offset = None
                    dropping_prefix = True
                    while tb is not None:
                        filename = tb.tb_frame.f_code.co_filename
                        if filename.endswith("tests.py") and error_offset is None:
                            error_offset = tb.tb_lineno - self._line
                        if dropping_prefix and not (filename.endswith("magic.py") or filename.endswith("tests.py")):
                            error_traceback = tb
                            dropping_prefix = False
                        tb = tb.tb_next
                    setup_len = len(setup_lines)
                    if error_offset is not None and error_offset < setup_len:
                        s.extend(setup_lines[: error_offset + 1])
                    else:
                        s.extend(setup_lines)
                        s.append(expect_line)
                        if error_offset is None or error_offset > setup_len:
                            if type(expect) is not type or not issubclass(expect, Exception):
                                s.append(expect_str)
                            s.append(output_line)
                    s.append(f"# Raised unexpected {to_typed_string(error)}:")
                    error_traceback = traceback.format_list(traceback.extract_tb(error_traceback)[0:])
                    error_traceback = [line for trace in error_traceback for line in trace[:-1].split("\n")]
                    s.extend("# " + trace for trace in error_traceback)
                else:
                    s.extend(setup_lines)
                    s.append(expect_line)
                    s.append(expect_str)
                    s.append(output_line)
                    s.append(output_str)
                    s.append(f"# Returned unexpected output")
                return "\n".join(s)
        return ""


def scale(initial_scale: int):
    def decorator(test):
        test.initial_scale = initial_scale
        return test

    return decorator
