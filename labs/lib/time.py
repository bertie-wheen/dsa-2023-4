from time import time


def get_time() -> float:
    """
    Get the current UTC time in seconds since the epoch.

    :returns: the number of seconds since 1970-01-01 00:00
    """
    return time()
