"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Linked Queues Solution
"""

from collections.abc import Iterator

from lib.base import Base
from lib.type_vars import Item

from lab2.core.singly_linked_list import SinglyLinkedList


class LinkedQueue(Base[Item]):
    """
    A queue implemented using a singly-linked list.

    Space: O(self.get_length())
    """

    _linked_list: SinglyLinkedList[Item]

    def __init__(self) -> None:
        """
        Initialize this queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._linked_list = SinglyLinkedList()

    @staticmethod
    def build(items: Iterator[Item]) -> "LinkedQueue[Item]":
        """
        Build a linked queue containing the given items.

        The queue should behave like that iterable,
        in that it yields the items in the same order.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a linked queue of those items
        """
        queue = LinkedQueue()
        queue._linked_list = SinglyLinkedList.build(items)
        return queue

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
        return self._linked_list.contains(item)

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
        return self._linked_list.is_empty()

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
        return self._linked_list.get_length()

    def enqueue(self, new_back_item: Item) -> None:
        """
        Enqueue (add) the given item to the back of the queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_back_item: the item to enqueue
        """
        self._linked_list.insert_last(new_back_item)

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
        return self._linked_list.get_first()

    def dequeue(self) -> Item:
        """
        Dequeue (remove and return) the item from the front of the queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the old front item
        :raises EmptyCollectionError: if the queue is empty
        """
        return self._linked_list.remove_first()

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
        return self._linked_list.iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this queue.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: an iterator over the queue's items, back-to-front
        """
        return self._linked_list.reverse_iterator()
