from collections.abc import Iterator
from copy import copy
from itertools import chain
from typing import Annotated

from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab2.core.static_array_list.exercise import StaticArrayList


@Test
def get_at_then_remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = StaticArrayList.build(items)
    yield list.get_at(index)
    yield list.remove_at(index)


@Test
def insert_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
    item: Item,
):
    list = StaticArrayList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def insert_at_first_repeatedly_then_reverse_iterator(
    items: Iterator[Item],
):
    list = StaticArrayList()
    for item in copy(items):
        list.insert_at(0, item)
    yield items
    yield list.reverse_iterator()


@Test
def insert_at_then_get_length(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = StaticArrayList.build(items)
    length = list.get_length()
    list.insert_at(index, item)
    yield length + 1
    yield list.get_length()


@Test
def insert_at_then_get_at_earlier(
    earlier_items: Annotated[Iterator[Item], GE(1)],
    later_items: Iterator[Item],
    insert_index: Annotated[int, EQ("earlier_items")],
    early_index: Annotated[int, GE(0), LT("earlier_items")],
    item: Item,
):
    list = StaticArrayList.build(chain(earlier_items, later_items))
    early_item = list.get_at(early_index)
    list.insert_at(insert_index, item)
    yield early_item
    yield list.get_at(early_index)


@Test
def insert_at_then_get_at(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = StaticArrayList.build(items)
    list.insert_at(index, item)
    yield item
    yield list.get_at(index)


@Test
def insert_at_then_get_at_later(
    earlier_items: Iterator[Item],
    later_items: Annotated[Iterator[Item], GE(1)],
    insert_index: Annotated[int, EQ("earlier_items")],
    late_index: Annotated[int, GE(0), LT("later_items")],
    item: Item,
):
    list = StaticArrayList.build(chain(earlier_items, later_items))
    late_item = list.get_at(insert_index + late_index)
    list.insert_at(insert_index, item)
    yield late_item
    yield list.get_at(insert_index + 1 + late_index)


@Test
def insert_at_then_remove_at(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = StaticArrayList.build(items)
    list.insert_at(index, item)
    yield item
    yield list.remove_at(index)


@Test
def insert_at_last_repeatedly_then_iterator(
    items: Iterator[Item],
):
    list = StaticArrayList()
    for item in copy(items):
        list.insert_at(list.get_length(), item)
    yield items
    yield list.iterator()


@Test
def insert_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GT("items")],
    item: Item,
):
    list = StaticArrayList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def remove_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
):
    list = StaticArrayList.build(items)
    yield IndexError
    yield list.remove_at(index)


@Test
def remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = StaticArrayList.build(items)
    yield list.get_at(index)
    yield list.remove_at(index)


@Test
def remove_at_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = StaticArrayList.build(items)
    length = list.get_length()
    list.remove_at(index)
    yield length - 1
    yield list.get_length()


@Test
def insert_at_then_get_at_earlier(
    earlier_items: Annotated[Iterator[Item], GE(1)],
    item: Item,
    later_items: Iterator[Item],
    remove_index: Annotated[int, EQ("earlier_items")],
    early_index: Annotated[int, GE(0), LT("earlier_items")],
):
    list = StaticArrayList.build(chain(earlier_items, (item,), later_items))
    early_item = list.get_at(early_index)
    list.remove_at(remove_index)
    yield early_item
    yield list.get_at(early_index)


@Test
def remove_at_then_get_at_later(
    earlier_items: Iterator[Item],
    item: Item,
    later_items: Annotated[Iterator[Item], GE(1)],
    remove_index: Annotated[int, EQ("earlier_items")],
    late_index: Annotated[int, GE(0), LT("later_items")],
):
    list = StaticArrayList.build(chain(earlier_items, (item,), later_items))
    late_item = list.get_at(remove_index + 1 + late_index)
    list.remove_at(remove_index)
    yield late_item
    yield list.get_at(remove_index + late_index)


@Test
def remove_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GE("items")],
):
    list = StaticArrayList.build(items)
    yield IndexError
    yield list.remove_at(index)
