from collections.abc import Iterator
from typing import Annotated

from lib.array import Array
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Key, Value

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.unsorted_array_map import UnsortedArrayMap
from lab7.core.binary_search_tree.exercise import BinarySearchTree


def is_sorted(bst: BinarySearchTree[Key, Value]) -> bool:
    if bst.is_empty():
        return True
    keys = bst.keys_iterator()
    previous_key = next(keys)
    for key in keys:
        if previous_key > key:
            return False
        previous_key = key
    return True


@Test
def get(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    the_values = DynamicArrayList()
    for key, value in mappings.iterator():
        if key == the_key:
            the_values.insert_last(value)
    bst = BinarySearchTree.build(mappings.iterator())
    yield the_values.get_last()
    yield bst.get(the_key)


@Test
def get_then_is_sorted(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    bst = BinarySearchTree.build(mappings.iterator())
    bst.get(the_key)
    yield True
    yield is_sorted(bst)


@Test
def insert_on_empty_bst_then_get(
    key: Key,
    value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, value)
    yield value
    yield bst.get(key)


@Test
def insert_twice_on_empty_bst_then_get(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, old_value)
    bst.insert(key, new_value)
    yield new_value
    yield bst.get(key)


@Test
def insert_twice_on_empty_bst_then_get_length(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, old_value)
    bst.insert(key, new_value)
    yield 1
    yield bst.get_length()


@Test
def insert_on_empty_bst_then_remove(
    key: Key,
    value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, value)
    yield value
    yield bst.remove(key)


@Test
def insert_on_empty_bst_then_remove_then_contains(
    key: Key,
    value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, value)
    bst.remove(key)
    yield False
    yield bst.contains(key)


@Test
def insert_on_empty_bst_then_remove_then_get(
    key: Key,
    value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, value)
    bst.remove(key)
    yield False
    yield bst.contains(key)


@Test
def insert_on_empty_bst_then_remove_then_get_length(
    key: Key,
    value: Value,
):
    bst = BinarySearchTree()
    bst.insert(key, value)
    bst.remove(key)
    yield 0
    yield bst.get_length()


@Test
def insert_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, value)
    yield True
    yield bst.contains(key)


@Test
def insert_then_is_sorted(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, value)
    yield True
    yield is_sorted(bst)


@Test
def insert_then_get_length(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    if bst.contains(key):
        length = bst.get_length()
    else:
        length = bst.get_length() + 1
    bst.insert(key, value)
    yield length
    yield bst.get_length()


@Test
def insert_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, value)
    yield value
    yield bst.get(key)


@Test
def insert_twice_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    old_value: Value,
    new_value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, old_value)
    bst.insert(key, new_value)
    yield new_value
    yield bst.get(key)


@Test
def insert_then_remove_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, value)
    bst.remove(key)
    yield False
    yield bst.contains(key)


@Test
def insert_then_remove_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    bst = BinarySearchTree.build(mappings)
    bst.insert(key, value)
    bst.remove(key)
    yield KeyError
    yield bst.get(key)


@Test
def remove(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    the_values = DynamicArrayList()
    for key, value in mappings.iterator():
        if key == the_key:
            the_values.insert_last(value)
    bst = BinarySearchTree.build(mappings.iterator())
    yield the_values.get_last()
    yield bst.remove(the_key)


@Test
def remove_then_contains(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    bst = BinarySearchTree.build(mappings.iterator())
    bst.remove(the_key)
    yield False
    yield bst.contains(the_key)


@Test
def remove_then_is_empty(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    only_key = True
    for key, value in mappings.iterator():
        if key != the_key:
            only_key = False
            break
    bst = BinarySearchTree.build(mappings.iterator())
    bst.remove(the_key)
    yield only_key
    yield bst.is_empty()


@Test
def remove_then_get_length(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    bst = BinarySearchTree.build(mappings.iterator())
    length = bst.get_length() - 1
    bst.remove(the_key)
    yield length
    yield bst.get_length()


@Test
def remove_then_get(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    bst = BinarySearchTree.build(mappings.iterator())
    bst.remove(the_key)
    yield KeyError
    yield bst.get(the_key)


@Test
def remove_then_is_sorted(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    bst = BinarySearchTree.build(mappings.iterator())
    bst.remove(the_key)
    yield True
    yield is_sorted(bst)


@Test
def remove_all_and_always_is_sorted(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    keys = set(key for key, value in mappings.iterator())
    bst = BinarySearchTree.build(mappings.iterator())
    always_sorted = True
    for key in keys:
        bst.remove(key)
        if not is_sorted(bst):
            always_sorted = False
            break
    yield True
    yield always_sorted
