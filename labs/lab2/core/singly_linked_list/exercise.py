"""
Data Structures & Algorithms

Lab 2: Lists

Singly-linked Lists Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Item


class SinglyLinkedList(Base[Item]):
    """
    A singly-linked list.

    Space: O(self.get_length())
    """

    _length: int
    _first_node: Optional["SinglyLinkedNode[Item]"]
    _last_node: Optional["SinglyLinkedNode[Item]"]

    def __init__(self) -> None:
        """
        Initialize this singly-linked list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._length = 0
        self._first_node = None
        self._last_node = None

    @staticmethod
    def build(items: Iterator[Item]) -> "SinglyLinkedList[Item]":
        """
        Build a singly-linked list containing the given items.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a singly-linked list of those items
        """
        singly_linked_list = SinglyLinkedList()
        for item in items:
            singly_linked_list.insert_last(item)
        return singly_linked_list

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

    def get_first_node(self) -> Optional["SinglyLinkedNode[Item]"]:
        """
        Get the first node in this list.

        If there is none, return ``None``.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the first node if there is one, else ``None``
        """
        return self._first_node

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
        return self._first_node.get()

    def get_node_at(self, index: int) -> "SinglyLinkedNode[Item]":
        """
        Get the node at the given index in this list.

        +--------+---------------------------------------------------+
        | Time:  | O(index if index != self.get_length() - 1 else 1) |
        +--------+---------------------------------------------------+
        | Space: | O(1)                                              |
        +--------+---------------------------------------------------+

        :parameter index: the index
        :returns: the item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        raise NotImplementedError

    def get_at(self, index: int) -> Item:
        """
        Get the item at the given index in this list.

        +--------+---------------------------------------------------+
        | Time:  | O(index if index != self.get_length() - 1 else 1) |
        +--------+---------------------------------------------------+
        | Space: | O(1)                                              |
        +--------+---------------------------------------------------+

        :parameter index: the index
        :returns: the item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        return self.get_node_at(index).get()

    def get_last_node(self) -> Optional["SinglyLinkedNode[Item]"]:
        """
        Get the last node in this list.

        If there is none, return ``None``.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the last node if there is one, else ``None``
        """
        return self._last_node

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
        return self._last_node.get()

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
        self._first_node.set(new_first_item)

    def set_at(self, index: int, new_item: Item) -> None:
        """
        Set the item at the given index in this list to be the one given.

        +--------+---------------------------------------------------+
        | Time:  | O(index if index != self.get_length() - 1 else 1) |
        +--------+---------------------------------------------------+
        | Space: | O(1)                                              |
        +--------+---------------------------------------------------+

        :parameter index: the item's index
        :parameter new_item: the new item to overwrite the old item at the index with
        :raises IndexError: unless ``0 <= index < length``
        """
        raise NotImplementedError

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
        self._last_node.set(new_last_item)

    def _make_singleton(self, new_sole_item: Item) -> None:
        """
        Make this a singleton list containing only the given item.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_sole_item: the new sole item
        """
        node = SinglyLinkedNode(self, new_sole_item)
        self._first_node = node
        self._last_node = node
        self._length = 1

    def insert_first(self, new_first_item: Item) -> None:
        """
        Insert the given item into this list as the first item.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_first_item: the new first item
        """
        if self.is_empty():
            self._make_singleton(new_first_item)
        else:
            self._first_node.insert_previous(new_first_item)

    def insert_at(self, index: int, new_item: Item) -> None:
        """
        Insert the given item into this list at the given index.

        +--------+-----------------------------------------------+
        | Time:  | O(index if index != self.get_length() else 1) |
        +--------+-----------------------------------------------+
        | Space: | O(1)                                          |
        +--------+-----------------------------------------------+

        :parameter index: the index that the item should be at
        :parameter new_item: the item to be inserted
        :raises IndexError: unless ``0 <= index <= length``
        """
        raise NotImplementedError

    def insert_last(self, new_last_item: Item) -> None:
        """
        Insert the given item into this list as the last item.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_last_item: the new last item
        """
        if self.is_empty():
            self._make_singleton(new_last_item)
        else:
            self._last_node.insert_next(new_last_item)

    def remove_first(self) -> Item:
        """
        Remove the first item from this list and return it.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the old first item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        return self._first_node.remove()

    def remove_at(self, index: int) -> Item:
        """
        Remove the item at the given index from this list and return it.

        +--------+----------+
        | Time:  | O(index) |
        +--------+----------+
        | Space: | O(1)     |
        +--------+----------+

        :parameter index: the index of the item to be removed
        :returns: the old item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        raise NotImplementedError

    def remove_last(self) -> Item:
        """
        Remove the last item from this list and return it.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the old last item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        return self._last_node.remove()

    def nodes_iterator(self) -> Iterator["SinglyLinkedNode[Item]"]:
        """
        Get a forward iterator over the nodes in this list.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the list's nodes, first-to-last
        """
        node = self._first_node
        while node is not None:
            yield node
            node = node.get_next_node()

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
        for node in self.nodes_iterator():
            yield node.get()

    def reverse_nodes_iterator(self) -> Iterator["SinglyLinkedNode[Item]"]:
        """
        Get a reverse iterator over the nodes in this list.

        Either:

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        Or:

        +--------+------------------------+
        | Time:  | O(self.get_length()^2) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: an iterator over the list's nodes, last-to-first
        """
        raise NotImplementedError

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this list.

        Either:

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        Or:

        +--------+------------------------+
        | Time:  | O(self.get_length()^2) |
        +--------+------------------------+
        | Space: | O(1)                   |
        +--------+------------------------+

        :returns: an iterator over the list's items, last-to-first
        """
        for node in self.reverse_nodes_iterator():
            yield node.get()


# noinspection PyProtectedMember
class SinglyLinkedNode(Base[Item]):
    """
    A node in a singly-linked list.

    Space: O(1)
    """

    _list: "SinglyLinkedList[Item]"
    _item: Item
    _next_node: Optional["SinglyLinkedNode[Item]"]

    def __init__(
        self,
        list: "SinglyLinkedList[Item]",
        item: Item,
        next_node: Optional["SinglyLinkedNode[Item]"] = None,
    ) -> None:
        """
        Initialize this node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter list: the singly-linked list containing this item
        :parameter item: the item this singly-linked node contains
        :parameter next_node: the next node, if there is one (default None)
        """
        self._list = list
        self._item = item
        self._next_node = next_node

    def has_previous(self) -> bool:
        """
        Check if there is a previous node before this node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there is a previous node, else ``False``
        """
        return not self.is_first()

    def has_next(self) -> bool:
        """
        Check if there is a next node after this node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there is a next node, else ``False``
        """
        return not self.is_last()

    def is_first(self) -> bool:
        """
        Check if this node is first in the list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the node is first, else ``False``
        """
        return self._list._first_node is self

    def is_last(self) -> bool:
        """
        Check if this node is last in the list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the node is last, else ``False``
        """
        return self._list._last_node is self

    def get_list(self) -> "SinglyLinkedList[Item]":
        """
        Get the list containing this node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the containing list
        """
        return self._list

    def get_index(self) -> int:
        """
        Get the index of this node within the list.

        +--------+---------------------+
        | Time:  | O(self.get_index()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the node's index
        :raises ValueError: if the node isn't in the list (because it's been removed)
        """
        index = 0
        for node in self.get_list().nodes_iterator():
            if node is self:
                return index
            index += 1
        raise ValueError

    def get_previous_node(self) -> Optional["SinglyLinkedNode[Item]"]:
        """
        Get the previous node before this node.

        If there is none, return ``None``.

        +--------+---------------------+
        | Time:  | O(self.get_index()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the previous node if there is one, else ``None``
        """
        if self.is_first():
            return None
        node = self._list._first_node
        while node._next_node is not self:
            node = node._next_node
        return node

    def get_previous(self) -> Item:
        """
        Get the previous item before this node's.

        +--------+---------------------+
        | Time:  | O(self.get_index()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the previous item
        :raises ValueError: if the node is first
        """
        if self.is_first():
            raise ValueError
        previous_node = self.get_previous_node()
        return previous_node.get()

    def get(self) -> Item:
        """
        Get the item contained in this node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the contained item
        """
        return self._item

    def get_next_node(self) -> Optional["SinglyLinkedNode[Item]"]:
        """
        Get the next node after this node.

        If there is none, return ``None``.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the next node if there is one, else ``None``
        """
        return self._next_node

    def get_next(self) -> Item:
        """
        Get the next item after this node's.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the next item
        :raises ValueError: if the node is last
        """
        if self.is_last():
            raise ValueError
        return self._next_node.get()

    def set(self, new_item: Item) -> None:
        """
        Set this node's item to be the one given.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_item: the new item this node should contain
        """
        self._item = new_item

    def insert_previous(self, new_previous_item: Item) -> None:
        """
        Insert the given item into the list as the previous node.

        +--------+---------------------+
        | Time:  | O(self.get_index()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :parameter new_previous_item: the item the new previous node should contain
        """
        raise NotImplementedError

    def insert_next(self, new_next_item: Item) -> None:
        """
        Insert the given item into the list as the next node.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_next_item: the item the new next node should contain
        """
        raise NotImplementedError

    def remove_previous(self) -> Item:
        """
        Remove the previous node from the list and return its item.

        +--------+----------------------+
        | Time:  | O(self.get_index()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the old previous item
        :raises ValueError: if there is no previous node
        """
        raise NotImplementedError

    def remove(self) -> Item:
        """
        Remove this node from the list and return its item.

        +--------+---------------------+
        | Time:  | O(self.get_index()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the item the node contained
        """
        raise NotImplementedError

    def remove_next(self) -> Item:
        """
        Remove the next node from the list and return its item.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the old next item
        :raises ValueError: if there is no next node
        """
        raise NotImplementedError
