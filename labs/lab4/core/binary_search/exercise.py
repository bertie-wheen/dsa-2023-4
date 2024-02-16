"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Binary Search Exercise
"""

from typing import Optional

from lib.array import Array
from lib.type_vars import Item


def _binary_search_between(array: Array[Item], item: Item, lower_index: int, upper_index: int) -> Optional[int]:
    """
    Search the given array for the given item using binary search.

    Only search indices in the given range.
    If the indices do not denote a valid range, return ``None``.

    +--------+------------------------------------+
    | Time:  | O(log2(upper_index - lower_index)) |
    +--------+------------------------------------+
    | Space: | O(1)                               |
    +--------+------------------------------------+

    :parameter array: the array to search
    :parameter item: the item to search for
    :parameter lower_index: the lower bound of indices to check
    :parameter upper_index: the upper bound of indices to check
    :returns: the index of the item if it's in the given range of the array, else ``None``
    """
    raise NotImplementedError


def binary_search(array: Array[Item], item: Item) -> Optional[int]:
    """
    Search the given array for the given item using binary search.

    +--------+-----------------------------+
    | Time:  | O(log2(array.get_length())) |
    +--------+-----------------------------+
    | Space: | O(1)                        |
    +--------+-----------------------------+

    :parameter array: the array to search
    :parameter item: the item to search for
    :returns: the index of the item if it's in the array, else ``None``
    """
    return _binary_search_between(array, item, 0, array.get_length() - 1)
