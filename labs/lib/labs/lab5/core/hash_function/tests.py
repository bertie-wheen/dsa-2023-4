from typing import Annotated

from lib.numberify import to_int
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab5.core.hash_function.exercise import HashFunction, _prime


@Test
def example_1(
    thing: Item,
):
    thing_as_int = to_int(thing)
    hash_function = HashFunction(thing_as_int + 1)
    hash_function._a = 1
    hash_function._b = 0
    yield thing_as_int
    yield hash_function.hash(thing)


@Test
def example_2(
    thing: Item,
    offset: Annotated[int, GE(0), LT(_prime)],
):
    thing_as_int = to_int(thing)
    hash_function = HashFunction(thing_as_int + 1 + offset)
    hash_function._a = 1
    hash_function._b = offset
    yield thing_as_int + offset
    yield hash_function.hash(thing)


@Test
def example_3(
    thing: Item,
    offset: Annotated[int, GE(0), LT(_prime)],
    size: Annotated[int, GE(1)],
):
    thing_as_int = to_int(thing)
    hash_function = HashFunction(size)
    hash_function._a = 1
    hash_function._b = offset
    yield (thing_as_int + offset) % size
    yield hash_function.hash(thing)


@Test
def example_4(
    thing: Item,
):
    thing_as_int = to_int(thing)
    hash_function = HashFunction(thing_as_int + 1)
    hash_function._a = 1
    hash_function._b = _prime
    yield thing_as_int
    yield hash_function.hash(thing)
