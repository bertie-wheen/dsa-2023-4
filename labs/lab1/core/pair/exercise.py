"""
Data Structures & Algorithms

Lab 1: Getting Ready

Pairs Exercise
"""


from collections.abc import Iterator
from typing import Generic
from lib.type_vars import Item


class Pair(Generic[Item]):
    """
    A pair of items.

    Space: O(1)
    """

    _first: Item
    _second: Item

    def __init__(self, first: Item, second: Item) -> None:
        """
        Initialize this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter first: the first item
        :parameter second: the second item
        """
        self._first = first
        self._second = second

    @staticmethod
    def build(items: Iterator[Item]) -> "Pair[Item]":
        """
        Build a pair containing the given items.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter items: an iterator of initial items
        :returns: a pair containing those items
        :raises ValueError: if the iterator contains more or less than 2 items
        """
        length = 0
        for item in items:
            if length == 0:
                first = item
            elif length == 1:
                second = item
            else:
                raise ValueError
            length += 1
        if length < 2:
            raise ValueError
        # noinspection PyUnboundLocalVariable
        return Pair(first, second)

    def get_first(self) -> Item:
        """
        Get the first item of this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the first item
        """
        return self._first

    def get_second(self) -> Item:
        """
        Get the second item of this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the second item
        """
        raise NotImplementedError

    def set_first(self, new_first: Item) -> None:
        """
        Set the first item of this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_first: the new item to overwrite the first with
        """
        self._first = new_first

    def set_second(self, new_second: Item) -> None:
        """
        Set the second item of this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_second: the new item to overwrite the second with
        """
        self._second = new_second

    def iterator(self) -> Iterator[Item]:
        """
        Get a forward iterator over the items in this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: an iterator over the pair's items, first-then-second
        """
        yield self._first
        yield self._second

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse iterator over the items in this pair.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: an iterator over the pair's items, second-then-first
        """
        raise NotImplementedError
