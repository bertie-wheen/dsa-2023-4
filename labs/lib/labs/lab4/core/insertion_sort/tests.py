from lib.array import Array
from lib.test import Test
from lib.type_vars import Item

from lab4.core.insertion_sort.exercise import insertion_sort


@Test
def insertion_sort_works(
    array: Array[Item],
):
    sorted_array = Array.build(iter(sorted(array.iterator())))
    insertion_sort(array)
    yield sorted_array
    yield array
