"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Array Stacks Solution
"""

from collections.abc import Iterator
from typing import Optional

from lib.array import Array
from lib.base import Base
from lib.type_vars import Item

from lab3.core.dynamic_array_list import DynamicArrayList


class ArrayStack(Base[Item]):
    """
    A stack implemented using a dynamic array list.

    Space: O(self.get_capacity())
    """

    _array_list: DynamicArrayList[Item]

    def __init__(self, capacity: int = 0):
        """
        Initialize this stack.

        +--------+-------------+
        | Time:  | O(capacity) |
        +--------+-------------+
        | Space: | O(capacity) |
        +--------+-------------+
        """
        self._array_list = DynamicArrayList(capacity=capacity)

    @staticmethod
    def build(items: Iterator[Item], capacity: Optional[int] = None) -> "ArrayStack[Item]":
        """
        Build a linked stack containing the given items.

        The stack should behave like that iterable,
        in that it yields the items in the same order.

        If ``capacity`` is not given, it is sized to just fit the initial items.

        +--------+--------------------------------+
        | Time:  | O(build(items).get_capacity()) |
        +--------+--------------------------------+
        | Space: | O(build(items).get_capacity()) |
        +--------+--------------------------------+

        :parameter items: an iterator of initial items
        :parameter capacity: optionally, the initial capacity (default ``None``)
        :returns: a linked stack of those items
        :raises ValueError: if ``capacity`` is less than the number of items
        """
        stack = ArrayStack()
        temporary_array = Array.build(items)
        stack._array_list = DynamicArrayList.build(temporary_array.reverse_iterator(), capacity=capacity)
        return stack

    def get_capacity(self) -> int:
        """
        Get the maximum number of items this array stack
        can hold without reallocating to increase its capacity.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the capacity
        """
        return self._array_list.get_capacity()

    def contains(self, item: Item) -> bool:
        """
        Check if this stack contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: ``True`` if the item is in the stack, else ``False``
        """
        return self._array_list.contains(item)

    def is_empty(self) -> bool:
        """
        Check if this stack is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the stack is empty, else ``False``
        """
        return self._array_list.is_empty()

    def get_length(self) -> int:
        """
        Get the number of items in this stack.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._array_list.get_length()

    def push(self, new_top_item: Item) -> None:
        """
        Push (add) the given item onto the top of the stack.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_top_item: the item to push
        """
        self._array_list.insert_last(new_top_item)

    def peek(self) -> Item:
        """
        Return the item on the top of the stack.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the top item
        :raises EmptyCollectionError: if the stack is empty
        """
        return self._array_list.get_last()

    def pop(self) -> Item:
        """
        Pop (remove and return) the item from the top of the stack.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the old top item
        :raises EmptyCollectionError: if the stack is empty
        """
        return self._array_list.remove_last()

    def iterator(self) -> Iterator[Item]:
        """
        Get a forward iterator over the items in this stack.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the stack's items, top-to-bottom
        """
        return self._array_list.reverse_iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this stack.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the stack's items, bottom-to-top
        """
        return self._array_list.iterator()
