from collections.abc import Iterator

from lib.type_vars import Item


def iterator(*items: Item) -> Iterator[Item]:
    return iter(items)
