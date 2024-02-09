from collections.abc import Iterator
from copy import copy
from typing import Annotated

from lib.errors import EmptyCollectionError
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item

from lab3.core.array_stack.exercise import ArrayStack


@Test
def push_then_get_length(
    items: Iterator[Item],
    top_item: Item,
):
    stack = ArrayStack.build(items)
    length = stack.get_length()
    stack.push(top_item)
    yield length + 1
    yield stack.get_length()


@Test
def push_then_peek(
    items: Iterator[Item],
    top_item: Item,
):
    stack = ArrayStack.build(items)
    stack.push(top_item)
    yield top_item
    yield stack.peek()


@Test
def push_then_pop(
    items: Iterator[Item],
    top_item: Item,
):
    stack = ArrayStack.build(items)
    stack.push(top_item)
    yield top_item
    yield stack.pop()


@Test
def push_repeatedly_then_reverse_iterator(
    items: Iterator[Item],
):
    stack = ArrayStack()
    for item in copy(items):
        stack.push(item)
    yield items
    yield stack.reverse_iterator()


@Test
def peek_on_empty_stack():
    stack = ArrayStack()
    yield EmptyCollectionError
    yield stack.peek()


@Test
def peek_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    stack = ArrayStack.build(items)
    length = stack.get_length()
    stack.peek()
    yield length
    yield stack.get_length()


@Test
def peek_then_pop(
    items: Annotated[Iterator[Item], GE(1)],
):
    stack = ArrayStack.build(items)
    yield stack.peek()
    yield stack.pop()


@Test
def pop_on_empty_stack():
    stack = ArrayStack()
    yield EmptyCollectionError
    yield stack.pop()


@Test
def pop_then_get_length(
    items: Annotated[Iterator[Item], GE(1)],
):
    stack = ArrayStack.build(items)
    length = stack.get_length()
    stack.pop()
    yield length - 1
    yield stack.get_length()
