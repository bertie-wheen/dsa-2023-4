from collections.abc import Iterator

from lib.test import Test
from lib.type_vars import Key, Value

from lab4.core.sorted_array_map.exercise import SortedArrayMap


def is_sorted(map: SortedArrayMap[Key, Value]) -> bool:
    for index in range(map.get_length() - 1):
        if map._array_list.get_at(index) > map._array_list.get_at(index + 1):
            return False
    return True


@Test
def insert_on_empty_map_then_get_length(
    key: Key,
    value: Value,
):
    map = SortedArrayMap()
    map.insert(key, value)
    yield 1
    yield map.get_length()


@Test
def insert_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    yield True
    yield map.contains(key)


@Test
def insert_then_is_sorted(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    yield True
    yield is_sorted(map)


@Test
def insert_then_get_length(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    if map.contains(key):
        length = map.get_length()
    else:
        length = map.get_length() + 1
    map.insert(key, value)
    yield length
    yield map.get_length()


@Test
def insert_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    yield value
    yield map.get(key)


@Test
def insert_then_remove(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    yield value
    yield map.remove(key)


@Test
def insert_then_remove_then_contains(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    map.remove(key)
    yield False
    yield map.contains(key)


@Test
def insert_then_remove_then_get(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
    value: Value,
):
    map = SortedArrayMap.build(mappings)
    map.insert(key, value)
    map.remove(key)
    yield KeyError
    yield map.get(key)


@Test
def insert_on_empty_map_then_remove_then_get_length(
    key: Key,
    value: Value,
):
    map = SortedArrayMap()
    map.insert(key, value)
    map.remove(key)
    yield 0
    yield map.get_length()


@Test
def remove_on_empty_map(
    key: Key,
):
    map = SortedArrayMap()
    yield KeyError
    yield map.remove(key)


@Test
def remove(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
):
    map = SortedArrayMap.build(mappings)
    if map.contains(key):
        remove_result = map.get(key)
    else:
        remove_result = KeyError
    yield remove_result
    yield map.remove(key)


@Test
def remove_then_is_sorted(
    mappings: Iterator[tuple[Key, Value]],
    key: Key,
):
    map = SortedArrayMap.build(mappings)
    try:
        map.remove(key)
    except KeyError:
        pass
    yield True
    yield is_sorted(map)
