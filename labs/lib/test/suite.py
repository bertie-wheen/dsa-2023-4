from collections.abc import Iterable, Iterator

from lib.test import Test


class TestSuite:
    _tests: dict[str, Test]

    def __init__(self, tests: Iterable[tuple[str, Test]]) -> None:
        self._tests = dict(tests)

    def __getitem__(self, test_name: str) -> Test:
        return self._tests[test_name]

    def __len__(self) -> int:
        return len(self._tests)

    def __iter__(self) -> Iterator[tuple[str, Test]]:
        return iter(self._tests.items())
