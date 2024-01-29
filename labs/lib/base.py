from typing import Any, Generic, Self, TypeVarTuple

from lib.magic import are_equal, to_typed_string


TypeVars = TypeVarTuple("TypeVars")


class Base(Generic[*TypeVars]):
    def __str__(self) -> str:
        return to_typed_string(self)

    def __eq__(self, other: Any) -> bool:
        return are_equal(self, other)

    def is_equal_to(self, other: Self) -> bool:
        return self is other
