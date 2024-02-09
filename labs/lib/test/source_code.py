from collections.abc import Callable, Iterator
import inspect


class TestSourceCode:
    _setup_lines: tuple[str]
    _expect_lines: str
    _output_lines: str
    _first_line_number: int

    def __init__(self, test_func: Callable) -> None:
        source, first_line = inspect.getsourcelines(test_func)

        offset = next(index for index, line in enumerate(source) if line.startswith("def "))
        offset += next(index for index, line in enumerate(source[offset:]) if line.endswith(":\n"))
        offset += 1
        source = source[offset:]
        first_line += offset

        source = [line[4:-1] for line in source]

        yields = (index for index, line in enumerate(source) if line.strip().startswith("yield "))
        expect_offset = next(yields)
        output_offset = next(yields)

        setup = source[:expect_offset]
        expect = source[expect_offset:output_offset]
        output = source[output_offset:]

        expect[0] = expect[0].replace("yield ", "expect = ", 1)
        output[0] = output[0].replace("yield ", "output = ", 1)

        self._setup_lines = tuple(setup)
        self._expect_lines = tuple(expect)
        self._output_lines = tuple(output)
        self._first_line_number = first_line

    @property
    def lines(self) -> tuple[str]:
        return (
            *self.setup_lines,
            *self.expect_lines,
            *self.output_lines,
        )

    @property
    def setup_lines(self) -> tuple[str]:
        return self._setup_lines

    @property
    def expect_lines(self) -> tuple[str]:
        return self._expect_lines

    @property
    def output_lines(self) -> tuple[str]:
        return self._output_lines

    @property
    def first_line_number(self) -> int:
        return self._first_line_number

    def __iter__(self) -> Iterator[str]:
        return iter(self.lines)

    def __len__(self) -> int:
        return len(self.lines)

    def __str__(self):
        return "\n".join(self.lines)
