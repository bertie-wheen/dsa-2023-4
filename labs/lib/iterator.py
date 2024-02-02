from collections.abc import Iterable, Iterator

from lib.base import Base
from lib.type_vars import Item


# class MagicIterator(Base[Item], Iterator[Item]):
#     def __init__(self, items: Iterable[Item]) -> None:
#         self._items = items
#
#     def __next__(self):
#         ...
#
#     def __iter__(self):
#         return self
#


def iterator(*items: Item) -> Iterator[Item]:
    # return MagicIterator(items)
    return iter(items)
