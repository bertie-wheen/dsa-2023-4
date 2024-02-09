# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/README.md))

### [The Shunting Yard Algorithm](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/shunting_yard/README.md)
```shell
python labs shunting_yard
```

Mathematical operations are usually written like this:
```
4 + 2
2 * 8
4 + 2 * 8
(4 + 2) * 8
8 * 2 + 4
8 * (2 + 4)
```

This is known as "infix" form, because the operators (e.g. `+` or `*`) are writen _in_-between their operands (e.g. `4`
or `2`). Infix notation feels very natural to many people, but it does come with some disadvantages. A particular
disadvantage is that, even with a standardised order of operations (the convention that some operations, such as `*`,
have higher "precedence" than others, such as `+` - you likely learned this in school as
"BODMAS"/"BIDMAS"/"PEMDAS"/etc. - which means that `4 + 2 * 8` is the same as `4 + (2 * 8)` and `8 * 2 + 4` is the same
as `(8 * 2) + 4`), parentheses are still sometimes needed, such as in the cases `(4 + 2) * 8` and `8 * (2 + 4)` above.
These would be different expressions if the parentheses were removed - and equivalent expressions without parentheses,
e.g. `4 * 8 + 2 * 8` and `8 * 2 + 8 * 4`, would be overly verbose and repetitive.

As well as the more normal infix notation, however, there are alternatives such as "prefix" and "postfix" notation.
These respectively place the operators _before_ or _after_ their operands, and are perhaps best illustrated by example:

| Infix       | Prefix    | Postfix   |
|-------------|-----------|-----------|
| 4 + 2       | + 4 2     | 4 2 +     |
| 2 * 8       | * 2 8     | 2 8 *     |
| 4 + 2 * 8   | + 4 * 2 8 | 4 2 8 * + |
| (4 + 2) * 8 | * + 4 2 8 | 4 2 + 8 * |
| 8 * 2 + 4   | + * 8 2 4 | 8 2 * 4 + |
| 8 * (2 + 4) | * 8 + 2 4 | 8 2 4 + * |

(Prefix notation is sometimes called "Polish notation", and postfix notation is often called "reverse Polish notation",
or "RPN".)

One of the advantages of these notations is that they don't require parentheses, or for operators to be organised in
precedence hierarchies, to avoid ambiguity. Taste is of course subjective, and they're certainly less common, but some
people find them more elegant. Hewlett-Packard calculators used to use postfix notation, as did calculators in the
Soviet Union, as well as some older computers, including the legendary
[Z3](https://en.wikipedia.org/wiki/Z3_(computer)). To this day, there are programming languages such as
[Forth](https://en.wikipedia.org/wiki/Forth_(programming_language)) and
[PostScript](https://en.wikipedia.org/wiki/PostScript) that use postfix notation.

The "shunting yard" algorithm is a way to convert expressions in infix form into postfix form.

[Wikipedia](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) describes it in pseudocode as:
```java
while there are tokens to be read:
    read a token
    if the token is:
    - a number:
        put it into the output queue
    - a function:
        push it onto the operator stack
    - an operator o1:
        while (
            there is an operator o2 at the top of the operator stack which is not a left parenthesis,
            and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
        ):
            pop o2 from the operator stack into the output queue
        push o1 onto the operator stack
    - a ",":
        while the operator at the top of the operator stack is not a left parenthesis:
             pop the operator from the operator stack into the output queue
    - a left parenthesis (i.e. "("):
        push it onto the operator stack
    - a right parenthesis (i.e. ")"):
        while the operator at the top of the operator stack is not a left parenthesis:
            {assert the operator stack is not empty}
            /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
            pop the operator from the operator stack into the output queue
        {assert there is a left parenthesis at the top of the operator stack}
        pop the left parenthesis from the operator stack and discard it
        if there is a function token at the top of the operator stack, then:
            pop the function from the operator stack into the output queue
/* After the while loop, pop the remaining items from the operator stack into the output queue. */
while there are tokens on the operator stack:
    /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
    {assert the operator on top of the stack is not a (left) parenthesis}
    pop the operator from the operator stack onto the output queue
```

This exercise features a version of this written in Python, with various `raise NotImplementedError`s that you are to
replace with appropriate lines of code. Each needs only a single line of code, though depending on how you like to write
code you may prefer to write some of them as two lines. (Refer to the pseudocode above to see what might be the right
thing to do in each case.)

---

Next:
- [Virtual Stack Machines](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/virtual_stack_machine/README.md)
