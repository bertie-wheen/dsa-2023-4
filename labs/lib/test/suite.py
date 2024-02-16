from collections.abc import Iterable, Iterator

import lib.test


class TestSuite:
    _tests: dict[str, "lib.test.Test"]

    def __init__(self, tests: Iterable[tuple[str, "lib.test.Test"]]) -> None:
        self._tests = dict(tests)

    def __getitem__(self, test_name: str) -> "lib.test.Test":
        return self._tests[test_name]

    def __len__(self) -> int:
        return len(self._tests)

    def __iter__(self) -> Iterator[tuple[str, "lib.test.Test"]]:
        return iter(self._tests.items())
