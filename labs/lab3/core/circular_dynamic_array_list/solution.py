"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Circular Dynamic Array Lists Solution
"""

from collections.abc import Iterator
from typing import Optional

from lib.array import Array
from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Item


class CircularDynamicArrayList(Base[Item]):
    """
    A circular, predominantly dynamic array list.

    Space: O(self.get_capacity())
    """

    _array: Array[Item]
    _first_index: int
    _length: int

    def __init__(self, capacity: int = 0) -> None:
        """
        Initialize this circular dynamic array list.

        +--------+-------------+
        | Time:  | O(capacity) |
        +--------+-------------+
        | Space: | O(capacity) |
        +--------+-------------+

        :parameter capacity: the array's initial capacity (default ``0``)
        """
        self._first_index = 0
        self._length = 0
        self._array = Array(capacity)

    @staticmethod
    def build(items: Iterator[Item], capacity: Optional[int] = None) -> "CircularDynamicArrayList[Item]":
        """
        Build a circular dynamic array list containing the given items.

        If ``capacity`` is not given, it is sized to just fit the initial items.

        +--------+--------------------------------+
        | Time:  | O(build(items).get_capacity()) |
        +--------+--------------------------------+
        | Space: | O(build(items).get_capacity()) |
        +--------+--------------------------------+

        :parameter items: an iterator of initial items
        :parameter capacity: optionally, the initial capacity (default ``None``)
        :returns: a dynamic array list of those items
        :raises ValueError: if ``capacity`` is less than the number of items
        """
        array = Array.build(items)
        length = array.get_length()
        if capacity is None:
            capacity = length
        elif capacity < length:
            raise ValueError
        list = CircularDynamicArrayList(capacity=capacity)
        list._length = length
        for index in range(length):
            item = array.get_at(index)
            list.set_at(index, item)
        return list

    def resize(self, new_capacity: int) -> None:
        """
        Set the capacity of this dynamic array list.

        Reallocate the backing array unless the capacity is unchanged.

        +--------+---------------------------------------------------------------------------------------+
        | Time:  | O(min(self.get_length(), new_capacity) if self.get_capacity() != new_capacity else 1) |
        +--------+---------------------------------------------------------------------------------------+
        | Space: | O(new_capacity)                                                                       |
        +--------+---------------------------------------------------------------------------------------+

        :parameter new_capacity: the new capacity
        :raises ValueError: if the new capacity is less than the length
        """
        old_capacity = self.get_capacity()
        if old_capacity == new_capacity:
            return
        if new_capacity < self._length:
            raise ValueError
        old_array = self._array
        new_array = Array(length=new_capacity)
        for new_array_index in range(self._length):
            old_array_index = self._get_array_index(new_array_index)
            item = old_array.get_at(old_array_index)
            new_array.set_at(new_array_index, item)
        self._array = new_array
        self._first_index = 0

    def _grow_if_should(self) -> None:
        """
        If the capacity should be increased,
        increase it, else do nothing.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+
        """
        capacity = self.get_capacity()
        if self._length == capacity:
            if capacity == 0:
                self.resize(1)
            else:
                self.resize(2 * capacity)

    def _shrink_if_should(self) -> None:
        """
        If the capacity should be decreased,
        decrease it, else do nothing.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+
        """
        if self._length <= self.get_capacity() // 4:
            self.resize(self.get_capacity() // 2)

    def shrink_to_fit(self) -> None:
        """
        Set the capacity of this dynamic array list to its length.

        Make there be no unused capacity.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+
        """
        self.resize(self._length)

    def contains(self, item: Item) -> bool:
        """
        Check if this list contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: ``True`` if the item is in the list, else ``False``
        """
        for contained_item in self.iterator():
            if item == contained_item:
                return True
        return False

    def is_empty(self) -> bool:
        """
        Check if this list is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the list is empty, else ``False``
        """
        return self._length == 0

    def get_length(self) -> int:
        """
        Get the number of items in this list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._length

    def get_capacity(self) -> int:
        """
        Get the maximum number of items this dynamic array list
        can hold without reallocating to increase its capacity.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the capacity
        """
        return self._array.get_length()

    def _get_array_index(self, index: int) -> int:
        capacity = self.get_capacity()
        return (self._first_index + index) % capacity

    def get_first(self) -> Item:
        """
        Get the first item in this list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the first item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        return self._array.get_at(self._first_index)

    def get_last(self) -> Item:
        """
        Get the last item in this list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the last item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        last_index = self._get_array_index(self._length - 1)
        return self._array.get_at(last_index)

    def get_at(self, index: int) -> Item:
        """
        Get the item at the given index in this list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the index
        :returns: the item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        if not 0 <= index < self._length:
            raise IndexError
        index = self._get_array_index(index)
        return self._array.get_at(index)

    def _increment_first_index(self) -> None:
        old_first_index = self._first_index
        if old_first_index == self.get_capacity() - 1:
            new_first_index = 0
        else:
            new_first_index = old_first_index + 1
        self._first_index = new_first_index

    def _decrement_first_index(self) -> None:
        old_first_index = self._first_index
        if old_first_index == 0:
            new_first_index = self.get_capacity() - 1
        else:
            new_first_index = old_first_index - 1
        self._first_index = new_first_index

    def set_first(self, new_first_item: Item) -> None:
        """
        Set the first item in this list to be the one given.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_first_item: the new item to overwrite the old first item with
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        self._array.set_at(self._first_index, new_first_item)

    def set_last(self, new_last_item: Item) -> None:
        """
        Set the last item in this list to be the one given.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_last_item: the new item to overwrite the old last item with
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        last_index = self._get_array_index(self._length - 1)
        self._array.set_at(last_index, new_last_item)

    def set_at(self, index: int, new_item: Item) -> None:
        """
        Set the item at the given index in this list to be the one given.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the item's index
        :parameter new_item: the new item to overwrite the old item at the index with
        :raises IndexError: unless ``0 <= index < length``
        """
        index = self._get_array_index(index)
        self._array.set_at(index, new_item)

    def insert_first(self, new_first_item: Item) -> None:
        """
        Insert the given item into this list as the first item.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_first_item: the new first item
        """
        self._grow_if_should()
        if not self.is_empty():
            self._decrement_first_index()
        self._length += 1
        self.set_first(new_first_item)

    def insert_last(self, new_last_item: Item) -> None:
        """
        Insert the given item into this list as the last item.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_last_item: the new last item
        """
        self._grow_if_should()
        self._length += 1
        self.set_last(new_last_item)

    def insert_at(self, index: int, new_item: Item) -> None:
        """
        Insert the given item into this list at the given index.

        +--------+----------------------------------------------------+
        | Time:  | O(min(index, self.get_length() - index)) amortized |
        +--------+----------------------------------------------------+
        | Space: | O(self.get_length())                               |
        +--------+----------------------------------------------------+

        :parameter index: the index that the item should be at
        :parameter new_item: the item to be inserted
        :raises IndexError: unless ``0 <= index <= length``
        """
        old_length = self._length
        if not 0 <= index <= old_length:
            raise IndexError
        self._grow_if_should()
        self._length += 1
        if index < old_length // 2:
            self._decrement_first_index()
            for i in range(index):
                item = self.get_at(i + 1)
                self.set_at(i, item)
        else:
            for i in reversed(range(index, old_length)):
                item = self.get_at(i)
                self.set_at(i + 1, item)
        self.set_at(index, new_item)

    def remove_first(self) -> Item:
        """
        Remove the first item from this list and return it.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old first item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        old_first_item = self.get_first()
        self._increment_first_index()
        self._shrink_if_should()
        self._length -= 1
        return old_first_item

    def remove_last(self) -> Item:
        """
        Remove the last item from this list and return it.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old last item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        old_last_item = self.get_last()
        self._length -= 1
        self._shrink_if_should()
        return old_last_item

    def remove_at(self, index: int) -> Item:
        """
        Remove the item at the given index from this list and return it.

        +--------+----------------------------------------------------+
        | Time:  | O(min(index, self.get_length() - index)) amortized |
        +--------+----------------------------------------------------+
        | Space: | O(self.get_length())                               |
        +--------+----------------------------------------------------+

        :parameter index: the index of the item to be removed
        :returns: the old item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        old_length = self._length
        if not 0 <= index < old_length:
            raise IndexError
        removed_item = self.get_at(index)
        if index < old_length // 2:
            for i in reversed(range(index)):
                item = self.get_at(i)
                self.set_at(i + 1, item)
            self._increment_first_index()
        else:
            new_length = old_length - 1
            for i in range(index, new_length):
                item = self.get_at(i + 1)
                self.set_at(i, item)
        self._length -= 1
        self._shrink_if_should()
        return removed_item

    def iterator(self) -> Iterator[Item]:
        """
        Get a forward iterator over the items in this list.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the list's items, first-to-last
        """
        for index in range(self._length):
            yield self.get_at(index)

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this list.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the list's items, last-to-first
        """
        for index in reversed(range(self._length)):
            yield self.get_at(index)
