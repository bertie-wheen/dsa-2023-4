"""
Data Structures & Algorithms

Lab 5: Hash Maps

Probing Hash Maps Exercise
"""

from collections.abc import Iterator
from enum import Enum

from lib.array import Array
from lib.base import Base
from lib.type_vars import Key, Value

from lab5.core.hash_function import HashFunction


class EmptyCell(Base, Enum):
    NEVER_USED = 0
    NOW_UNUSED = 1


class ProbingHashMap(Base[Key, Value]):
    """
    A probing hash map.

    Space: O(self.get_capacity())
    """

    _array: "Array[tuple[Key, Value] | EmptyCell]"
    _length: int
    _max_load_factor: float
    _hash_function: HashFunction

    def __init__(self, max_load_factor: float = 0.8) -> None:
        """
        Initialize this probing hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter initial_capacity: the initial array capacity
        :parameter max_load_factor: the proportion of items to cells at which the table is considered overly full
        :raises ValueError: unless ``1/2 < max_load_factor <= 1``
        """
        if not 1 / 2 < max_load_factor <= 1:
            raise ValueError
        self._array = Array(1)
        self._array.set_at(0, EmptyCell.NEVER_USED)
        self._hash_function = HashFunction(1)
        self._length = 0
        self._max_load_factor = max_load_factor

    @staticmethod
    def build(items: Iterator[tuple[Key, Value]], max_load_factor: float = 0.8) -> "ProbingHashMap[Key, Value]":
        """
        Build a probing hash map containing the given items.

        +--------+---------------------------------------+
        | Time:  | O(build(items).get_length()) expected |
        +--------+---------------------------------------+
        | Space: | O(build(items).get_capacity())        |
        +--------+---------------------------------------+

        :parameter items: an iterator of initial items
        :parameter max_load_factor: the proportion of items to cells at which the table is considered overly full
        :returns: a probing hash map of those items
        :raises ValueError: unless ``1/2 < max_load_factor <= 1``
        """
        map = ProbingHashMap(max_load_factor=max_load_factor)
        for key, value in items:
            map.insert(key, value)
        return map

    def is_empty(self) -> bool:
        """
        Check if this map is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the map is empty, else ``False``
        """
        return self._length == 0

    def get_capacity(self) -> int:
        """
        Get the number of cells in this hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the cell count
        """
        return self._array.get_length()

    def _resize(self, new_capacity: int) -> None:
        """
        Change this hash map's capacity, redistribute the mappings, and choose a new random hash function.

        +--------+---------------------------------------+
        | Time:  | O(self.get_capacity() + new_capacity) |
        +--------+---------------------------------------+
        | Space: | O(new_capacity)                       |
        +--------+---------------------------------------+

        :parameter new_capacity: the new capacity
        :raises ValueError: if ``new_capacity < 1``
        """
        if new_capacity < 1:
            raise ValueError
        items = Array.build(self.iterator())
        self._array = Array(new_capacity)
        for index in range(self._array.get_length()):
            self._array.set_at(index, EmptyCell.NEVER_USED)
        self._hash_function = HashFunction(new_capacity)
        self._length = 0
        for key, value in items.iterator():
            self.insert(key, value)

    def optimize(self) -> None:
        """
        Improve this probing hash map's performance by redistributing the mappings and removing any previously-used
        cell markers.

        +--------+-----------------------+
        | Time:  | O(self.get_capacity() |
        +--------+-----------------------+
        | Space: | O(self.get_capacity() |
        +--------+-----------------------+

        :parameter new_capacity: the new capacity
        :raises ValueError: if ``new_capacity < 1``
        """
        capacity = self.get_capacity()
        self._resize(capacity)

    def contains(self, key: Key) -> bool:
        """
        Check if this map contains the given key.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: ``True`` if the key is in the map, else ``False``
        """
        raise NotImplementedError

    def get_length(self) -> int:
        """
        Get the number of items in this map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._length

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this map.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key is not in the map
        """
        raise NotImplementedError

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this map.
        If the key is already in the map, set it to map to the new value.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        raise NotImplementedError

    def remove(self, key: Key) -> Value:
        """
        Remove the mapping for the given key from this map, and return the value that it mapped to.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key was not in the map
        """
        raise NotImplementedError

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        """
        Get an iterator over the key/value pairs in this map.
        The iteration order is unspecified.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: an iterator over the map's items
        """
        for item in self._array.iterator():
            match item:
                case EmptyCell():
                    continue
            yield item

    def keys_iterator(self) -> Iterator[Key]:
        """
        Get an iterator over the keys in this map.
        The iteration order is unspecified.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: an iterator over the map's keys
        """
        for key, value in self.iterator():
            yield key

    def values_iterator(self) -> Iterator[Value]:
        """
        Get an iterator over the values in this map.
        The iteration order is unspecified.
        If the same value is mapped to by multiple keys, it will occur multiple times.

        +--------+------------------------+
        | Time:  | O(self.get_capacity()) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: an iterator over the map's values
        """
        for key, value in self.iterator():
            yield value
