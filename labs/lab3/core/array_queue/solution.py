"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Array Queues Solution
"""

from collections.abc import Iterator
from typing import Optional

from lib.base import Base
from lib.type_vars import Item

from lab3.core.circular_dynamic_array_list import CircularDynamicArrayList


class ArrayQueue(Base[Item]):
    """
    A queue implemented using a circular dynamic array list.

    Space: O(self.get_capacity())
    """

    _circular_array_list: CircularDynamicArrayList[Item]

    def __init__(self, capacity: int = 0):
        """
        Initialize this queue.

        +--------+-------------+
        | Time:  | O(capacity) |
        +--------+-------------+
        | Space: | O(capacity) |
        +--------+-------------+
        """
        self._circular_array_list = CircularDynamicArrayList(capacity=capacity)

    @staticmethod
    def build(items: Iterator[Item], capacity: Optional[int] = None) -> "ArrayQueue[Item]":
        """
        Build an array queue containing the given items.

        The queue should behave like that iterable,
        in that it yields the items in the same order.

        If ``capacity`` is not given, it is sized to just fit the initial items.

        +--------+--------------------------------+
        | Time:  | O(build(items).get_capacity()) |
        +--------+--------------------------------+
        | Space: | O(build(items).get_capacity()) |
        +--------+--------------------------------+

        :parameter items: an iterator of initial items
        :parameter capacity: optionally, the initial capacity (default ``None``)
        :returns: an array queue of those items
        :raises ValueError: if ``capacity`` is less than the number of items
        """
        queue = ArrayQueue()
        queue._circular_array_list = CircularDynamicArrayList.build(items, capacity=capacity)
        return queue

    def get_capacity(self) -> int:
        """
        Get the maximum number of items this array queue
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
        Check if this queue contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: ``True`` if the item is in the queue, else ``False``
        """
        return self._circular_array_list.contains(item)

    def is_empty(self) -> bool:
        """
        Check if this queue is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the queue is empty, else ``False``
        """
        return self._circular_array_list.is_empty()

    def get_length(self) -> int:
        """
        Get the number of items in this queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._circular_array_list.get_length()

    def enqueue(self, new_back_item: Item) -> None:
        """
        Enqueue (add) the given item to the back of the queue.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_back_item: the item to enqueue
        """
        self._circular_array_list.insert_last(new_back_item)

    def front(self) -> Item:
        """
        Return the item at the front of the queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the front item
        :raises EmptyCollectionError: if the queue is empty
        """
        return self._circular_array_list.get_first()

    def dequeue(self) -> Item:
        """
        Dequeue (remove and return) the item from the front of the queue.

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old front item
        :raises EmptyCollectionError: if the queue is empty
        """
        return self._circular_array_list.remove_first()

    def iterator(self) -> Iterator[Item]:
        """
        Get a forward iterator over the items in this queue.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the queue's items, front-to-back
        """
        return self._circular_array_list.iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this queue.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the queue's items, back-to-front
        """
        return self._circular_array_list.reverse_iterator()
