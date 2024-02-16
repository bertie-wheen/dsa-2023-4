from lib.array import Array
from lib.test import Test
from lib.type_vars import Item

from lab4.core.selection_sort.exercise import selection_sort


@Test
def selection_sort_works(
    array: Array[Item],
):
    sorted_array = Array.build(iter(sorted(array.iterator())))
    selection_sort(array)
    yield sorted_array
    yield array
