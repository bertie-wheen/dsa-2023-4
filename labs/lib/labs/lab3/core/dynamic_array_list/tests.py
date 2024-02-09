from collections.abc import Iterator
from copy import copy
from itertools import chain
from typing import Annotated

from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab3.core.dynamic_array_list.exercise import DynamicArrayList


@Test
def resize_then_get_capacity(
    items: Iterator[Item],
    old_capacity: Annotated[int, GE("items")],
    new_capacity: Annotated[int, GE("items")],
):
    list = DynamicArrayList.build(items, capacity=old_capacity)
    list.resize(new_capacity)
    yield new_capacity
    yield list.get_capacity()


@Test
def resize_then_get_length(
    items: Iterator[Item],
    old_capacity: Annotated[int, GE("items")],
    new_capacity: Annotated[int, GE("items")],
):
    list = DynamicArrayList.build(items, capacity=old_capacity)
    length = list.get_length()
    list.resize(new_capacity)
    yield length
    yield list.get_length()


@Test
def resize_then_get_at(
    items: Annotated[Iterator[Item], GE(1)],
    old_capacity: Annotated[int, GE("items")],
    new_capacity: Annotated[int, GE("items")],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DynamicArrayList.build(items, capacity=old_capacity)
    item = list.get_at(index)
    list.resize(new_capacity)
    yield item
    yield list.get_at(index)


@Test
def get_at_then_remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DynamicArrayList.build(items)
    yield list.get_at(index)
    yield list.remove_at(index)


@Test
def insert_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
    item: Item,
):
    list = DynamicArrayList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def insert_at_first_repeatedly_then_reverse_iterator(
    items: Iterator[Item],
):
    list = DynamicArrayList()
    for item in copy(items):
        list.insert_at(0, item)
    yield items
    yield list.reverse_iterator()


@Test
def insert_at_then_get_capacity(
    items: Annotated[Iterator[Item], GE(0)],
    old_capacity: Annotated[int, GE("items")],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DynamicArrayList.build(items, capacity=old_capacity)
    length = list.get_length()
    if length < old_capacity:
        new_capacity = old_capacity
    elif old_capacity == 0:
        new_capacity = 1
    else:
        new_capacity = 2 * old_capacity
    list.insert_at(index, item)
    yield new_capacity
    yield list.get_capacity()


@Test
def insert_at_then_get_length(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DynamicArrayList.build(items)
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
    list = DynamicArrayList.build(chain(earlier_items, later_items))
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
    list = DynamicArrayList.build(items)
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
    list = DynamicArrayList.build(chain(earlier_items, later_items))
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
    list = DynamicArrayList.build(items)
    list.insert_at(index, item)
    yield item
    yield list.remove_at(index)


@Test
def insert_at_when_should_grow(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DynamicArrayList.build(items)
    old_capacity = list.get_capacity()
    list.insert_at(index, item)
    if old_capacity == 0:
        new_capacity = 1
    else:
        new_capacity = 2 * old_capacity
    yield new_capacity
    yield list.get_capacity()


@Test
def insert_at_when_should_not_grow(
    items: Iterator[Item],
    capacity: Annotated[int, GT("items")],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DynamicArrayList.build(items, capacity=capacity)
    list.insert_at(index, item)
    yield capacity
    yield list.get_capacity()


@Test
def insert_at_last_repeatedly_then_iterator(
    items: Iterator[Item],
):
    list = DynamicArrayList()
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
    list = DynamicArrayList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def remove_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
):
    list = DynamicArrayList.build(items)
    yield IndexError
    yield list.remove_at(index)


@Test
def remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DynamicArrayList.build(items)
    yield list.get_at(index)
    yield list.remove_at(index)


@Test
def remove_at_then_get_capacity(
    items: Annotated[Iterator[Item], GE(1)],
    old_capacity: Annotated[int, GE("items")],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DynamicArrayList.build(items, capacity=old_capacity)
    if (list.get_length() - 1) <= old_capacity // 4:
        new_capacity = old_capacity // 2
    else:
        new_capacity = old_capacity
    list.remove_at(index)
    yield new_capacity
    yield list.get_capacity()


@Test
def remove_at_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DynamicArrayList.build(items)
    length = list.get_length()
    list.remove_at(index)
    yield length - 1
    yield list.get_length()


@Test
def remove_at_then_get_at_earlier(
    earlier_items: Annotated[Iterator[Item], GE(1)],
    item: Item,
    later_items: Iterator[Item],
    remove_index: Annotated[int, EQ("earlier_items")],
    early_index: Annotated[int, GE(0), LT("earlier_items")],
):
    list = DynamicArrayList.build(chain(earlier_items, (item,), later_items))
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
    list = DynamicArrayList.build(chain(earlier_items, (item,), later_items))
    late_item = list.get_at(remove_index + 1 + late_index)
    list.remove_at(remove_index)
    yield late_item
    yield list.get_at(remove_index + late_index)


@Test
def remove_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GE("items")],
):
    list = DynamicArrayList.build(items)
    yield IndexError
    yield list.remove_at(index)
