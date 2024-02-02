"""
Data Structures & Algorithms

Lab 2: Lists

Static Array Lists Exercise
"""


from collections.abc import Iterator

from lib.array import Array
from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Item


class StaticArrayList(Base[Item]):
    """
    A predominantly static array list.

    Space: O(self.get_length())
    """

    _array: Array[Item]

    def __init__(self) -> None:
        """
        Initialize this static array list.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._array = Array(0)

    @staticmethod
    def build(items: Iterator[Item]) -> "StaticArrayList[Item]":
        """
        Build a static array list containing the given items.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a static array list of those items
        """
        list = StaticArrayList()
        list._array = Array.build(items)
        return list

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
        return self.get_length() == 0

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
        return self._array.get_length()

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
        return self.get_at(0)

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
        return self._array.get_at(index)

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
        return self.get_at(self.get_length() - 1)

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
        self.set_at(0, new_first_item)

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
        self._array.set_at(index, new_item)

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
        self.set_at(self.get_length() - 1, new_last_item)

    def insert_first(self, new_first_item: Item) -> None:
        """
        Insert the given item into this list as the first item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :parameter new_first_item: the new first item
        """
        self.insert_at(0, new_first_item)

    def insert_at(self, index: int, new_item: Item) -> None:
        """
        Insert the given item into this list at the given index.

        +--------+----------------------------------------+
        | Time:  | O(self.get_length() - index) amortized |
        +--------+----------------------------------------+
        | Space: | O(self.get_length())                   |
        +--------+----------------------------------------+

        :parameter index: the index that the item should be at
        :parameter new_item: the item to be inserted
        :raises IndexError: unless ``0 <= index <= length``
        """
        raise NotImplementedError

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
        self.insert_at(self.get_length(), new_last_item)

    def remove_first(self) -> Item:
        """
        Remove the first item from this list and return it.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: the old first item
        :raises EmptyCollectionError: if the list is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        return self.remove_at(0)

    def remove_at(self, index: int) -> Item:
        """
        Remove the item at the given index from this list and return it.

        +--------+----------------------------------------+
        | Time:  | O(self.get_length() - index) amortized |
        +--------+----------------------------------------+
        | Space: | O(self.get_length())                   |
        +--------+----------------------------------------+

        :parameter index: the index of the item to be removed
        :returns: the old item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        raise NotImplementedError

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
        return self.remove_at(self.get_length() - 1)

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
        for index in range(self.get_length()):
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
        for index in reversed(range(self.get_length())):
            yield self.get_at(index)
