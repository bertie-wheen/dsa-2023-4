"""
Data Structures & Algorithms

Lab 2: Lists
"""


from collections.abc import Iterator
from typing import Optional

from lib.base import Base
from lib.type_vars import Item


class Array(Base[Item]):
    """
    A basic array type, supporting O(1) random access.

    Space: O(self.get_length())
    """

    _items: list[Optional[Item]]

    def __init__(self, length: int = 0) -> None:
        """
        Initialize this array.

        If ``length > 0``, the items will be initially ``None``.

        +--------+-----------+
        | Time:  | O(length) |
        +--------+-----------+
        | Space: | O(length) |
        +--------+-----------+

        :parameter length: the length of the array
        """
        self._items = [None] * length

    @staticmethod
    def build(items: Iterator[Optional[Item]]) -> "Array[Item]":
        """
        Build an array containing the given items.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: an array of those items
        """
        items_list = list(items)
        length = len(items_list)
        array = Array(length)
        for index in range(length):
            array.set_at(index, items_list[index])
        return array

    def get_length(self) -> int:
        """
        Get the number of items in this array.

        ``None``s are counted as items.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return len(self._items)

    def get_at(self, index: int) -> Optional[Item]:
        """
        Get the item at the given index in this array.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the index
        :returns: the item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        if not 0 <= index < self.get_length():
            raise IndexError
        return self._items[index]

    def set_at(self, index: int, new_item: Optional[Item]) -> None:
        """
        Set the item at the given index in this ar.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the item's index
        :parameter new_item: the new item to overwrite the old item at the index with
        :raises IndexError: unless ``0 <= index < length``
        """
        if not 0 <= index < self.get_length():
            raise IndexError
        self._items[index] = new_item

    def iterator(self) -> Iterator[Optional[Item]]:
        """
        Get a forward iterator over the items in this array.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the array's items, first-to-last
        """
        for index in range(self.get_length()):
            yield self.get_at(index)

    def reverse_iterator(self) -> Iterator[Optional[Item]]:
        """
        Get a reverse iterator over the items in this array.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the array's items, last-to-first
        """
        for index in reversed(range(self.get_length())):
            yield self.get_at(index)
