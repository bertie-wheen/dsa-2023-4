"""
Data Structures & Algorithms

Lab 3: More Lists, Stacks & Queues

Shunting Yard Algorithm Solution
"""

from collections.abc import Iterator
from enum import Enum
from typing import TypeAlias

from lib.base import Base

from lab3.core.linked_queue import LinkedQueue as Queue
from lab3.core.linked_stack import LinkedStack as Stack


class Associativity(Base, Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


class Parenthesis(Base, Enum):
    OPENING = 0
    CLOSING = 1


class Operator(Base, Enum):
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3
    MODULO = 4
    EXPONENTIATION = 5

    def get_precedence(self) -> int:
        match self:
            case Operator.EXPONENTIATION:
                return 2
            case Operator.MULTIPLICATION | Operator.DIVISION | Operator.MODULO:
                return 1
            case Operator.ADDITION | Operator.SUBTRACTION:
                return 0

    def get_associativity(self) -> Associativity:
        match self:
            case Operator.EXPONENTIATION:
                return Associativity.RIGHT
            case _:
                return Associativity.LEFT

    def is_not_associative(self):
        return self.get_associativity() is Associativity.NONE

    def is_left_associative(self):
        return self.get_associativity() is Associativity.LEFT

    def is_right_associative(self):
        return self.get_associativity() is Associativity.RIGHT


class ValueToken(Base):
    def __init__(self, value: int | str) -> None:
        self.value = value


class FunctionToken(Base):
    def __init__(self, name: str) -> None:
        self.name = name


class OperatorToken(Base):
    def __init__(self, operator: Operator) -> None:
        self.operator = operator


class ParenthesisToken(Base):
    def __init__(self, parenthesis: Parenthesis) -> None:
        self.parenthesis = parenthesis


class CommaToken(Base):
    pass


Token: TypeAlias = ValueToken | FunctionToken | OperatorToken | ParenthesisToken | CommaToken


def shunt(tokens: Iterator[Token]) -> Iterator[Token]:
    """
    Convert the given tokens from infix to postfix using the shunting yard algorithm.

    :parameter tokens: tokens in infix form
    :returns: tokens in postfix form
    :raises ValueError: if the given tokens are invalid (for example because of unbalanced parentheses)
    """
    stack = Stack[FunctionToken | OperatorToken | ParenthesisToken]()
    output = Queue[Token]()
    for token in tokens:
        match token:
            case ValueToken():
                output.enqueue(token)
            case FunctionToken():
                stack.push(token)
            case OperatorToken(operator=token_operator):
                while not stack.is_empty():
                    match stack.peek():
                        case FunctionToken():
                            pass
                        case OperatorToken(operator=stack_operator):
                            token_precedence = token_operator.get_precedence()
                            stack_precedence = stack_operator.get_precedence()
                            if token_precedence > stack_precedence:
                                break
                            if token_precedence == stack_precedence:
                                if token_operator.get_associativity() is not Associativity.LEFT:
                                    break
                        case ParenthesisToken(parenthesis=Parenthesis.OPENING):
                            break
                        case _:
                            # this shouldn't happen
                            # because we don't push anything else
                            assert False
                    output.enqueue(stack.pop())
                stack.push(token)
            case ParenthesisToken(parenthesis=Parenthesis.OPENING):
                stack.push(token)
            case ParenthesisToken(parenthesis=Parenthesis.CLOSING):
                while not stack.is_empty() and type(stack.peek()) is not ParenthesisToken:
                    output.enqueue(stack.pop())
                if stack.is_empty():
                    raise ValueError("closing parenthesis with no matching opening parenthesis")
                stack.pop()
                if not stack.is_empty() and type(stack.peek()) is FunctionToken:
                    output.enqueue(stack.pop())
            case CommaToken():
                while not stack.is_empty() and type(stack.peek()) is not ParenthesisToken:
                    output.enqueue(stack.pop())
    while not stack.is_empty():
        token = stack.pop()
        if type(token) is ParenthesisToken:
            raise ValueError("opening parenthesis with no matching closing parenthesis")
        output.enqueue(token)
    return output.iterator()
