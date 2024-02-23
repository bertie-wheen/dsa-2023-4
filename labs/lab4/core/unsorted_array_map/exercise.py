"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Unsorted Array Maps Exercise
"""

from collections.abc import Iterator

from lib.base import Base
from lib.type_vars import Key, Value

from lab2.core.static_array_list import StaticArrayList


class UnsortedArrayMap(Base[Key, Value]):
    _array_list: StaticArrayList[tuple[Key, Value]]

    def __init__(self) -> None:
        """
        Initialize this unsorted array map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._array_list = StaticArrayList()

    @staticmethod
    def build(mappings: Iterator[tuple[Key, Value]]) -> "UnsortedArrayMap[Key, Value]":
        """
        Build an unsorted array map containing the given key/value mappings.

        +--------+---------------------------------+
        | Time:  | O(build(mappings).get_length()) |
        +--------+---------------------------------+
        | Space: | O(build(mappings).get_length()) |
        +--------+---------------------------------+

        :parameter items: an iterator of initial mappings
        :returns: an unsorted array map with those mappings
        """
        map = UnsortedArrayMap()
        for key, value in mappings:
            map.insert(key, value)
        return map

    def contains(self, key: Key) -> bool:
        """
        Check if this map contains the given key.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key to search for
        :returns: ``True`` if the key is in the map, else ``False``
        """
        for contained_key in self.keys_iterator():
            if key == contained_key:
                return True
        return False

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
        return self._array_list.is_empty()

    def get_length(self) -> int:
        """
        Get the number of mappings in this map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+


        :returns: the length
        """
        return self._array_list.get_length()

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this map.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key is not in the map
        """
        for contained_key, contained_value in self.iterator():
            if key == contained_key:
                return contained_value
        raise KeyError

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this map.
        If the key is already in the map, set it to map to the new value.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        raise NotImplementedError

    def remove(self, key: Key) -> Value:
        """
        Remove the mapping for the given key from this map, and return the value that it mapped to.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key was not in the map
        """
        raise NotImplementedError

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        """
        Get an iterator over the key/value pairs in this map.
        The iteration order is unspecified.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the map's items
        """
        return self._array_list.iterator()

    def keys_iterator(self) -> Iterator[Key]:
        """
        Get an iterator over the keys in this map.
        The iteration order is unspecified.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the map's keys
        """
        for key, value in self.iterator():
            yield key

    def values_iterator(self) -> Iterator[Value]:
        """
        Get an iterator over the values in this map.
        The iteration order is unspecified.
        If the same value is mapped to by multiple keys, it will occur multiple times.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the map's values
        """
        for key, value in self.iterator():
            yield value
