from collections.abc import Iterator
from typing import Annotated

from lib.array import Array
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Key, Value

from lab5.core.chaining_hash_map.exercise import ChainingHashMap


@Test
def contains_on_empty_map(
    key: Key,
):
    map = ChainingHashMap()
    yield False
    yield map.contains(key)


@Test
def contains(
    mappings: Annotated[Array[tuple[Key, Value]], GE(1)],
    index: Annotated[int, GE(0), LT("mappings")],
):
    map = ChainingHashMap.build(mappings.iterator())
    key, value = mappings.get_at(index)
    yield True
    yield map.contains(key)


@Test
def contains_not(
    unique_keys: Annotated[set[Key], GE(1)],
    values: Annotated[Iterator[Value], EQ("unique_keys")],
):
    keys = list(unique_keys)
    key = keys[0]
    other_keys = keys[1:]
    mappings = zip(other_keys, values)
    map = ChainingHashMap.build(mappings)
    yield False
    yield map.contains(key)


@Test
def contains_then_insert_then_get_length(
    mappings: Array[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator())
    old_length = map.get_length()
    if map.contains(key):
        new_length = old_length
    else:
        new_length = old_length + 1
    map.insert(key, value)
    yield new_length
    yield map.get_length()


@Test
def get_length(
    mappings: Array[tuple[Key, Value]],
):
    map = ChainingHashMap.build(mappings.iterator())
    unique_key_count = len(set(key for key, value in mappings.iterator()))
    yield unique_key_count
    yield map.get_length()


@Test
def get_on_empty_map(
    key: Key,
):
    map = ChainingHashMap()
    yield KeyError
    yield map.get(key)


@Test
def insert_on_empty_map_then_get_length(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    yield 1
    yield map.get_length()


@Test
def insert_twice_on_empty_map_then_get_length(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    map = ChainingHashMap()
    map.insert(key, old_value)
    map.insert(key, new_value)
    yield 1
    yield map.get_length()


@Test
def insert_on_empty_map_then_contains(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    yield True
    yield map.contains(key)


@Test
def insert_on_empty_map_then_remove_then_contains(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    map.remove(key)
    yield False
    yield map.contains(key)


@Test
def insert_on_empty_map_then_get(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    yield value
    yield map.get(key)


@Test
def insert_twice_on_empty_map_then_get(
    key: Key,
    old_value: Value,
    new_value: Value,
):
    map = ChainingHashMap()
    map.insert(key, old_value)
    map.insert(key, new_value)
    yield new_value
    yield map.get(key)


@Test
def insert_on_empty_map_then_remove(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    yield value
    yield map.remove(key)


@Test
def insert_on_empty_map_then_remove_twice(
    key: Key,
    value: Value,
):
    map = ChainingHashMap()
    map.insert(key, value)
    map.remove(key)
    yield KeyError
    yield map.remove(key)


@Test
def insert_then_get_chain_count(
    mappings: Array[tuple[Key, Value]],
    max_load_factor: Annotated[int, GE(1), LE(3)],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator(), max_load_factor=max_load_factor)
    old_chain_count = map.get_chain_count()
    map.insert(key, value)
    if map.get_length() > old_chain_count * max_load_factor:
        new_chain_count = old_chain_count * 2
    else:
        new_chain_count = old_chain_count
    yield new_chain_count
    yield map.get_chain_count()


@Test
def insert_then_contains(
    mappings: Array[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator())
    map.insert(key, value)
    yield True
    yield map.contains(key)


@Test
def insert_then_get(
    mappings: Array[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator())
    map.insert(key, value)
    yield value
    yield map.get(key)


@Test
def insert_then_remove(
    mappings: Array[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator())
    map.insert(key, value)
    yield value
    yield map.remove(key)


@Test
def insert_then_remove_twice(
    mappings: Array[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator())
    map.insert(key, value)
    map.remove(key)
    yield KeyError
    yield map.remove(key)


@Test
def remove_on_empty_map(
    key: Key,
):
    map = ChainingHashMap()
    yield KeyError
    yield map.remove(key)


@Test
def remove_then_get_chain_count(
    mappings: Array[tuple[Key, Value]],
    max_load_factor: Annotated[int, GE(1), LE(3)],
    key: Key,
    value: Value,
):
    map = ChainingHashMap.build(mappings.iterator(), max_load_factor=max_load_factor)
    map.insert(key, value)
    old_chain_count = map.get_chain_count()
    map.remove(key)
    if map.get_length() < max_load_factor * old_chain_count / 4:
        new_chain_count = max(1, old_chain_count // 2)
    else:
        new_chain_count = old_chain_count
    yield new_chain_count
    yield map.get_chain_count()
