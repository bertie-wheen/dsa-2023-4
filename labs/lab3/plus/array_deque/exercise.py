"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Deques

Array Deques Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.base import Base
from lib.type_vars import Item

from lab3.core.circular_dynamic_array_list import CircularDynamicArrayList


class ArrayDeque(Base[Item]):
    """
    A deque implemented using a circular dynamic array list.

    Space: O(self.get_capacity())
    """

    _circular_array_list: CircularDynamicArrayList[Item]

    def __init__(self, capacity: int = 0):
        """
        Initialize this deque.

        +--------+-------------+
        | Time:  | O(capacity) |
        +--------+-------------+
        | Space: | O(capacity) |
        +--------+-------------+
        """
        self._circular_array_list = CircularDynamicArrayList(capacity=capacity)

    @staticmethod
    def build(items: Iterator[Item], capacity: Optional[int] = None) -> "ArrayDeque[Item]":
        """
        Build an array deque containing the given items.

        The deque should behave like that iterable,
        in that it yields the items in the same order.

        If ``capacity`` is not given, it is sized to just fit the initial items.

        +--------+--------------------------------+
        | Time:  | O(build(items).get_capacity()) |
        +--------+--------------------------------+
        | Space: | O(build(items).get_capacity()) |
        +--------+--------------------------------+

        :parameter items: an iterator of initial items
        :parameter capacity: optionally, the initial capacity (default ``None``)
        :returns: an array deque of those items
        :raises ValueError: if ``capacity`` is less than the number of items
        """
        deque = ArrayDeque()
        deque._circular_array_list = CircularDynamicArrayList.build(items, capacity=capacity)
        return deque

    def get_capacity(self) -> int:
        """
        Get the maximum number of items this array deque
        can hold without reallocating to increase its capacity.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the capacity
        """
        return self._circular_array_list.get_capacity()

    def contains(self, item: Item) -> bool:
        """
        Check if this deque contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: ``True`` if the item is in the deque, else ``False``
        """
        return self._circular_array_list.contains(item)

    def is_empty(self) -> bool:
        """
        Check if this deque is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the deque is empty, else ``False``
        """
        return self._circular_array_list.is_empty()

    def get_length(self) -> int:
        """
        Get the number of items in this deque.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._circular_array_list.get_length()

    def get_first(self) -> Item:
        """
        Get the first item in this deque.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the first item
        :raises EmptyCollectionError: if the deque is empty
        """
        raise NotImplementedError

    def get_last(self) -> Item:
        """
        Get the last item in this deque.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the last item
        :raises EmptyCollectionError: if the deque is empty
        """
        raise NotImplementedError

    def insert_first(self, new_first_item: Item) -> None:
        """
        Insert the given item into this deque as the first item.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_first_item: the new first item
        """
        raise NotImplementedError

    def insert_last(self, new_last_item: Item) -> None:
        """
        Insert the given item into this deque as the last item.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_last_item: the new last item
        """
        raise NotImplementedError

    def remove_first(self) -> Item:
        """
        Remove the first item from this deque and return it.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old first item
        :raises EmptyCollectionError: if the deque is empty
        """
        raise NotImplementedError

    def remove_last(self) -> Item:
        """
        Remove the last item from this deque and return it.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old last item
        :raises EmptyCollectionError: if the deque is empty
        """
        raise NotImplementedError

    def iterator(self) -> Iterator[Item]:
        """
        Get a forward iterator over the items in this deque.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the deque's items, front-to-back
        """
        return self._circular_array_list.iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this deque.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the deque's items, back-to-front
        """
        return self._circular_array_list.reverse_iterator()
