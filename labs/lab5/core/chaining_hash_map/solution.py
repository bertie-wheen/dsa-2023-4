"""
Data Structures & Algorithms

Lab 5: Hash Maps

Chaining Hash Maps Solution
"""

from collections.abc import Iterator

from lib.array import Array
from lib.base import Base
from lib.type_vars import Key, Value

from lab2.core.doubly_linked_list import DoublyLinkedList
from lab5.core.hash_function import HashFunction


class ChainingHashMap(Base[Key, Value]):
    """
    A chaining hash map.

    Space: O(self.get_chain_count() + self.get_length())
    """

    _chain_array: Array[DoublyLinkedList[tuple[Key, Value]]]
    _hash_function: HashFunction
    _length: int
    _max_load_factor: float

    def __init__(self, max_load_factor: float = 2.0) -> None:
        """
        Initialize this chaining hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter max_load_factor: the proportion of items to chains at which the table is considered overly full
        :raises ValueError: if ``max_load_factor <= 1/2``
        """
        if max_load_factor <= 1 / 2:
            raise ValueError
        self._chain_array = Array(1)
        self._chain_array.set_at(0, DoublyLinkedList())
        self._hash_function = HashFunction(1)
        self._length = 0
        self._max_load_factor = max_load_factor

    @staticmethod
    def build(items: Iterator[tuple[Key, Value]], max_load_factor: float = 2.0) -> "ChainingHashMap[Key, Value]":
        """
        Build a chaining hash map containing the given items.

        +--------+------------------------------------------------------------------------+
        | Time:  | O(build(items).get_chain_count() + build(items).get_length()) expected |
        +--------+------------------------------------------------------------------------+
        | Space: | O(build(items).get_chain_count() + build(items).get_length())          |
        +--------+------------------------------------------------------------------------+

        :parameter items: an iterator of initial items
        :parameter max_load_factor: the proportion of items to chains at which the table is considered overly full
        :returns: a chaining hash map of those items
        :raises ValueError: if ``max_load_factor <= 1/2``
        """
        map = ChainingHashMap(max_load_factor=max_load_factor)
        for key, value in items:
            map.insert(key, value)
        return map

    def get_chain_count(self) -> int:
        """
        Get the number of chains in this hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the chain count
        """
        return self._chain_array.get_length()

    def get_min_load_factor(self) -> float:
        """
        Get the minimum load factor of this hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the minimum load factor
        """
        return self._max_load_factor / 4

    def get_max_load_factor(self) -> float:
        """
        Get the maximum load factor of this hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the maximum load factor
        """
        return self._max_load_factor

    def get_load_factor(self) -> float:
        """
        Get the load factor of this hash map.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the current load factor
        """
        return self._length / self.get_chain_count()

    def _resize(self, new_chain_count: int) -> None:
        """
        Change this hash map's number of chains, redistribute the mappings, and choose a new random hash function.

        +--------+-----------------------------------------------------------------+
        | Time:  | O(self.get_chain_count() + new_chain_count + self.get_length()) |
        +--------+-----------------------------------------------------------------+
        | Space: | O(new_chain_count + self.get_length())                          |
        +--------+-----------------------------------------------------------------+

        :parameter new_chain_count: the new number of chains
        :raises ValueError: if ``new_chain_count < 1``
        """
        if new_chain_count < 1:
            raise ValueError
        items = Array.build(self.iterator())
        self._chain_array = Array(new_chain_count)
        for index in range(self._chain_array.get_length()):
            self._chain_array.set_at(index, DoublyLinkedList())
        self._hash_function = HashFunction(new_chain_count)
        self._length = 0
        for key, value in items.iterator():
            self.insert(key, value)

    def _get_chain(self, key: Key) -> DoublyLinkedList[tuple[Key, Value]]:
        """
        Get the chain that would hold a mapping with the given key.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter key: the key
        :returns: the appropriate chain
        """
        return self._chain_array.get_at(self._hash_function.hash(key))

    def contains(self, key: Key) -> bool:
        """
        Check if this map contains the given key.

        +--------+------------------------------------+
        | Time:  | O(self.get_chain_count()) expected |
        +--------+------------------------------------+
        | Space: | O(1)                               |
        +--------+------------------------------------+

        :returns: ``True`` if the key is in the map, else ``False``
        """
        chain = self._get_chain(key)
        for item_key, item_value in chain.iterator():
            if key == item_key:
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
        return self._length == 0

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

        +--------+------------------------------------+
        | Time:  | O(self.get_chain_count()) expected |
        +--------+------------------------------------+
        | Space: | O(1)                               |
        +--------+------------------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key is not in the map
        """
        chain = self._get_chain(key)
        for item_key, item_value in chain.iterator():
            if key == item_key:
                return item_value
        raise KeyError

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this map.
        If the key is already in the map, set it to map to the new value.

        +--------+----------------------------------------------+
        | Time:  | O(self.get_chain_count()) amortised expected |
        +--------+----------------------------------------------+
        | Space: | O(1)                                         |
        +--------+----------------------------------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        new_item = key, new_value
        chain = self._get_chain(key)
        for node in chain.nodes_iterator():
            item_key, item_value = node.get()
            if key == item_key:
                node.set(new_item)
                return
        self._length += 1
        if self.get_load_factor() > self._max_load_factor:
            old_chain_count = self.get_chain_count()
            new_chain_count = old_chain_count * 2
            self._resize(new_chain_count)
            self.insert(key, new_value)
        else:
            chain.insert_last(new_item)

    def remove(self, key: Key) -> Value:
        """
        Remove the mapping for the given key from this map, and return the value that it mapped to.

        +--------+----------------------------------------------+
        | Time:  | O(self.get_chain_count()) amortised expected |
        +--------+----------------------------------------------+
        | Space: | O(1)                                         |
        +--------+----------------------------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key was not in the map
        """
        chain = self._get_chain(key)
        found = False
        for node in chain.nodes_iterator():
            item_key, item_value = node.get()
            if key == item_key:
                node.remove()
                removed_value = item_value
                found = True
                break
        if not found:
            raise KeyError
        self._length -= 1
        if self.get_load_factor() < self.get_min_load_factor():
            old_chain_count = self.get_chain_count()
            new_chain_count = old_chain_count // 2
            if new_chain_count < 1:
                new_chain_count = 1
            self._resize(new_chain_count)
        return removed_value

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        """
        Get an iterator over the key/value pairs in this map.
        The iteration order is unspecified.

        +--------+-----------------------------------------------+
        | Time:  | O(self.get_chain_count() + self.get_length()) |
        +--------+-----------------------------------------------+
        | Space: | O(1)                                          |
        +--------+-----------------------------------------------+

        :returns: an iterator over the map's items
        """
        for chain in self._chain_array.iterator():
            for item in chain.iterator():
                yield item

    def keys_iterator(self) -> Iterator[Key]:
        """
        Get an iterator over the keys in this map.
        The iteration order is unspecified.

        +--------+-----------------------------------------------+
        | Time:  | O(self.get_chain_count() + self.get_length()) |
        +--------+-----------------------------------------------+
        | Space: | O(1)                                          |
        +--------+-----------------------------------------------+

        :returns: an iterator over the map's keys
        """
        for key, value in self.iterator():
            yield key

    def values_iterator(self) -> Iterator[Value]:
        """
        Get an iterator over the values in this map.
        The iteration order is unspecified.
        If the same value is mapped to by multiple keys, it will occur multiple times.

        +--------+-----------------------------------------------+
        | Time:  | O(self.get_chain_count() + self.get_length()) |
        +--------+-----------------------------------------------+
        | Space: | O(1)                                          |
        +--------+-----------------------------------------------+

        :returns: an iterator over the map's values
        """
        for key, value in self.iterator():
            yield value
