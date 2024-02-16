"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Merge Sort Exercise
"""

from lib.array import Array
from lib.type_vars import Item


def merge(array_a: Array[Item], array_b: Array[Item]) -> Array[Item]:
    """
    Merge the two sorted arrays into a single sorted array.

    +--------+------------------------------------------------+
    | Time:  | O(array_a.get_length() + array_b.get_length()) |
    +--------+------------------------------------------------+
    | Space: | O(array_a.get_length() + array_b.get_length()) |
    +--------+------------------------------------------------+

    :parameter array_a: a sorted array
    :parameter array_b: another sorted array
    :returns: a sorted array containing all the items in both the given arrays
    """
    raise NotImplementedError


def merge_sort(array: Array[Item]) -> None:
    """
    Sort the given array in increasing order using merge sort.

    +--------+--------------------------------------------------+
    | Time:  | O(array.get_length() * log2(array.get_length())) |
    +--------+--------------------------------------------------+
    | Space: | O(array.get_length())                            |
    +--------+--------------------------------------------------+

    :parameter array: the array to sort
    """
    raise NotImplementedError
