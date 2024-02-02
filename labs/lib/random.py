from random import randint, random


def generate_bool(chance: float = 0.5) -> bool:
    """
    Generate a random boolean, with the given chance of it being ``True``.

    :parameter chance: the probability that the boolean will be ``True``
    :returns: a random boolean
    :raises ValueError: unless ``0 <= chance <= 1``
    """
    if not 0 <= chance <= 1:
        raise ValueError
    return random() < chance


def generate_int(lower: int, upper: int) -> int:
    """
    Generate a random integer in the range [``lower``, ``upper``].

    Generated integers will be uniformly distributed within the given range.

    :parameter lower: the inclusive lower bound of the range
    :parameter upper: the inclusive upper bound of the range
    :returns: a random integer in that range
    :raises ValueError: if ``lower > upper``
    """
    return randint(lower, upper)


def generate_index(count: int) -> int:
    """
    Generate a random non-negative integer less than ``count``.

    :parameter count: the number of distinct integers possible
    :returns: a random integer in the given range
    :raises ValueError: if ``count <= 0``
    """
    if count <= 0:
        raise ValueError
    return generate_int(0, count - 1)
