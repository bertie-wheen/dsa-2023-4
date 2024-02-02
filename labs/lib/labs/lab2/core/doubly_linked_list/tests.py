from collections.abc import Iterator
from copy import copy
from typing import Annotated

from lib.array import Array
from lib.errors import EmptyCollectionError
from lib.iterator import iterator
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab2.core.doubly_linked_list.exercise import DoublyLinkedList


@Test
def get_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.get_at(index)


@Test
def get_at_first_then_get_first(
    items: Annotated[Iterator[Item], GE(1)],
):
    list = DoublyLinkedList.build(items)
    yield list.get_at(0)
    yield list.get_first()


@Test
def get_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    items_array = Array.build(copy(items))
    list = DoublyLinkedList.build(items)
    yield items_array.get_at(index)
    yield list.get_at(index)


@Test
def get_at_then_calculate_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    list.get_at(index)
    length = 0
    for _ in list.iterator():
        length += 1
    yield list.get_length()
    yield length


@Test
def get_at_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    length = list.get_length()
    list.get_at(index)
    yield length
    yield list.get_length()


@Test
def get_at_then_get_first(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    first = list.get_first()
    list.get_at(index)
    yield first
    yield list.get_first()


@Test
def get_at_then_get_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    yield list.get_at(index)
    yield list.get_at(index)


@Test
def get_at_then_get_last(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    last = list.get_last()
    list.get_at(index)
    yield last
    yield list.get_last()


@Test
def get_at_then_remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    yield list.get_at(index)
    yield list.remove_at(index)


@Test
def get_at_last_then_get_last(
    items: Annotated[Iterator[Item], GE(1)],
):
    list = DoublyLinkedList.build(items)
    yield list.get_at(list.get_length() - 1)
    yield list.get_last()


@Test
def get_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GE("items")],
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.get_at(index)


@Test
def set_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.set_at(index, item)


@Test
def set_at_first_then_get_first(
    items: Annotated[Iterator[Item], GE(1)],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.set_at(0, item)
    yield item
    yield list.get_first()


@Test
def set_at_non_last_then_get_last(
    items: Annotated[Iterator[Item], GE(2)],
    index_plus_one: Annotated[int, GE(1), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    index = index_plus_one - 1
    last = list.get_last()
    list.set_at(index, item)
    yield last
    yield list.get_last()


@Test
def set_at_then_calculate_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.set_at(index, item)
    length = 0
    for _ in list.iterator():
        length += 1
    yield list.get_length()
    yield length


@Test
def set_at_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    length = list.get_length()
    list.set_at(index, item)
    yield length
    yield list.get_length()


@Test
def set_at_then_get_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.set_at(index, item)
    yield item
    yield list.get_at(index)


@Test
def set_at_then_remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.set_at(index, item)
    yield item
    yield list.remove_at(index)


@Test
def set_at_non_first_then_get_first(
    items: Annotated[Iterator[Item], GE(2)],
    index: Annotated[int, GE(1), LT("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    first = list.get_first()
    list.set_at(index, item)
    yield first
    yield list.get_first()


@Test
def set_at_last_then_get_last(
    items: Annotated[Iterator[Item], GE(1)],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.set_at(list.get_length() - 1, item)
    yield item
    yield list.get_last()


@Test
def set_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.set_at(index, item)


@Test
def insert_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def insert_at_first_then_get_first(
    items: Iterator[Item],
    first_item: Item,
):
    list = DoublyLinkedList.build(items)
    list.insert_at(0, first_item)
    yield first_item
    yield list.get_first()


@Test
def insert_at_first_repeatedly_then_reverse_iterator(
    items: Iterator[Item],
):
    list = DoublyLinkedList()
    for item in copy(items):
        list.insert_at(0, item)
    yield items
    yield list.reverse_iterator()


@Test
def insert_at_non_first_then_get_first(
    items: Annotated[Iterator[Item], GE(2)],
    index: Annotated[int, GE(1), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    first = list.get_first()
    list.insert_at(index, item)
    yield first
    yield list.get_first()


@Test
def insert_at_then_calculate_length(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.insert_at(index, item)
    length = 0
    for _ in list.iterator():
        length += 1
    yield list.get_length()
    yield length


@Test
def insert_at_then_get_length(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    length = list.get_length()
    list.insert_at(index, item)
    yield length + 1
    yield list.get_length()


@Test
def insert_at_then_get_at(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.insert_at(index, item)
    yield item
    yield list.get_at(index)


@Test
def insert_at_then_remove_at(
    items: Iterator[Item],
    index: Annotated[int, GE(0), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    list.insert_at(index, item)
    yield item
    yield list.remove_at(index)


@Test
def insert_at_non_last_then_get_last(
    items: Annotated[Iterator[Item], GE(2)],
    index_plus_one: Annotated[int, GE(1), LE("items")],
    item: Item,
):
    list = DoublyLinkedList.build(items)
    index = index_plus_one - 1
    last = list.get_last()
    list.insert_at(index, item)
    yield last
    yield list.get_last()


@Test
def insert_at_last_then_get_last(
    items: Iterator[Item],
    last_item: Item,
):
    list = DoublyLinkedList.build(items)
    list.insert_at(list.get_length(), last_item)
    yield last_item
    yield list.get_last()


@Test
def insert_at_last_repeatedly_then_iterator(
    items: Iterator[Item],
):
    list = DoublyLinkedList()
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
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.insert_at(index, item)


@Test
def remove_at_below_lower_bound(
    items: Iterator[Item],
    index: Annotated[int, LT(0)],
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.remove_at(index)


@Test
def remove_at_first(
    items: Annotated[Iterator[Item], GE(1)],
):
    list = DoublyLinkedList.build(items)
    yield list.get_first()
    yield list.remove_at(0)


@Test
def remove_at_first_then_get_first(
    items: Annotated[Iterator[Item], GE(1)],
):
    items_array = Array.build(copy(items))
    list = DoublyLinkedList.build(items)
    list.remove_at(0)
    if items_array.get_length() == 1:
        first = EmptyCollectionError
    else:
        first = items_array.get_at(1)
    yield first
    yield list.get_first()


@Test
def remove_at_non_first_then_get_first(
    items: Annotated[Iterator[Item], GE(2)],
    index: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    first = list.get_first()
    list.remove_at(index)
    yield first
    yield list.get_first()


@Test
def remove_at(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    items_array = Array.build(copy(items))
    list = DoublyLinkedList.build(items)
    yield items_array.get_at(index)
    yield list.remove_at(index)


@Test
def remove_at_then_calculate_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    list.remove_at(index)
    length = 0
    for _ in list.iterator():
        length += 1
    yield list.get_length()
    yield length


@Test
def remove_at_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    length = list.get_length()
    list.remove_at(index)
    yield length - 1
    yield list.get_length()


@Test
def remove_at_non_last_then_get_last(
    items: Annotated[Iterator[Item], GE(2)],
    index_plus_one: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    index = index_plus_one - 1
    last = list.get_last()
    list.remove_at(index)
    yield last
    yield list.get_last()


@Test
def remove_at_last(
    items: Annotated[Iterator[Item], GE(1)],
):
    list = DoublyLinkedList.build(items)
    yield list.get_last()
    yield list.remove_at(list.get_length() - 1)


@Test
def remove_at_last_then_get_last(
    items: Annotated[Iterator[Item], GE(1)],
):
    items_array = Array.build(copy(items))
    list = DoublyLinkedList.build(items)
    list.remove_at(list.get_length() - 1)
    if items_array.get_length() == 1:
        last = EmptyCollectionError
    else:
        last = items_array.get_at(items_array.get_length() - 2)
    yield last
    yield list.get_last()


@Test
def remove_at_above_upper_bound(
    items: Iterator[Item],
    index: Annotated[int, GE("items")],
):
    list = DoublyLinkedList.build(items)
    yield IndexError
    yield list.remove_at(index)


@Test
def reverse_iterator_on_empty_list():
    list = DoublyLinkedList()
    yield iterator()
    yield list.reverse_iterator()


@Test
def reverse_iterator(
    items: Iterator[Item],
):
    items_array = Array.build(copy(items))
    list = DoublyLinkedList.build(items)
    yield items_array.reverse_iterator()
    yield list.reverse_iterator()


@Test
def reverse_iterator_then_calculate_length(
    items: Iterator[Item],
):
    list = DoublyLinkedList.build(items)
    for _ in list.reverse_iterator():
        pass
    length = 0
    for _ in list.iterator():
        length += 1
    yield list.get_length()
    yield length


@Test
def reverse_iterator_then_get_length(
    items: Iterator[Item],
):
    list = DoublyLinkedList.build(items)
    length = list.get_length()
    for _ in list.reverse_iterator():
        pass
    yield length
    yield list.get_length()


@Test
def reverse_iterator_then_get_first(
    items: Iterator[Item],
):
    list = DoublyLinkedList.build(items)
    if list.is_empty():
        first = EmptyCollectionError
    else:
        first = list.get_first()
    for _ in list.reverse_iterator():
        pass
    yield first
    yield list.get_first()


@Test
def reverse_iterator_then_get_last(
    items: Iterator[Item],
):
    list = DoublyLinkedList.build(items)
    if list.is_empty():
        last = EmptyCollectionError
    else:
        last = list.get_last()
    for _ in list.reverse_iterator():
        pass
    yield last
    yield list.get_last()


@Test
def insert_previous_on_first_then_get_previous(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    node.insert_previous(previous_item)
    yield previous_item
    yield node.get_previous()


@Test
def insert_previous_on_first_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.get()


@Test
def insert_previous_on_first_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    if list.get_length() == 1:
        next_item = ValueError
    else:
        next_item = node.get_next()
    node.insert_previous(previous_item)
    yield next_item
    yield node.get_next()


@Test
def insert_previous_on_first_then_remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    node.insert_previous(previous_item)
    yield previous_item
    yield node.remove_previous()


@Test
def insert_previous_on_first_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.remove()


@Test
def insert_previous_on_first_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    if list.get_length() == 1:
        next_item = ValueError
    else:
        next_item = node.get_next()
    node.insert_previous(previous_item)
    yield next_item
    yield node.remove_next()


@Test
def insert_previous_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    length = list.get_length()
    node.insert_previous(previous_item)
    yield length + 1
    yield list.get_length()


@Test
def insert_previous_then_get_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    node.insert_previous(previous_item)
    yield previous_item
    yield node.get_previous()


@Test
def insert_previous_then_get_previous_on_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == 0:
        old_previous_item = ValueError
    else:
        old_previous_item = node.get_previous()
    node.insert_previous(previous_item)
    yield old_previous_item
    yield node.get_previous_node().get_previous()


@Test
def insert_previous_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.get()


@Test
def insert_previous_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == list.get_length() - 1:
        next_item = ValueError
    else:
        next_item = node.get_next()
    node.insert_previous(previous_item)
    yield next_item
    yield node.get_next()


@Test
def insert_previous_then_remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    node.insert_previous(previous_item)
    yield previous_item
    yield node.remove_previous()


@Test
def insert_previous_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.remove()


@Test
def insert_previous_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == list.get_length() - 1:
        next_item = ValueError
    else:
        next_item = node.get_next()
    node.insert_previous(previous_item)
    yield next_item
    yield node.remove_next()


@Test
def insert_previous_on_last_then_get_previous(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_previous(previous_item)
    yield previous_item
    yield node.get_previous()


@Test
def insert_previous_on_last_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.get()


@Test
def insert_previous_on_last_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_previous(previous_item)
    yield ValueError
    yield node.get_next()


@Test
def insert_previous_on_last_then_remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_previous(previous_item)
    yield previous_item
    yield node.remove_previous()


@Test
def insert_previous_on_last_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    item = node.get()
    node.insert_previous(previous_item)
    yield item
    yield node.remove()


@Test
def insert_previous_on_last_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    previous_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_previous(previous_item)
    yield ValueError
    yield node.remove_next()


@Test
def insert_next_on_first_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.get()


@Test
def insert_next_on_first_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    node.insert_next(next_item)
    yield next_item
    yield node.get_next()


@Test
def insert_next_on_first_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.remove()


@Test
def insert_next_on_first_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_first_node()
    node.insert_next(next_item)
    yield next_item
    yield node.remove_next()


@Test
def insert_next_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    length = list.get_length()
    node.insert_next(next_item)
    yield length + 1
    yield list.get_length()


@Test
def insert_next_then_get_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == 0:
        previous_item = ValueError
    else:
        previous_item = node.get_previous()
    node.insert_next(next_item)
    yield previous_item
    yield node.get_previous()


@Test
def insert_next_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.get()


@Test
def insert_next_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    node.insert_next(next_item)
    yield next_item
    yield node.get_next()


@Test
def insert_next_then_get_next_on_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == list.get_length() - 1:
        old_next_item = ValueError
    else:
        old_next_item = node.get_next()
    node.insert_next(next_item)
    yield old_next_item
    yield node.get_next_node().get_next()


@Test
def insert_next_then_remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == 0:
        previous_item = ValueError
    else:
        previous_item = node.get_previous()
    node.insert_next(next_item)
    yield previous_item
    yield node.remove_previous()


@Test
def insert_next_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.remove()


@Test
def insert_next_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    node.insert_next(next_item)
    yield next_item
    yield node.remove_next()


@Test
def insert_next_then_remove_next_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == list.get_length() - 1:
        old_next_item = ValueError
    else:
        old_next_item = node.get_next()
    node.insert_next(next_item)
    node.remove_next()
    yield old_next_item
    yield node.get_next()


@Test
def insert_next_on_last_then_get_previous(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    if list.get_length() == 1:
        previous_item = ValueError
    else:
        previous_item = node.get_previous()
    node.insert_next(next_item)
    yield previous_item
    yield node.get_previous()


@Test
def insert_next_on_last_then_get(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.get()


@Test
def insert_next_on_last_then_get_next(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_next(next_item)
    yield next_item
    yield node.get_next()


@Test
def insert_next_on_last_then_remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    if list.get_length() == 1:
        previous_item = ValueError
    else:
        previous_item = node.get_previous()
    node.insert_next(next_item)
    yield previous_item
    yield node.remove_previous()


@Test
def insert_next_on_last_then_remove(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    item = node.get()
    node.insert_next(next_item)
    yield item
    yield node.remove()


@Test
def insert_next_on_last_then_remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    next_item: Item,
):
    list = DoublyLinkedList.build(items)
    node = list.get_last_node()
    node.insert_next(next_item)
    yield next_item
    yield node.remove_next()


@Test
def remove_previous(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == 0:
        previous_item = ValueError
    else:
        previous_item = node.get_previous()
    yield previous_item
    yield node.remove_previous()


@Test
def remove_previous_then_get_length(
    items: Annotated[Iterator[Item], GE(2)],
    index: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    length = list.get_length()
    node.remove_previous()
    yield length - 1
    yield list.get_length()


@Test
def remove_previous_on_non_first(
    items: Annotated[Iterator[Item], GE(2)],
    index: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    previous_item = node.get_previous()
    yield previous_item
    yield node.remove_previous()


@Test
def remove(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    item = node.get()
    yield item
    yield node.remove()


@Test
def remove_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    length = list.get_length()
    node.remove()
    yield length - 1
    yield list.get_length()


@Test
def remove_next_on_non_last(
    items: Annotated[Iterator[Item], GE(2)],
    index_plus_one: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    index = index_plus_one - 1
    node = list.get_node_at(index)
    next_item = node.get_next()
    yield next_item
    yield node.remove_next()


@Test
def remove_next(
    items: Annotated[Iterator[Item], GE(1)],
    index: Annotated[int, GE(0), LT("items")],
):
    list = DoublyLinkedList.build(items)
    node = list.get_node_at(index)
    if index == list.get_length() - 1:
        next_item = ValueError
    else:
        next_item = node.get_next()
    yield next_item
    yield node.remove_next()


@Test
def remove_next_then_get_length(
    items: Annotated[Iterator[Item], GE(2)],
    index_plus_one: Annotated[int, GE(1), LT("items")],
):
    list = DoublyLinkedList.build(items)
    index = index_plus_one - 1
    node = list.get_node_at(index)
    length = list.get_length()
    node.remove_next()
    yield length - 1
    yield list.get_length()
