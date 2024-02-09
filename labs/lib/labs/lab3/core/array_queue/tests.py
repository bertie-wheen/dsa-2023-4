from collections.abc import Iterator
from copy import copy
from typing import Annotated

from lib.errors import EmptyCollectionError
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab3.core.linked_queue.exercise import LinkedQueue


@Test
def enqueue_then_get_length(
    items: Iterator[Item],
    back_item: Item,
):
    queue = LinkedQueue.build(items)
    length = queue.get_length()
    queue.enqueue(back_item)
    yield length + 1
    yield queue.get_length()


@Test
def enqueue_on_empty_queue_then_front(
    item: Item,
):
    queue = LinkedQueue()
    queue.enqueue(item)
    yield item
    yield queue.front()


@Test
def enqueue_on_empty_queue_then_dequeue(
    item: Item,
):
    queue = LinkedQueue()
    queue.enqueue(item)
    yield item
    yield queue.dequeue()


@Test
def enqueue_repeatedly_then_iterator(
    items: Iterator[Item],
):
    queue = LinkedQueue()
    for item in copy(items):
        queue.enqueue(item)
    yield items
    yield queue.iterator()


@Test
def front_on_empty_queue():
    queue = LinkedQueue()
    yield EmptyCollectionError
    yield queue.front()


@Test
def front_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    queue = LinkedQueue.build(items)
    length = queue.get_length()
    queue.front()
    yield length
    yield queue.get_length()


@Test
def front_then_dequeue(
    items: Annotated[Iterator[Item], GE(1)],
):
    queue = LinkedQueue.build(items)
    yield queue.front()
    yield queue.dequeue()


@Test
def dequeue_on_empty_queue():
    queue = LinkedQueue()
    yield EmptyCollectionError
    yield queue.dequeue()


@Test
def dequeue_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    queue = LinkedQueue.build(items)
    length = queue.get_length()
    queue.dequeue()
    yield length - 1
    yield queue.get_length()
