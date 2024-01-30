from itertools import product

from lib.iterator import iterator
from lib.test import Test, cases

from lab1.core.pair.exercise import Pair


positives = [
    1,
    2,
    10,
    907,
    1995,
    2004,
    9001,
]
integers = [0, *positives, *map(lambda n: -n, positives)]
strings = [
    "a",
    "b",
    "c",
    "fox",
    "chicken",
    "grain",
]


@Test
@cases(
    *product(integers, repeat=2),
    *product(strings, repeat=2),
)
def get_second_after_init(first, second):
    yield second
    pair = Pair(first, second)
    yield pair.get_second()


@Test
@cases(
    *product(integers, repeat=3),
    *product(strings, repeat=3),
)
def get_second_after_set_second(first, old_second, new_second):
    yield new_second
    pair = Pair(first, old_second)
    pair.set_second(new_second)
    yield pair.get_second()


@Test
@cases(
    *product(integers, repeat=2),
    *product(strings, repeat=2),
)
def reverse_iterator_after_init(first, second):
    yield iterator(second, first)
    pair = Pair(first, second)
    yield pair.reverse_iterator()


@Test
@cases(
    *product(integers, repeat=3),
    *product(strings, repeat=3),
)
def reverse_iterator_after_set_second(first, old_second, new_second):
    yield iterator(new_second, first)
    pair = Pair(first, old_second)
    pair.set_second(new_second)
    yield pair.reverse_iterator()
