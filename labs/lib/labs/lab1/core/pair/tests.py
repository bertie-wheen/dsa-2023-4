from lib.iterator import iterator
from lib.test import Test
from lib.type_vars import Item

from lab1.core.pair.exercise import Pair


@Test
def get_second_after_init(first: Item, second: Item):
    pair = Pair(first, second)
    yield second
    yield pair.get_second()


@Test
def get_second_after_set_second(first: Item, old_second: Item, new_second: Item):
    pair = Pair(first, old_second)
    pair.set_second(new_second)
    yield new_second
    yield pair.get_second()


@Test
def reverse_iterator_after_init(first: Item, second: Item):
    pair = Pair(first, second)
    yield iterator(second, first)
    yield pair.reverse_iterator()


@Test
def reverse_iterator_after_set_second(first: Item, old_second: Item, new_second: Item):
    pair = Pair(first, old_second)
    pair.set_second(new_second)
    yield iterator(new_second, first)
    yield pair.reverse_iterator()
