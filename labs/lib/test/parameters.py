from collections.abc import Callable, Iterator
import inspect
from inspect import Parameter
from typing import Any


class TestParameters:
    _parameters: tuple[Parameter]

    def __init__(self, test_func: Callable) -> None:
        signature = inspect.signature(test_func)
        self._parameters = tuple(signature.parameters.values())

    def __len__(self) -> int:
        return len(self._parameters)

    def __iter__(self) -> Iterator[Parameter]:
        return iter(self._parameters)

    @property
    def names(self) -> tuple[str]:
        return tuple(parameter.name for parameter in self._parameters)

    @property
    def types(self) -> tuple[Any]:
        return tuple(parameter.annotation for parameter in self._parameters)
