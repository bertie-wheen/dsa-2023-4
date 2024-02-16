from collections.abc import Iterator


def split_on_whitespace(input: str) -> Iterator[str]:
    return iter(input.split())
