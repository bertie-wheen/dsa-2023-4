"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Selection Sort Solution
"""

from lib.array import Array
from lib.type_vars import Item


def _swap(array: Array[Item], index_a: int, index_b: int) -> None:
    """
    Swap the items at the given indices in the given array.

    :parameter array: the array
    :parameter index_a: the index that should instead contain the item at ``index_b``
    :parameter index_b: the index that should instead contain the item at ``index_a``
    :raises IndexError: if ``index_a`` or ``index_b`` are out of bounds
    """
    a = array.get_at(index_a)
    b = array.get_at(index_b)
    array.set_at(index_a, b)
    array.set_at(index_b, a)


def selection_sort(array: Array[Item]) -> None:
    """
    Sort the given array in increasing order using selection sort.

    +--------+---------------------------+
    | Time:  | O(array.get_length() ^ 2) |
    +--------+---------------------------+
    | Space: | O(1)                      |
    +--------+---------------------------+

    :parameter array: the array to sort
    """
    length = array.get_length()
    for lower_index in range(length - 1):
        min_index = lower_index
        for index in range(lower_index + 1, length):
            if array.get_at(index) < array.get_at(min_index):
                min_index = index
        _swap(array, lower_index, min_index)
