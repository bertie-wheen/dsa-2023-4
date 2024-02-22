from lib.array import Array
from lib.test import Test
from lib.type_vars import Item

from lab4.core.merge_sort.exercise import merge, merge_sort


@Test
def merge_then_get_length(
    array_a: Array[Item],
    array_b: Array[Item],
):
    sorted_array_a = Array.build(iter(sorted(array_a.iterator())))
    sorted_array_b = Array.build(iter(sorted(array_b.iterator())))
    array = merge(sorted_array_a, sorted_array_b)
    yield array_a.get_length() + array_b.get_length()
    yield array.get_length()


@Test
def merge_then_is_sorted(
    array_a: Array[Item],
    array_b: Array[Item],
):
    sorted_array_a = Array.build(iter(sorted(array_a.iterator())))
    sorted_array_b = Array.build(iter(sorted(array_b.iterator())))
    array = merge(sorted_array_a, sorted_array_b)
    sorted_array = Array.build(iter(sorted(array.iterator())))
    yield sorted_array
    yield array


@Test
def merge_then_contains_a(
    array_a: Array[Item],
    array_b: Array[Item],
):
    sorted_array_a = Array.build(iter(sorted(array_a.iterator())))
    sorted_array_b = Array.build(iter(sorted(array_b.iterator())))
    array = merge(sorted_array_a, sorted_array_b)
    # checks if every item in array_a is in the merged array
    contains_a = True
    for item_a in sorted_array_a.iterator():
        contains_item = False
        for item in array.iterator():
            if item_a == item:
                contains_item = True
                break
        if not contains_item:
            contains_a = False
            break
    yield True
    yield contains_a


@Test
def merge_then_contains_b(
    array_a: Array[Item],
    array_b: Array[Item],
):
    sorted_array_a = Array.build(iter(sorted(array_a.iterator())))
    sorted_array_b = Array.build(iter(sorted(array_b.iterator())))
    array = merge(sorted_array_a, sorted_array_b)
    # checks if every item in array_b is in the merged array
    contains_b = True
    for item_a in sorted_array_b.iterator():
        contains_item = False
        for item in array.iterator():
            if item_a == item:
                contains_item = True
                break
        if not contains_item:
            contains_b = False
            break
    yield True
    yield contains_b


@Test
def merge_sort_works(
    array: Array[Item],
):
    sorted_array = Array.build(iter(sorted(array.iterator())))
    merge_sort(array)
    yield sorted_array
    yield array
