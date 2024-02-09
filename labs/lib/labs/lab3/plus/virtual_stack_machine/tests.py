from lib.array import Array
from lib.errors import EmptyCollectionError
from lib.iterator import iterator
from lib.test import Test

from lab3.core.linked_stack import LinkedStack
from lab3.plus.virtual_stack_machine.exercise import Opcode, VirtualStackMachine


@Test
def dupe_on_empty_stack():
    bytecode = Array.build(
        iterator(
            Opcode.DUPE.value,
        )
    )
    vm = VirtualStackMachine(bytecode)
    yield EmptyCollectionError
    yield vm.run()


@Test
def dupe_on_non_empty_stack(
    values: LinkedStack[int],
    top_value: int,
):
    bytecode = Array.build(
        iterator(
            Opcode.DUPE.value,
        )
    )
    values.push(top_value)
    vm = VirtualStackMachine(bytecode, values=values.iterator())
    values.push(top_value)
    vm.run()
    yield values.iterator()
    yield vm.values()


@Test
def movu(
    values_below: LinkedStack[int],
    values_above: LinkedStack[int],
    value: int,
):
    old_values = LinkedStack.build(values_below.iterator())
    old_values.push(value)
    for value_above in values_above.iterator():
        old_values.push(value_above)
    index = values_above.get_length()
    bytecode = Array.build(
        iterator(
            Opcode.PUSH.value,
            index,
            Opcode.MOVU.value,
        )
    )
    vm = VirtualStackMachine(bytecode, values=old_values.iterator())
    vm.run()
    new_values = LinkedStack.build(values_below.iterator())
    for value_above in values_above.iterator():
        new_values.push(value_above)
    new_values.push(value)
    yield new_values.iterator()
    yield vm.values()


@Test
def movd(
    values_below: LinkedStack[int],
    values_above: LinkedStack[int],
    value: int,
):
    old_values = LinkedStack.build(values_below.iterator())
    for value_above in values_above.iterator():
        old_values.push(value_above)
    old_values.push(value)
    index = values_above.get_length()
    bytecode = Array.build(
        iterator(
            Opcode.PUSH.value,
            index,
            Opcode.MOVD.value,
        )
    )
    vm = VirtualStackMachine(bytecode, values=old_values.iterator())
    vm.run()
    new_values = LinkedStack.build(values_below.iterator())
    new_values.push(value)
    for value_above in values_above.iterator():
        new_values.push(value_above)
    yield new_values.iterator()
    yield vm.values()


@Test
def swap(
    values: LinkedStack[int],
    value_a: int,
    value_b: int,
):
    old_values = LinkedStack.build(values.iterator())
    old_values.push(value_a)
    old_values.push(value_b)
    bytecode = Array.build(
        iterator(
            Opcode.SWAP.value,
        )
    )
    vm = VirtualStackMachine(bytecode, values=old_values.iterator())
    vm.run()
    new_values = LinkedStack.build(values.iterator())
    new_values.push(value_b)
    new_values.push(value_a)
    yield new_values.iterator()
    yield vm.values()
