from collections.abc import Iterator


def split(input: str) -> Iterator[str]:
    return iter(input.split())
