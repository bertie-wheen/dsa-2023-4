from collections.abc import Iterator
from copy import copy
from typing import Annotated

from lib.errors import EmptyCollectionError
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab3.plus.linked_deque.exercise import LinkedDeque


@Test
def insert_first_then_get_length(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.insert_first(top_item)
    yield length + 1
    yield deque.get_length()


@Test
def insert_first_then_get_first(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    deque.insert_first(top_item)
    yield top_item
    yield deque.get_first()


@Test
def insert_first_then_remove_first(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    deque.insert_first(top_item)
    yield top_item
    yield deque.remove_first()


@Test
def insert_first_repeatedly_then_reverse_iterator(
    items: Iterator[Item],
):
    deque = LinkedDeque()
    for item in copy(items):
        deque.insert_first(item)
    yield items
    yield deque.reverse_iterator()


@Test
def insert_last_then_get_length(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.insert_last(top_item)
    yield length + 1
    yield deque.get_length()


@Test
def insert_last_then_get_last(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    deque.insert_last(top_item)
    yield top_item
    yield deque.get_last()


@Test
def insert_last_then_remove_last(
    items: Iterator[Item],
    top_item: Item,
):
    deque = LinkedDeque.build(items)
    deque.insert_last(top_item)
    yield top_item
    yield deque.remove_last()


@Test
def insert_last_repeatedly_then_iterator(
    items: Iterator[Item],
):
    deque = LinkedDeque()
    for item in copy(items):
        deque.insert_last(item)
    yield items
    yield deque.iterator()


@Test
def get_first_on_empty_deque():
    deque = LinkedDeque()
    yield EmptyCollectionError
    yield deque.get_first()


@Test
def get_first_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.get_first()
    yield length
    yield deque.get_length()


@Test
def get_first_then_remove_first(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    yield deque.get_first()
    yield deque.remove_first()


@Test
def get_last_on_empty_deque():
    deque = LinkedDeque()
    yield EmptyCollectionError
    yield deque.get_last()


@Test
def get_last_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.get_last()
    yield length
    yield deque.get_length()


@Test
def get_last_then_remove_last(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    yield deque.get_last()
    yield deque.remove_last()


@Test
def remove_first_on_empty_deque():
    deque = LinkedDeque()
    yield EmptyCollectionError
    yield deque.remove_first()


@Test
def remove_first_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.remove_first()
    yield length - 1
    yield deque.get_length()


@Test
def remove_last_on_empty_deque():
    deque = LinkedDeque()
    yield EmptyCollectionError
    yield deque.remove_last()


@Test
def remove_last_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    deque = LinkedDeque.build(items)
    length = deque.get_length()
    deque.remove_last()
    yield length - 1
    yield deque.get_length()
