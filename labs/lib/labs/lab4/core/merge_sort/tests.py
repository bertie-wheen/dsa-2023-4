from lib.array import Array
from lib.test import Test
from lib.type_vars import Item

from lab4.core.merge_sort.exercise import merge_sort


@Test
def merge_sort_works(
    array: Array[Item],
):
    sorted_array = Array.build(iter(sorted(array.iterator())))
    merge_sort(array)
    yield sorted_array
    yield array
