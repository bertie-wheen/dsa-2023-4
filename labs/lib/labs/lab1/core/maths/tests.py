from itertools import product

from lib.test import Test, cases

from lab1.core.maths.exercise import is_even


even_naturals = [
    2,
    10,
    2004,
]
even_integers = [0, *even_naturals, *map(lambda n: -n, even_naturals)]

odd_naturals = [
    1,
    907,
    1995,
    9001,
]
odd_integers = [*odd_naturals, *map(lambda n: -n, odd_naturals)]


@Test
@cases(*even_integers)
def even_number_is_even(number):
    yield True
    yield is_even(number)


@Test
@cases(*odd_integers)
def odd_number_is_not_even(number):
    yield False
    yield is_even(number)
