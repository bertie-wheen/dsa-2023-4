"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Deques

Linked Deques Solution
"""

from collections.abc import Iterator

from lib.base import Base
from lib.type_vars import Item

from lab2.core.doubly_linked_list import DoublyLinkedList


class LinkedDeque(Base[Item]):
    """
    A deque implemented using a doubly-linked list.

    Space: O(self.get_length())
    """

    _linked_list: DoublyLinkedList[Item]

    def __init__(self) -> None:
        """
        Initialize this deque.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._linked_list = DoublyLinkedList()

    @staticmethod
    def build(items: Iterator[Item]) -> "LinkedDeque[Item]":
        """
        Build a linked deque containing the given items.

        The deque should behave like that iterable,
        in that it yields the items in the same order.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a linked deque of those items
        """
        deque = LinkedDeque()
        deque._linked_list = DoublyLinkedList.build(items)
        return deque

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
        return self._linked_list.contains(item)

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
        return self._linked_list.is_empty()

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
        return self._linked_list.get_length()

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
        return self._linked_list.get_first()

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
        return self._linked_list.get_last()

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
        self._linked_list.insert_first(new_first_item)

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
        self._linked_list.insert_last(new_last_item)

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
        return self._linked_list.remove_first()

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
        return self._linked_list.remove_last()

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
        return self._linked_list.iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this deque.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: an iterator over the deque's items, back-to-front
        """
        return self._linked_list.reverse_iterator()
