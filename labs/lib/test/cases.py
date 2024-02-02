from collections.abc import Iterator
from copy import copy
from inspect import Parameter
from math import log10
from random import choice, randint, randrange
from string import printable
from time import perf_counter_ns
from types import GenericAlias
from typing import Annotated, Any, TypeVar, get_args, get_origin

from lib.iterator import iterator
from lib.test.annotations import *


class CasesGenerator:
    _parameters: list[Parameter]
    _vars: dict[str, type]
    _case: list
    _min_time: int
    _scale: int
    _initial_scale: int

    def __init__(self, parameters: list[Parameter], min_time: int, initial_scale: int) -> None:
        if initial_scale < 0:
            raise ValueError
        self._parameters = parameters
        self._min_time = min_time
        self._initial_scale = initial_scale

    def get_type(self, parameter_type: type | TypeVar | GenericAlias) -> type | GenericAlias:
        if type(parameter_type) is TypeVar:
            name = parameter_type.__name__
            if name not in self._vars:
                self._vars[name] = choice((int, str, bool))
            return self._vars[name]
        origin = get_origin(parameter_type)
        if origin is None:
            return parameter_type
        args = get_args(parameter_type)
        if origin is Annotated:
            return Annotated[self.get_type(args[0]), *args[1:]]
        return GenericAlias(origin, tuple(map(self.get_type, args)))

    def __iter__(self) -> Iterator[tuple]:
        start = perf_counter_ns()
        self._scale = self._initial_scale
        while perf_counter_ns() - start < self._min_time:
            self._vars = {}
            self._case = []
            for parameter in self._parameters:
                parameter_type = parameter.annotation
                argument_type = self.get_type(parameter_type)
                try:
                    argument = self.gen_value(argument_type)
                    self._case.append(argument)
                except ValueError:
                    self._scale = 1
                    break
            if len(self._case) < len(self._parameters):
                continue
            yield self._case
            if self._scale == 0:
                self._scale = 1
            self._scale += 10 ** int(log10(self._scale))

    def gen_annotated_value(self, value_type: type | GenericAlias, *annotations: Any) -> Any:
        if value_type is bool:
            return randint(0, 1) == 0
        if value_type is int:
            even = False
            odd = False
            lower = None
            upper = None
            for annotation in annotations:
                match annotation:
                    case Even():
                        even = True
                        if odd:
                            raise TypeError
                    case Odd():
                        odd = True
                        if even:
                            raise TypeError
                    case EQ(bound):
                        bound = self.get_value(bound)
                        if lower is not None and lower > bound:
                            raise TypeError
                        if upper is not None and upper < bound:
                            raise TypeError
                        lower = upper = bound
                    case GE(bound):
                        bound = self.get_value(bound)
                        if lower is None or lower < bound:
                            lower = bound
                    case GT(bound):
                        bound = self.get_value(bound) + 1
                        if lower is None or lower < bound:
                            lower = bound
                    case LE(bound):
                        bound = self.get_value(bound)
                        if upper is None or upper > bound:
                            upper = bound
                    case LT(bound):
                        bound = self.get_value(bound) - 1
                        if upper is None or upper > bound:
                            upper = bound
            if lower is None and upper is None:
                lower = -self._scale
                upper = self._scale
                if odd and self._scale == 0:
                    lower += 1
                    upper += 1
            elif lower is None and upper is not None:
                lower = upper - self._scale
                if self._scale == 0 and (odd and upper % 2 == 0 or even and upper % 2 == 1):
                    lower -= 1
            elif lower is not None and upper is None:
                upper = lower + self._scale
                if self._scale == 0 and (odd and lower % 2 == 0 or even and lower % 2 == 1):
                    upper += 1
            elif lower > upper:
                raise TypeError
            if even:
                if lower % 2 == 1:
                    if lower == upper:
                        raise TypeError
                    lower += 1
                return randrange(lower, upper + 1, 2)
            if odd:
                if lower % 2 == 0:
                    if lower == upper:
                        raise TypeError
                    lower += 1
                return randrange(lower, upper + 1, 2)
            return randint(lower, upper)
        if value_type is str:
            length = self.gen_annotated_value(int, GE(0), *annotations)
            return "".join(choice(printable) for _ in range(length))
        if type(value_type) is GenericAlias:
            origin = get_origin(value_type)
            args = get_args(value_type)
            if origin is Iterator:
                item_type = args[0]
                length = self.gen_annotated_value(int, GE(0), *annotations)
                return iterator(*(self.gen_value(item_type) for _ in range(length)))
        raise TypeError

    def gen_value(self, value_type: type | GenericAlias) -> Any:
        if get_origin(value_type) is Annotated:
            value_type, *annotations = get_args(value_type)
            return self.gen_annotated_value(value_type, *annotations)
        return self.gen_annotated_value(value_type)

    def get_value(self, value: str | int) -> int:
        if type(value) is int:
            return value
        if value == "scale":
            return self._scale
        value = self._case[next(index for index, parameter in enumerate(self._parameters) if parameter.name == value)]
        if type(value) is int:
            return value
        if isinstance(value, Iterator):
            value = list(copy(value))
        return len(value)
