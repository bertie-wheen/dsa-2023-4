"""
Data Structures & Algorithms

Lab 1: Getting Ready

Maths Exercise
"""


from collections.abc import Iterator
from math import ceil, sqrt


def divides(divisor: int, number: int) -> bool:
    """
    Check if the given divisor divides the given number.

    +--------+------+
    | Time:  | O(1) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter divisor: the divisor
    :parameter number: the number
    :returns: ``True`` if ``divisor`` | ``number``, else ``False``
    :raises ZeroDivisionError: if ``divisor == 0``
    """
    return number % divisor == 0


def is_even(number: int) -> bool:
    """
    Check if the given number is even.

    +--------+------+
    | Time:  | O(1) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter number: the number to check for evenness
    :returns: ``True`` if ``number`` is even, else ``False``
    """
    return divides(2, number)


def is_prime(number: int) -> bool:
    """
    Check if the given number is prime.

    +--------+-----------------+
    | Time:  | O(sqrt(number)) |
    +--------+-----------------+
    | Space: | O(1)            |
    +--------+-----------------+

    :parameter number: the number to check for primality
    :returns: ``True`` if ``number`` is prime, else ``False``
    :raises ValueError: if ``number < 0``
    """
    maximum_divisor = ceil(sqrt(number))
    for divisor in range(2, maximum_divisor + 1):
        if divides(divisor, number):
            return False
    return True


def factorial(n: int) -> int:
    """
    Calculates ``n`` factorial, i.e. ``1 * 2 * ... * (n - 1) * n``.

    +--------+------+
    | Time:  | O(n) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter n: the number to calculate the factorial of
    :returns: the factorial of that number
    :raises ValueError: if ``n < 1``
    """
    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    n_minus_1_factorial = factorial(n - 1)
    return n_minus_1_factorial * n


def divisors(number: int) -> Iterator[int]:
    """
    Get an iterator over the divisors of the given number.

    +--------+-----------+
    | Time:  | O(number) |
    +--------+-----------+
    | Space: | O(1)      |
    +--------+-----------+

    :parameter number: the number whose divisors are to be iterated over
    :returns: the divisors of ``number`` (from ``1`` to ``number``, inclusive)
    """
    for divisor in range(1, number + 1):
        if divides(divisor, number):
            yield divisor


def divisor_count(number: int) -> int:
    """
    Get the number of divisors the given number has.

    +--------+-----------+
    | Time:  | O(number) |
    +--------+-----------+
    | Space: | O(1)      |
    +--------+-----------+

    :parameter number: the number whose divisors are to be counted
    :returns: the number of divisors of ``number`` (from ``1`` to ``number``, inclusive)
    """
    count = 0
    for divisor in divisors(number):
        count += 1
    return count


def collatz_sequence(initial: int) -> Iterator[int]:
    """
    Get an iterator over the numbers in the given Collatz sequence.

    +--------+------+
    | Time:  | O(?) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter initial: the initial number of the sequence
    :returns: an iterator over the numbers of the sequence
    """
    number = initial
    while number != 1:
        yield number
        if is_even(number):
            number = number // 2
        else:
            number = number * 3 + 1
    yield number
