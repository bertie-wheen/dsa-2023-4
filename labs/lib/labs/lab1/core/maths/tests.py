from typing import Annotated

from lib.test import Test
from lib.test.annotations import Even, Odd

from lab1.core.maths.exercise import is_even


@Test
def even_number_is_even(even_number: Annotated[int, Even()]):
    yield True
    yield is_even(even_number)


@Test
def odd_number_is_not_even(odd_number: Annotated[int, Odd()]):
    yield False
    yield is_even(odd_number)
