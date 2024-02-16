"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Memoization Exercise
"""

from lab4.core.sorted_array_map import SortedArrayMap


def slow_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    return slow_fibonacci(n - 2) + slow_fibonacci(n - 1)


_cache = SortedArrayMap[int, int]()


def _fast_fibonacci_helper(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fast_fibonacci(n - 2) + fast_fibonacci(n - 1)


def fast_fibonacci(n: int) -> int:
    if _cache.contains(n):
        return _cache.get(n)
    fib = _fast_fibonacci_helper(n)
    _cache.insert(n, fib)
    return fib
