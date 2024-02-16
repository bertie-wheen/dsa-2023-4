"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Virtual Stack Machines Solution
"""

from collections.abc import Iterator
from enum import Enum
from typing import Optional

from lib.array import Array
from lib.base import Base

from lab3.core.linked_queue import LinkedQueue as Queue
from lab3.core.linked_stack import LinkedStack as Stack


def _bool_to_int(b: bool) -> int:
    return 1 if b else 0


def _int_to_bool(b: int) -> bool:
    return b != 0


# noinspection SpellCheckingInspection
class Opcode(Base, Enum):
    """
    The opcode of an instruction.
    """

    # fmt: off
    NOOP  = 0b00000000  # no operation
    PUSH  = 0b00000100  # push
    DUPE  = 0b00100100  # duplicate
    MOVU  = 0b00010100  # move up
    MOVD  = 0b01010100  # move down
    SWAP  = 0b00110100  # swap
    POP   = 0b00001100  # pop
    EMPTY = 0b00011100  # is empty
    J     = 0b00000010  # jump
    JC    = 0b00100010  # conditional jump
    CALL  = 0b00001010  # call
    CALLC = 0b00101010  # conditional call
    RET   = 0b00011010  # return
    RETC  = 0b00111010  # conditional return
    PRINT = 0b00000110  # print character
    EXIT  = 0b00001110  # exit / halt
    NEG   = 0b00000001  # negate
    ADD   = 0b00000101  # add
    SUB   = 0b00100101  # subtract
    MUL   = 0b00010101  # multiply
    DIV   = 0b00110101  # divide
    MOD   = 0b01110101  # modulo
    EXP   = 0b00001101  # exponentiate
    MIN   = 0b00011101  # min
    MAX   = 0b00111101  # max
    NOT   = 0b00000011  # logical not
    EQ    = 0b00000111  # equal
    NE    = 0b00100111  # not equal
    LE    = 0b00000111  # less than or equal
    LT    = 0b00010111  # less than
    GE    = 0b00100111  # greater than or equal
    GT    = 0b00110111  # greater than
    AND   = 0b00001111  # logical and
    OR    = 0b00101111  # logical or
    IF    = 0b00011111  # if-else
    # fmt: on


class VirtualStackMachine(Base):
    """
    A virtual machine implementing a simple stack-based instruction set.
    """

    _bytecode: Array[int]
    _instruction_pointer: int
    _output: Queue[str]
    _values: Stack[int]
    _return_addresses: Stack[int]

    def __init__(
        self,
        bytecode: Array[int],
        instruction_pointer: int = 0,
        values: Optional[Iterator[int]] = None,
        return_addresses: Optional[Iterator[int]] = None,
    ) -> None:
        """
        Initialize the virtual machine.

        The bytecode given is the VM's memory, and will be interpreted as a program.

        :parameter bytecode: the bytecode
        :parameter instruction_pointer: the initial value of the instruction pointer (default 0)
        :parameter values: an optional iterable of initial values, top-first (default None)
        :parameter return_addresses: an optional iterable of initial return addresses, top-first (default None)
        """
        self._bytecode = bytecode
        self._instruction_pointer = instruction_pointer
        self._output = Queue()
        if values is None:
            self._values = Stack()
        else:
            self._values = Stack.build(values)
        if return_addresses is None:
            self._return_addresses = Stack()
        else:
            self._return_addresses = Stack.build(return_addresses)

    def output(self) -> Iterator[str]:
        """
        Get an iterator over the program's output queue.

        :returns: an iterator over the output, oldest-to-newest
        """
        return self._output.iterator()

    def values(self) -> Iterator[int]:
        """
        Get an iterator over the program's value stack.

        :returns: an iterator over the values, top-to-bottom
        """
        return self._values.iterator()

    def return_addresses(self) -> Iterator[int]:
        """
        Get an iterator over the program's return address stack.

        :returns: an iterator over the return addresses, top-to-bottom
        """
        return self._return_addresses.iterator()

    def is_running(self) -> bool:
        """
        Check whether the program is still running.

        The program stops when the machine finishes processing all the instructions
        or when it processes an ``EXIT`` instruction.

        :returns: ``True`` if the program is still running, else ``False``
        """
        return 0 <= self._instruction_pointer < self._bytecode.get_length()

    def has_exited(self) -> bool:
        """
        Whether the program has exited.

        The program exits when the machine finishes processing all the instructions
        or when it processes an ``EXIT`` instruction.

        :returns: ``True`` if the program has stopped running, else ``False``
        """
        return not self.is_running()

    def fetch(self) -> int:
        """
        Fetch the current bytecode item and advance the instruction pointer.

        Will fetch an instruction unless a ``PUSH`` instruction was just fetched, when it will fetch its argument.

        :returns: the current bytecode item (either an instruction or an argument)
        :raises IndexError: if the program has exited
        """
        instruction = self._bytecode.get_at(self._instruction_pointer)
        self._instruction_pointer += 1
        return instruction

    def process(self) -> None:
        """
        Process (fetch, decode and execute) an instruction.

        If the program has exited, do nothing.

        :raises EmptyCollectionError: if a ``PEEK`` or ``POP`` on an empty value stack, or a ``RET`` or ``RETC`` on an empty return address stack
        :raises IndexError: if a ``MOVU`` or ``MOVD`` is given an invalid index, or a ``PUSH`` is given no argument
        :raises ValueError: if an opcode is unrecognised
        :raises ZeroDivisionError: if ``DIV`` is given a divisor of 0
        """
        if self.has_exited():
            return
        opcode = self.fetch()
        match Opcode(opcode):
            case Opcode.NOOP:
                pass
            case Opcode.PUSH:
                value = self.fetch()
                self._values.push(value)
            case Opcode.DUPE:
                value = self._values.peek()
                self._values.push(value)
            case Opcode.MOVU:
                index = self._values.pop()
                if not 0 <= index < self._values.get_length():
                    raise IndexError
                temp_stack = Stack()
                for _ in range(index):
                    temp = self._values.pop()
                    temp_stack.push(temp)
                value = self._values.pop()
                for _ in range(index):
                    temp = temp_stack.pop()
                    self._values.push(temp)
                self._values.push(value)
            case Opcode.MOVD:
                index = self._values.pop()
                if not 0 <= index < self._values.get_length():
                    raise IndexError
                temp_stack = Stack()
                value = self._values.pop()
                for _ in range(index):
                    temp = self._values.pop()
                    temp_stack.push(temp)
                self._values.push(value)
                for _ in range(index):
                    temp = temp_stack.pop()
                    self._values.push(temp)
            case Opcode.SWAP:
                operand_a = self._values.pop()
                operand_b = self._values.pop()
                self._values.push(operand_a)
                self._values.push(operand_b)
            case Opcode.POP:
                self._values.pop()
            case Opcode.EMPTY:
                is_empty = self._values.is_empty()
                self._values.push(_bool_to_int(is_empty))
            case Opcode.J:
                destination_address = self._values.pop()
                self._instruction_pointer = destination_address
            case Opcode.JC:
                destination_address = self._values.pop()
                condition = self._values.pop()
                if _int_to_bool(condition):
                    self._instruction_pointer = destination_address
            case Opcode.CALL:
                function_address = self._values.pop()
                return_address = self._instruction_pointer
                self._return_addresses.push(return_address)
                self._instruction_pointer = function_address
            case Opcode.CALLC:
                function_address = self._values.pop()
                condition = self._values.pop()
                if _int_to_bool(condition):
                    return_address = self._instruction_pointer
                    self._return_addresses.push(return_address)
                    self._instruction_pointer = function_address
            case Opcode.RET:
                return_address = self._return_addresses.pop()
                self._instruction_pointer = return_address
            case Opcode.RETC:
                condition = self._values.pop()
                if _int_to_bool(condition):
                    return_address = self._return_addresses.pop()
                    self._instruction_pointer = return_address
            case Opcode.PRINT:
                character_code = self._values.pop()
                character = chr(character_code)
                self._output.enqueue(character)
            case Opcode.EXIT:
                self._instruction_pointer = -1
            case Opcode.NEG:
                operand = self._values.pop()
                result = -operand
                self._values.push(result)
            case Opcode.ADD:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a + operand_b
                self._values.push(result)
            case Opcode.SUB:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a - operand_b
                self._values.push(result)
            case Opcode.MUL:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a * operand_b
                self._values.push(result)
            case Opcode.DIV:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a // operand_b
                self._values.push(result)
            case Opcode.MOD:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a % operand_b
                self._values.push(result)
            case Opcode.EXP:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a**operand_b
                self._values.push(result)
            case Opcode.MIN:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = min(operand_a, operand_b)
                self._values.push(result)
            case Opcode.MAX:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = max(operand_a, operand_b)
                self._values.push(result)
            case Opcode.NOT:
                operand = _int_to_bool(self._values.pop())
                result = not operand
                self._values.push(_bool_to_int(result))
            case Opcode.EQ:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a == operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.NE:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a != operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.LE:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a <= operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.LT:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a < operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.GE:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a >= operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.GT:
                operand_b = self._values.pop()
                operand_a = self._values.pop()
                result = operand_a > operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.AND:
                operand_b = _int_to_bool(self._values.pop())
                operand_a = _int_to_bool(self._values.pop())
                result = operand_a and operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.OR:
                operand_b = _int_to_bool(self._values.pop())
                operand_a = _int_to_bool(self._values.pop())
                result = operand_a or operand_b
                self._values.push(_bool_to_int(result))
            case Opcode.IF:
                if_false = self._values.pop()
                if_true = self._values.pop()
                condition = self._values.pop()
                result = if_true if condition else if_false
                self._values.push(result)
            case _:
                raise ValueError

    def run(self) -> None:
        """
        Run until exit.

        :raises EmptyCollectionError: if a ``PEEK`` or ``POP`` on an empty value stack, or a ``RET`` or ``RETC`` on an empty return address stack
        :raises IndexError: if a ``MOVU`` or ``MOVD`` is given an invalid index, or a ``PUSH`` is given no argument
        :raises ValueError: if an opcode is unrecognised
        :raises ZeroDivisionError: if ``DIV`` is given a divisor of 0
        """
        while self.is_running():
            self.process()
