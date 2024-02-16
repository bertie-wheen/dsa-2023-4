from collections.abc import Iterator
from typing import Annotated

from lib.array import Array
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab2.core.static_array_list import StaticArrayList
from lab4.core.binary_search.exercise import binary_search


@Test
def binary_search_when_contained(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    sorted_array = Array.build(iter(sorted(items)))
    item = sorted_array.get_at(index)
    index = binary_search(sorted_array, item)
    yield item
    yield sorted_array.get_at(index)


@Test
def binary_search_on_unique_items_when_contained(
    items: Annotated[set[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    sorted_array = Array.build(iter(sorted(items)))
    item = sorted_array.get_at(index)
    yield index
    yield binary_search(sorted_array, item)


@Test
def binary_search_when_not_contained(
    items: StaticArrayList[Item],
    item: Item,
):
    indices = StaticArrayList()
    for index in range(items.get_length()):
        if item == items.get_at(index):
            indices.insert_last(index)
    for index in indices.reverse_iterator():
        items.remove_at(index)
    sorted_array = Array.build(iter(sorted(items.iterator())))
    yield None
    yield binary_search(sorted_array, item)
