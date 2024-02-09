from lib.iterator import iterator
from lib.test import Test

from lab3.plus.shunting_yard.exercise import *


@Test
def shunt_quadratic_formula():
    # the greater case of the quadratic formula
    #     infix: ( 0- b + sqrt ( b ^ 2 - 4 * a * c ) ) / ( 2 * a )
    #   postfix: b 0- b 2 ^ 4 a * c * - sqrt + 2 a * /
    # (note that 0- represents unary negation, and - binary subtraction)
    yield iterator(
        ValueToken("b"),
        FunctionToken("-"),
        ValueToken("b"),
        ValueToken(2),
        OperatorToken(Operator.EXPONENTIATION),
        ValueToken(4),
        ValueToken("a"),
        OperatorToken(Operator.MULTIPLICATION),
        ValueToken("c"),
        OperatorToken(Operator.MULTIPLICATION),
        OperatorToken(Operator.SUBTRACTION),
        FunctionToken("sqrt"),
        OperatorToken(Operator.ADDITION),
        ValueToken(2),
        ValueToken("a"),
        OperatorToken(Operator.MULTIPLICATION),
        OperatorToken(Operator.DIVISION),
    )
    yield shunt(
        iterator(
            ParenthesisToken(Parenthesis.OPENING),
            FunctionToken("-"),
            ValueToken("b"),
            OperatorToken(Operator.ADDITION),
            FunctionToken("sqrt"),
            ParenthesisToken(Parenthesis.OPENING),
            ValueToken("b"),
            OperatorToken(Operator.EXPONENTIATION),
            ValueToken(2),
            OperatorToken(Operator.SUBTRACTION),
            ValueToken(4),
            OperatorToken(Operator.MULTIPLICATION),
            ValueToken("a"),
            OperatorToken(Operator.MULTIPLICATION),
            ValueToken("c"),
            ParenthesisToken(Parenthesis.CLOSING),
            ParenthesisToken(Parenthesis.CLOSING),
            OperatorToken(Operator.DIVISION),
            ParenthesisToken(Parenthesis.OPENING),
            ValueToken(2),
            OperatorToken(Operator.MULTIPLICATION),
            ValueToken("a"),
            ParenthesisToken(Parenthesis.CLOSING),
        )
    )


@Test
def shunt_wikipedia_example_1():
    # the first detailed example from wikipedia
    #     infix: 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3
    #   postfix: 3 4 2 * 1 5 - 2 3 ^ ^ / +
    yield iterator(
        ValueToken(3),
        ValueToken(4),
        ValueToken(2),
        OperatorToken(Operator.MULTIPLICATION),
        ValueToken(1),
        ValueToken(5),
        OperatorToken(Operator.SUBTRACTION),
        ValueToken(2),
        ValueToken(3),
        OperatorToken(Operator.EXPONENTIATION),
        OperatorToken(Operator.EXPONENTIATION),
        OperatorToken(Operator.DIVISION),
        OperatorToken(Operator.ADDITION),
    )
    yield shunt(
        iterator(
            ValueToken(3),
            OperatorToken(Operator.ADDITION),
            ValueToken(4),
            OperatorToken(Operator.MULTIPLICATION),
            ValueToken(2),
            OperatorToken(Operator.DIVISION),
            ParenthesisToken(Parenthesis.OPENING),
            ValueToken(1),
            OperatorToken(Operator.SUBTRACTION),
            ValueToken(5),
            ParenthesisToken(Parenthesis.CLOSING),
            OperatorToken(Operator.EXPONENTIATION),
            ValueToken(2),
            OperatorToken(Operator.EXPONENTIATION),
            ValueToken(3),
        )
    )


@Test
def shunt_wikipedia_example_2():
    # the second detailed example from wikipedia
    #     infix: sin ( max ( 2 , 3 ) / 3 * pi )
    #   postfix: 2 3 max 3 / pi * sin
    yield iterator(
        ValueToken(2),
        ValueToken(3),
        FunctionToken("max"),
        ValueToken(3),
        OperatorToken(Operator.DIVISION),
        ValueToken("pi"),
        OperatorToken(Operator.MULTIPLICATION),
        FunctionToken("sin"),
    )
    yield shunt(
        iterator(
            FunctionToken("sin"),
            ParenthesisToken(Parenthesis.OPENING),
            FunctionToken("max"),
            ParenthesisToken(Parenthesis.OPENING),
            ValueToken(2),
            CommaToken(),
            ValueToken(3),
            ParenthesisToken(Parenthesis.CLOSING),
            OperatorToken(Operator.DIVISION),
            ValueToken(3),
            OperatorToken(Operator.MULTIPLICATION),
            ValueToken("pi"),
            ParenthesisToken(Parenthesis.CLOSING),
        )
    )


@Test
def shunt_function_vs_operator_precedence_example():
    # a simple example of prioritising functions over operators
    #     infix: f x + g y
    #   postfix: x f y g +
    yield iterator(
        ValueToken("x"),
        FunctionToken("f"),
        ValueToken("y"),
        FunctionToken("g"),
        OperatorToken(Operator.ADDITION),
    )
    yield shunt(
        iterator(
            FunctionToken("f"),
            ValueToken("x"),
            OperatorToken(Operator.ADDITION),
            FunctionToken("g"),
            ValueToken("y"),
        )
    )
