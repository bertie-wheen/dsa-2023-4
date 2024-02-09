"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Linked Stacks Exercise
"""

from collections.abc import Iterator

from lib.base import Base
from lib.type_vars import Item

from lab2.core.singly_linked_list import SinglyLinkedList


class LinkedStack(Base[Item]):
    """
    A stack implemented using a singly-linked list.

    Space: O(self.get_length())
    """

    _linked_list: SinglyLinkedList[Item]

    def __init__(self) -> None:
        """
        Initialize this stack.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._linked_list = SinglyLinkedList()

    @staticmethod
    def build(items: Iterator[Item]) -> "LinkedStack[Item]":
        """
        Build a linked stack containing the given items.

        The stack should behave like that iterable,
        in that it yields the items in the same order.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a linked stack of those items
        """
        stack = LinkedStack()
        stack._linked_list = SinglyLinkedList.build(items)
        return stack

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
        return self._linked_list.contains(item)

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
        return self._linked_list.is_empty()

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
        return self._linked_list.get_length()

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
        raise NotImplementedError

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
        raise NotImplementedError

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
        raise NotImplementedError

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
        return self._linked_list.iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this stack.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: an iterator over the stack's items, bottom-to-top
        """
        return self._linked_list.reverse_iterator()
