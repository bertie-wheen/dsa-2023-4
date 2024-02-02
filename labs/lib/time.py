from time import time_ns


def get_time() -> int:
    """
    Get the current UTC time in nanoseconds since the epoch.

    :returns: the number of nanoseconds since 1970-01-01 00:00
    """
    return time_ns()
