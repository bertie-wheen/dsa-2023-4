from collections.abc import Iterator
from copy import copy
import random
from string import printable
from types import GenericAlias
from typing import Annotated, Any, Optional, TypeVar, get_args, get_origin

from lib.test import Test
from lib.test.annotations import *


class TestCaseGenerator:
    _test: Test
    _scale: int
    _vars: dict[str, type]
    _case: list

    def __init__(self, test: Test, scale: int) -> None:
        self._test = test
        self._scale = scale

    def __call__(self) -> Optional[tuple]:
        self._vars = {}
        self._case = []
        for parameter_type in self._test.parameters.types:
            try:
                argument = self._generate_argument(parameter_type)
            except ValueError:
                return None
            self._case.append(argument)
        return tuple(self._case)

    def _generate_argument(self, parameter_type: Any) -> Any:
        argument_type = self._specify_type(parameter_type)
        return self._generate(argument_type)

    def _generate(self, generated_type: Any) -> Any:
        if get_origin(generated_type) is Annotated:
            annotated_type, *annotations = get_args(generated_type)
            return self._generate_annotated(annotated_type, *annotations)
        return self._generate_annotated(generated_type)

    def _generate_annotated(self, annotated_type: Any, *annotations: Any) -> Any:
        if annotated_type is bool:
            return self._generate_bool()
        if annotated_type is int:
            return self._generate_int(*annotations)
        if annotated_type is str:
            return self._generate_str(*annotations)
        if type(annotated_type) is GenericAlias:
            generic_type = get_origin(annotated_type)
            generic_args = get_args(annotated_type)
            return self._generate_generic(generic_type, generic_args, *annotations)
        raise TypeError

    def _generate_bool(self) -> bool:
        return random.randint(0, 1) == 0

    def _generate_int(self, *annotations: Any) -> int:
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
                    bound = self._specify_value(bound)
                    if lower is not None and lower > bound:
                        raise TypeError
                    if upper is not None and upper < bound:
                        raise TypeError
                    lower = upper = bound
                case GE(bound):
                    bound = self._specify_value(bound)
                    if lower is None or lower < bound:
                        lower = bound
                case GT(bound):
                    bound = self._specify_value(bound) + 1
                    if lower is None or lower < bound:
                        lower = bound
                case LE(bound):
                    bound = self._specify_value(bound)
                    if upper is None or upper > bound:
                        upper = bound
                case LT(bound):
                    bound = self._specify_value(bound) - 1
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
            return random.randrange(lower, upper + 1, 2)
        if odd:
            if lower % 2 == 0:
                if lower == upper:
                    raise TypeError
                lower += 1
            return random.randrange(lower, upper + 1, 2)
        return random.randint(lower, upper)

    def _generate_length(self, *annotations: Any) -> int:
        return self._generate_int(GE(0), *annotations)

    def _generate_str(self, *annotations: Any) -> str:
        length = self._generate_length(*annotations)
        return "".join(self._generate_char() for _ in range(length))

    def _generate_char(self) -> str:
        return random.choice(printable)

    def _generate_generic(self, generic_type: Any, generic_args: Any, *annotations: Any) -> Any:
        if generic_type is Iterator:
            item_type = generic_args[0]
            length = self._generate_length(*annotations)
            return iter(tuple(self._generate(item_type) for _ in range(length)))
        if generic_type is tuple:
            return tuple(map(self._generate, generic_args))
        if generic_type is list:
            return list(self._generate_generic(Iterator, generic_args, *annotations))
        if generic_type is set:
            for annotation in annotations:
                match annotation:
                    case GT(count):
                        count = self._specify_value(count)
                        if count >= 1:
                            raise NotImplementedError
                    case GE(count) | EQ(count):
                        count = self._specify_value(count)
                        if count > 1:
                            raise NotImplementedError
            return set(self._generate_generic(Iterator, generic_args, *annotations))
        if hasattr(generic_type, "build") and callable(generic_type.build):
            return generic_type.build(self._generate_generic(Iterator, generic_args, *annotations))
        raise TypeError

    def _specify_type(self, generic_type: Any) -> Any:
        if type(generic_type) is TypeVar:
            return self._specify_type_var(generic_type)
        origin = get_origin(generic_type)
        if origin is None:
            return generic_type
        args = get_args(generic_type)
        if origin is Annotated:
            annotated_type, *annotations = args
            return Annotated[self._specify_type(annotated_type), *annotations]
        return GenericAlias(origin, tuple(map(self._specify_type, args)))

    def _specify_type_var(self, type_var: TypeVar) -> type:
        name = type_var.__name__
        if name not in self._vars:
            self._vars[name] = random.choice((int, str, bool))
        return self._vars[name]

    def _specify_value(self, value: str | int) -> int:
        if type(value) is int:
            return value
        if value == "scale":
            return self._scale
        value = self._argument(value)
        if type(value) is int:
            return value
        if hasattr(value, "get_length") and callable(value.get_length):
            return value.get_length()
        if isinstance(value, Iterator):
            value = list(copy(value))
        return len(value)

    def _argument(self, argument_name: str) -> Any:
        try:
            index = next(index for index, name in enumerate(self._test.parameters.names) if name == argument_name)
        except StopIteration:
            assert False, f"test {self._test.full_id} has no argument called {argument_name}, but it was referenced in an annotation"
        return self._case[index]


def generate_test_case(test: Test, scale: int) -> Optional[tuple]:
    test_case_generator = TestCaseGenerator(test, scale)
    return test_case_generator()
