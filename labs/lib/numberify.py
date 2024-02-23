from typing import Any


def to_int(thing: Any) -> int:
    """
    Convert anything to an int.

    The int will be non-negative, and less than 2^64.

    :parameter thing: the thing to convert to an int
    :returns: an int
    """
    # return 2**63 + hash(thing)  # this should be safe
    return hash(thing) % 2**64  # but this is safer (protects against unusual custom __hash__s)
