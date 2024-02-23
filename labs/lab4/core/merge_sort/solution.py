"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Merge Sort Solution
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
    length_a = array_a.get_length()
    length_b = array_b.get_length()
    length = length_a + length_b
    array = Array(length)
    index_a = 0
    index_b = 0
    for index in range(length):
        if index_b >= length_b or (index_a < length_a and array_a.get_at(index_a) <= array_b.get_at(index_b)):
            item = array_a.get_at(index_a)
            index_a += 1
        else:
            item = array_b.get_at(index_b)
            index_b += 1
        array.set_at(index, item)
    return array


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
    length = array.get_length()
    if length <= 1:
        return
    pivot_index = length // 2
    left_subarray = Array(pivot_index)
    right_subarray = Array(length - pivot_index)
    for index in range(pivot_index):
        left_subarray.set_at(index, array.get_at(index))
    for index in range(pivot_index, length):
        right_subarray.set_at(index - pivot_index, array.get_at(index))
    merge_sort(left_subarray)
    merge_sort(right_subarray)
    merged_array = merge(left_subarray, right_subarray)
    for index in range(length):
        array.set_at(index, merged_array.get_at(index))
