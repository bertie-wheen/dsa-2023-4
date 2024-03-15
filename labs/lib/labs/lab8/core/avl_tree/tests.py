from collections.abc import Iterator
from math import ceil, log2
import random
from typing import Annotated, Optional

from lib.array import Array
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item, Key, Value

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.merge_sort import merge_sort
from lab8.core.avl_tree.exercise import AVLTree, _AVLSubtree


def is_sorted(tree: AVLTree[Key, Value]) -> bool:
    if tree.is_empty():
        return True
    keys = tree.keys_iterator()
    previous_key = next(keys)
    for key in keys:
        if previous_key > key:
            return False
        previous_key = key
    return True


def get_correct_balance_factor(subtree: _AVLSubtree[Key, Value]) -> int:
    left_height = get_correct_height(subtree._left)
    right_height = get_correct_height(subtree._right)
    return right_height - left_height


def get_correct_height(subtree: Optional[_AVLSubtree[Key, Value]]) -> int:
    if subtree is None:
        return -1
    left_height = get_correct_height(subtree._left)
    right_height = get_correct_height(subtree._right)
    return 1 + max(left_height, right_height)


def shuffled(array: Array[Item]) -> Array[Item]:
    tmp = list(array.iterator())
    random.shuffle(tmp)
    return Array.build(iter(tmp))


@Test
def insert_on_empty_tree_then_get(
    key: Key,
    value: Value,
):
    tree = AVLTree()
    tree.insert(key, value)
    yield value
    yield tree.get(key)


@Test
def insert_twice_on_empty_tree_then_get(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    tree = AVLTree()
    tree.insert(key, old_value)
    tree.insert(key, new_value)
    yield new_value
    yield tree.get(key)


@Test
def insert_twice_on_empty_tree_then_get_length(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    tree = AVLTree()
    tree.insert(key, old_value)
    tree.insert(key, new_value)
    yield 1
    yield tree.get_length()


@Test
def insert_on_empty_tree_then_remove(
    key: Key,
    value: Value,
):
    tree = AVLTree()
    tree.insert(key, value)
    yield value
    yield tree.remove(key)


@Test
def insert_on_empty_tree_then_remove_then_contains(
    key: Key,
    value: Value,
):
    tree = AVLTree()
    tree.insert(key, value)
    tree.remove(key)
    yield False
    yield tree.contains(key)


@Test
def insert_on_empty_tree_then_remove_then_get(
    key: Key,
    value: Value,
):
    tree = AVLTree()
    tree.insert(key, value)
    tree.remove(key)
    yield False
    yield tree.contains(key)


@Test
def insert_on_empty_tree_then_remove_then_get_length(
    key: Key,
    value: Value,
):
    tree = AVLTree()
    tree.insert(key, value)
    tree.remove(key)
    yield 0
    yield tree.get_length()


@Test
def insert_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, value)
    yield True
    yield tree.contains(key)


@Test
def insert_then_is_sorted(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, value)
    yield True
    yield is_sorted(tree)


@Test
def insert_then_get_length(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    if tree.contains(key):
        length = tree.get_length()
    else:
        length = tree.get_length() + 1
    tree.insert(key, value)
    yield length
    yield tree.get_length()


@Test
def insert_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, value)
    yield value
    yield tree.get(key)


@Test
def insert_twice_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    old_value: Value,
    new_value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, old_value)
    tree.insert(key, new_value)
    yield new_value
    yield tree.get(key)


@Test
def insert_all_and_always_contains(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_contains = True
    for key, value in mappings:
        tree.insert(key, value)
        if not tree.contains(key):
            always_contains = False
            break
    yield True
    yield always_contains


@Test
def insert_all_and_always_correct_balance_factor(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_correct_balance_factor = True
    for key, value in mappings:
        tree.insert(key, value)
        for subtree in tree._root.iterator():
            balance_factor = subtree.get_balance_factor()
            correct_balance_factor = get_correct_balance_factor(subtree)
            if balance_factor != correct_balance_factor:
                always_correct_balance_factor = False
                break
    yield True
    yield always_correct_balance_factor


@Test
def insert_all_and_always_correct_height(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_correct_height = True
    for key, value in mappings:
        tree.insert(key, value)
        for subtree in tree._root.iterator():
            height = subtree.get_height()
            correct_height = get_correct_height(subtree)
            if height != correct_height:
                always_correct_height = False
                break
    yield True
    yield always_correct_height


@Test
def insert_all_and_always_correct_length(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_correct_length = True
    for key, value in mappings:
        if tree.contains(key):
            correct_length = tree.get_length()
        else:
            correct_length = tree.get_length() + 1
        tree.insert(key, value)
        length = tree.get_length()
        if length != correct_length:
            always_correct_length = False
            break
    yield True
    yield always_correct_length


@Test
def insert_all_and_always_is_balanced(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_is_balanced = True
    for key, value in mappings:
        tree.insert(key, value)
        length = tree.get_length()
        height = tree.get_height()
        max_height = ceil(log2(length)) + 1
        if height > max_height:
            always_is_balanced = False
            break
    yield True
    yield always_is_balanced


@Test
def insert_all_and_always_is_sorted(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree()
    always_is_sorted = True
    for key, value in mappings:
        tree.insert(key, value)
        if not is_sorted(tree):
            always_is_sorted = False
            break
    yield True
    yield always_is_sorted


@Test
def insert_then_remove_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, value)
    tree.remove(key)
    yield False
    yield tree.contains(key)


@Test
def insert_then_remove_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    tree = AVLTree.build(mappings)
    tree.insert(key, value)
    tree.remove(key)
    yield KeyError
    yield tree.get(key)


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
    tree = AVLTree.build(mappings.iterator())
    yield the_values.get_last()
    yield tree.remove(the_key)


@Test
def remove_then_contains(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    tree = AVLTree.build(mappings.iterator())
    tree.remove(the_key)
    yield False
    yield tree.contains(the_key)


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
    tree = AVLTree.build(mappings.iterator())
    tree.remove(the_key)
    yield only_key
    yield tree.is_empty()


@Test
def remove_then_get_length(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    tree = AVLTree.build(mappings.iterator())
    length = tree.get_length() - 1
    tree.remove(the_key)
    yield length
    yield tree.get_length()


@Test
def remove_then_get(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    tree = AVLTree.build(mappings.iterator())
    tree.remove(the_key)
    yield KeyError
    yield tree.get(the_key)


@Test
def remove_then_is_sorted(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    an_index: Annotated[int, GE(0), LT("mappings")],
):
    the_key, a_value = mappings.get_at(an_index)
    tree = AVLTree.build(mappings.iterator())
    tree.remove(the_key)
    yield True
    yield is_sorted(tree)


@Test
def remove_all_and_always_correct_balance_factor(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree.build(mappings)
    keys = shuffled(Array.build(tree.keys_iterator()))
    always_correct_balance_factor = True
    for key in keys.iterator():
        tree.remove(key)
        if tree.is_empty():
            continue
        for subtree in tree._root.iterator():
            balance_factor = subtree.get_balance_factor()
            correct_balance_factor = get_correct_balance_factor(subtree)
            if balance_factor != correct_balance_factor:
                always_correct_balance_factor = False
                break
    yield True
    yield always_correct_balance_factor


@Test
def remove_all_and_always_correct_height(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree.build(mappings)
    keys = shuffled(Array.build(tree.keys_iterator()))
    always_correct_height = True
    for key in keys.iterator():
        tree.remove(key)
        if tree.is_empty():
            continue
        for subtree in tree._root.iterator():
            height = subtree.get_height()
            correct_height = get_correct_height(subtree)
            if height != correct_height:
                always_correct_height = False
                break
    yield True
    yield always_correct_height


@Test
def remove_all_and_always_correct_length(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree.build(mappings)
    keys = shuffled(Array.build(tree.keys_iterator()))
    always_correct_length = True
    for key in keys.iterator():
        length = tree.get_length() - 1
        tree.remove(key)
        if length != tree.get_length():
            always_correct_length = False
            break
    yield True
    yield always_correct_length


@Test
def remove_all_and_always_is_balanced(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree.build(mappings)
    keys = shuffled(Array.build(tree.keys_iterator()))
    always_is_balanced = True
    for key in keys.iterator():
        tree.remove(key)
        length = tree.get_length()
        height = tree.get_height()
        if not tree.is_empty() and height > ceil(log2(length)) + 1:
            always_is_balanced = False
            break
    yield True
    yield always_is_balanced


@Test
def remove_all_and_always_is_sorted(
    mappings: Annotated[Iterator[tuple[Key, Value]], GE(1)],
):
    tree = AVLTree.build(mappings)
    keys = shuffled(Array.build(tree.keys_iterator()))
    always_is_sorted = True
    for key in keys.iterator():
        tree.remove(key)
        if not is_sorted(tree):
            always_is_sorted = False
            break
    yield True
    yield always_is_sorted

