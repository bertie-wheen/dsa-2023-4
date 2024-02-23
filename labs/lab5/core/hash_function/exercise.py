"""
Data Structures & Algorithms

Lab 5: Hash Maps

Hash Functions Exercise
"""

from typing import Any

from lib.base import Base
from lib.numberify import to_int
from lib.random import generate_int


# greater than 2**64
_prime = 2**100 - 1


class HashFunction(Base):
    """
    A random hash function from a universal family.

    Space: O(1)
    """

    _a: int
    _b: int
    _size: int

    def __init__(self, size: int) -> None:
        """
        Initialise this hash function.

        Randomly choose it from the universal family.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter size: the size of the space of possible hashes
        :raises ValueError: if ``size < 1``
        """
        if size < 1:
            raise ValueError
        self._a = generate_int(1, _prime - 1)
        self._b = generate_int(0, _prime - 1)
        self._size = size

    def hash(self, thing: Any) -> int:
        """
        Returns a hash of the given thing within the given range.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter thing: the thing to hash
        :returns: a non-negative integer less than ``size``
        """
        raise NotImplementedError
