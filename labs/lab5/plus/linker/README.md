# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/README.md))

### [Linkers](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/linkers/README.md)
```shell
python labs linker
```

This example features an assembler and linker for our simple stack-based instruction set we defined in lab 3's virtual
stack machines exercise.

In that exercise we defined what the machine code looked like, but generally writing machine code by hand is pretty
painful - what people generally prefer to do is write "assembly" code, which is essentially a very simple text-based
version of the ones and zeros of machine code. It's much the same as machine code, and maps very directly onto it, but
is easier for humans to read and write.

As we described in the `virtual_stack_machine` notes, this assembly code:
```
    PUSH 1
    PUSH 2
    ADD
    PUSH 4
    MUL
```

Is equivalent to this machine code:
```
[
    0b00000100, 1,
    0b00000100, 2,
    0b00000101,
    0b00000100, 4,
    0b00010101,
]
```

(The opcodes for `PUSH`, `ADD` and `MUL` we chose were `0b00000100`, `0b00000101` and `0b00010101` respectively.)

An assembler is essentially an assembly language compiler: You give it assembly code, and it gives you the equivalent
machine code.

Well, sort of. What it actually gives you is "object code", which is partway from assembly code to machine code, but not
necessarily all the way there quite yet. To finish the job, and go from object code to machine code, you need a linker.

This is because a particular convenience assemblers afford you, as well as letting you write opcodes as text rather than
numbers, is that they let you use "labels". To understand why these are useful, you must first understand "jump"
instructions:

Examples like the one above, which adds 1 and 2, and then multiplies the result by 4, are all well and good, but what if
you wanted to conditionally branch or loop? If you were writing in a higher-level language like Python, you'd use
control-flow statements like `if` and `while`, but these don't exist in machine code!

(Admittedly, we included an opcode for an `IF` instruction in the `virtual_stack_machine` exercise, but since that's
fairly unusual and potentially confusing, we probably shouldn't have. It might be best to pretend it's not there! If
you're interested though, it's more akin to an if _expression_ than an if _statement_, but could - when combined with a
unconditional jump instruction - be used to implement if statements.)

When writing assembly / machine code, we instead use jump instructions - particularly, "conditional" jumps - to alter
the flow of execution.

After executing a _unconditional_ jump instruction, instead of then executing whatever instruction was supposed to be
next, the program will "jump" to somewhere else in the program. The way this works is that you give it an address, and
it sets the instruction pointer to that address.

A _conditional_ jump only sets it to that address if some condition is met, otherwise the instruction pointer is just
incremented like normal.

We can therefore use conditional jumps (also known as "branches", or "branching instructions") to implement both
conditionals (like `if`) and loops (like `while`).

In both cases, the condition is evaluated, and used as the basis for a conditional jump, after which - depending on the
condition - we then either execute the body of the `if`/`while` (that is, the code inside it), or skip ahead to the code
immediately after it and continue execution from there. (Usually, the body immediately follows the conditional jump, and
the code after the body comes later. This means that the jump is to that post-`if`/`while` code, and therefore the
condition is the opposite of what you might expect in a high-level language. In e.g. Python, the condition is for
whether or not to execute the body, but here the condition is for whether or not to _not_ execute it.) For loops such as
`while`, there is then an unconditional jump at the end of the body that redirects execution back to the condition,
which is then re-evaluated, followed by another conditional jump instruction that either carries on for another
iteration or exits the loop.

To illustrate, here's a simple if statement:
```
[
    0b00000100, 2,   # [ 0]: PUSH 2
    0b00000100, 2,   # [ 2]: PUSH 2
    0b00000101,      # [ 4]: ADD
    0b00000100, 4,   # [ 5]: PUSH 4
    0b00000111,      # [ 7]: EQ
    0b00000100, 14,  # [ 8]: PUSH 14
    0b00100010,      # [10]: JC
    0b00000100, 21,  # [11]: PUSH '!'
    0b00000110,      # [13]: PRINT
    0b00000100, 46,  # [14]: PUSH '.'
    0b00000110,      # [16]: PRINT
]
```

The above is essentially equivalent to the following Python code:
```python
if 2 + 2 != 4:
    print("!", end="")
print(".", end="")
```

(Note that `end` is an optional argument to `print`, which by default is the newline character `\n`, and is why `print`
normally adds a newline to the end of whatever you give it. We don't want that newline here, so set it to the empty
string to make it just output what we give it directly. Our `PRINT` instruction not only doesn't add a newline, it
prints only a single ASCII character at a time! If the number on the top of the stack is 21, then it pops that,
interprets it as an ASCII character code, and prints the corresponding character, which in this case is an exclamation
mark. You can then use this very basic `PRINT` to implement higher-level print functions that print entire strings - or
other types - with or without newlines.)

In the machine code above, the corresponding assembly code is shown to the right of it, along with the instructions'
addresses (assuming the code is loaded in at address 0, which wouldn't happen in a "real" system, but is fine for our
purposes). For example `PUSH 14` is at address `8`. Speaking of `PUSH 14`, the `14` it's pushing is itself an address,
corresponding to the instruction `PUSH '.'`.

(In our assembly language - and this is often the case - we allow writing the actual characters, e.g. `'.'` or `'!'`,
and have the assembler convert them to their numeric codes, e.g. `46` or `21`.)

This is because `14` is the address that the `JC` (conditional jump) instruction should jump to if the condition
(`2 + 2 == 4`) is true. Our machine encodes booleans as integers in a fairly standard way, which is to say that `False`
is `0` and `True` is anything else. Therefore what `JC` will do is to pop the top two items off the stack, check whether
the condition - which was the second item on the stack, i.e. the one `PUSH`ed first - is non-zero, and if that's the
case, then it will jump to the given address - which was the top item, i.e. the one `PUSH`ed second. If not, then it
will simply carry on to the next instruction, which is the `PUSH '!'` at address 11.

Now, this works, but it's very awkward to have to manually calculate that the next instruction after the if statement is
at address 14, and to remember to update that if it changes, for example because you added an extra instruction before
then, e.g. to the body of the if statement.

The solution is to write it in assembly using labels. This means that we could write the above program as:
```
    PUSH 2
    PUSH 2
    ADD
    PUSH 4
    EQ
    PUSH done
    JC
    PUSH '!'
    PRINT
done:
    PUSH '.'
    PRINT
```

Here we've labelled the first instruction after the if statement (the one executed once it's done) as "done". This means
that we can use it to write `PUSH done` rather than `PUSH 14`. The advantage of this is that we don't need to
calculate - nor recalculate - the address of that instruction.

Before we move on to talking about the point of our linker, here are a couple of extra examples to help show how we can
use labels and jump instructions to implement standard control structures.

The above was for a simple `if` statement, and the following is for an `if/else` statement:
```
    PUSH 1
    PUSH 2
    ADD
    PUSH 3
    NE
    PUSH else
    JC
    PUSH 'y'
    PRINT
    PUSH done
    J
else:
    PUSH 'n'
    PRINT
done:
    PUSH '.'
    PRINT
```

This is equivalent to
```python
if 1 + 2 == 3:
    print("y", end="")
else:
    print("n", end="")
print(".", end="")
```
and will print `y.`.

Note that `J` is an unconditional jump, which simply pops the top item off the stack, interprets it as an address, and
jumps there.

The following is an example of a `while` loop:
```
    PUSH 0
loop:
    DUPE
    PUSH 4
    GE
    PUSH done
    JC
    DUPE
    PUSH '0'
    ADD
    PRINT
    PUSH 1
    ADD
    PUSH loop
    J
done:
    PUSH '.'
    PRINT
```

This is equivalent to
```python
i = 0
while i < 4:
    print(i, end="")
    i += 1
print(".", end="")
```
or
```python
for i in range(4):
    print(i, end="")
print(".", end="")
```
and will print `0123.`.

Note that to print the numbers as characters representing those numbers, we use them as an offset to the character
`'0'`, taking advantage of the fact that in ASCII digits' character codes are consecutive and in order. (The character
code for `'0'` is `48`, `'1'` is `49`, `'2'` is `50`, ... `'9'` is `57`, so if we do `48 + d`, we get the character code
for the digit `d`.)

One more thing to briefly mention: Function calls, and `return`ing from functions, are also implemented using jumps.
Usually though, we don't use `J` or `JC`, but rather slightly more specialised instructions, which we've here called
`CALL` and `RET`. (This is pretty standard, though we've also included conditional versions `CALLC` and `RETC`, and
these aren't always included.)

`CALL` works much like `J`, but before jumping to the given address, it pushes the instruction pointer - the address of
the next instruction to be executed - onto a second stack, the return address stack.

`RET` then works by popping the top item off the return address stack, and jumping to that address.

(`CALLC` and `RETC` do the same thing, but take a condition, and only call/return if the condition is true.)

An example is worth a thousand words:
```
    PUSH 0
    PUSH 1
    PUSH 2
    PUSH 3
    PUSH add4
    CALL
    PUSH '0'
    ADD
    PRINT
    EXIT
add3:
    ADD
    ADD
    RET
add4:
    PUSH add3
    CALL
    ADD
    RET
```

The above is equivalent to
```python
def add3(a: int, b: int, c: int) -> int:
    return a + b + c

def add4(a: int, b: int, c: int, d: int) -> int:
    return a + add3(b, c, d)

print(add4(0, 1, 2, 3), end="")
```
and prints `6`.

Now, with all of that context out of the way, let's talk about the point of this exercise: linkers!

As mentioned earlier:

> An assembler is essentially an assembly language compiler: You give it assembly code, and it gives you the equivalent
> machine code.
>
> Well, sort of. What it actually gives you is "object code", which is partway from assembly code to machine code, but
> not necessarily all the way there quite yet. To finish the job, and go from object code to machine code, you need a
> linker.

The "object code" we were talking about, is "almost" machine code, except for the fact that it hasn't yet calculated the
labels' addresses. Therefore, for our purposes, object code will look like this:
```
[
    0b00000100, 0,       # [ 0]:     PUSH 0
    0b00000100, 1,       # [ 2]:     PUSH 1
    0b00000100, 1,       # [ 4]:     PUSH 2
    0b00000100, 1,       # [ 6]:     PUSH 3
    0b00000100, "add4",  # [ 8]:     PUSH add4
    0b00001010,          # [10]:     CALL
    0b00000100, 48,      # [11]:     PUSH '0'
    0b00000101,          # [13]:     ADD
    0b00000110,          # [14]:     PRINT
    0b00001110,          # [15]:     EXIT
    "add3",              # [16]: add3:
    0b00000101,          # [16]:     ADD
    0b00000101,          # [17]:     ADD
    0b00011010,          # [18]:     RET
    "add4",              # [19]: add4:
    0b00000100, "add3",  # [19]:     PUSH add3
    0b00001010,          # [21]:     CALL
    0b00000101,          # [22]:     ADD
    0b00011010,          # [23]:     RET
]
```

Our linker's job, then, is to calculate the addresses, substitute them in where appropriate, and return:
```
[
    0b00000100, 0,   # [ 0]: PUSH 0
    0b00000100, 1,   # [ 2]: PUSH 1
    0b00000100, 1,   # [ 4]: PUSH 2
    0b00000100, 1,   # [ 6]: PUSH 3
    0b00000100, 19,  # [ 8]: PUSH add4
    0b00001010,      # [10]: CALL
    0b00000100, 48,  # [11]: PUSH '0'
    0b00000101,      # [13]: ADD
    0b00000110,      # [14]: PRINT
    0b00001110,      # [15]: EXIT
    0b00000101,      # [16]: ADD
    0b00000101,      # [17]: ADD
    0b00011010,      # [18]: RET
    0b00000100, 16,  # [19]: PUSH add3
    0b00001010,      # [21]: CALL
    0b00000101,      # [22]: ADD
    0b00011010,      # [23]: RET
]
```

Now, you may be wondering why the assembler can't just do that. The answer is that it could, and some do - in fact most
do to some extent. The reason is that we're not necessarily assembling the entire program all at once, but rather often
we assemble individual pieces and then "link"(!) them all together. Say we were writing a program that used some library
function `foo`. Our assembler would assemble our assembly code program, and leave a placeholder wherever we've
referenced `foo`. When we then link that object code against the library, the linker can figure out the address of `foo`
and thus fill in those placeholders.

By the way, if you're thinking "well, I'm never going to write much assembly, so why do I care?", note that even in
higher-level languages, their compilers often compile only down to object code, and then involve a subsequent linking
step. (For example, if you're writing C and run `clang` or `gcc` to compile your code, they'll output a file with the
extension `.o`, which indicates that it's an object file, i.e. a file containing object code, which you'll then need to
pass to a linker like `lld` or `ld`, along with the object files for all the libraries you're using, to get a proper
executable that you can actually run.)

To use the previous example again, if we had:
```python
add3 = """
add3:
    ADD
    ADD
    RET
"""

add4 = """
add4:
    PUSH add3
    CALL
    ADD
    RET
"""

main = """
    PUSH 0
    PUSH 1
    PUSH 2
    PUSH 3
    PUSH add4
    CALL
    PUSH '0'
    ADD
    PRINT
    EXIT
"""
```

We could run:
```
main_object_code = assemble(main)
add3_object_code = assemble(add3)
add4_object_code = assemble(add4)

object_codes = Queue()
object_codes.enqueue(main_object_code)
object_codes.enqueue(add3_object_code)
object_codes.enqueue(add4_object_code)

program = link(object_codes)
```

Or, for convenience (when we're assembling all the components at once, rather than linking against e.g. precompiled
libraries):
```
source_codes = Queue()
source_codes.enqueue(main)
source_codes.enqueue(add3)
source_codes.enqueue(add4)

program = assemble_and_link(source_codes)
```

(The idea is, though, that we could have assembled `add3` and `add4` once, ahead of time, and then used them and re-used
them in multiple programs without having to re-assemble them each time.)

The output, `program`, will then be the machine code from earlier, i.e.:
```
[
    0b00000100, 0,   # [ 0]: PUSH 0
    0b00000100, 1,   # [ 2]: PUSH 1
    0b00000100, 1,   # [ 4]: PUSH 2
    0b00000100, 1,   # [ 6]: PUSH 3
    0b00000100, 19,  # [ 8]: PUSH add4
    0b00001010,      # [10]: CALL
    0b00000100, 48,  # [11]: PUSH '0'
    0b00000101,      # [13]: ADD
    0b00000110,      # [14]: PRINT
    0b00001110,      # [15]: EXIT
    0b00000101,      # [16]: ADD
    0b00000101,      # [17]: ADD
    0b00011010,      # [18]: RET
    0b00000100, 16,  # [19]: PUSH add3
    0b00001010,      # [21]: CALL
    0b00000101,      # [22]: ADD
    0b00011010,      # [23]: RET
]
```

Right! Hopefully that very brief, yet admittedly lengthy, background is enough to understand what the code in
`exercise.py` is doing. The point, ostensibly at least, is that for the linker to resolve the label addresses, it uses
a map! (In the interest of transparency: the other point is that it might inspire you to learn more about assembly
programming and the way computers really work, and/or create your own compilers etc.)

As you will see in the `link` function, it does this by iterating over all the object code twice (we would thus call it
a two-pass linker). In the first pass, it finds all the labels and calculates their addresses, building up a
`Map[str, int]` where labels are keys and their addresses the associated values. (It also removes the labels from the
object code, as in our representation they're still interspersed throughout the code itself.) In the second pass, it
goes through again, this time finding all the places those labels are referenced as arguments to `PUSH` instructions,
and replaces them with the actual addresses. It then concatenates all the results of this together, and _voilà_! It
returns a machine code - well, bytecode (tomato tomato) - program that we can give to our virtual machine from lab 3
to execute!

(If you enjoy this sort of thing, there are a few fun little example functions written in this made-up assembly
language that you might like to try to understand. Better, you might like to write your own, or create your own
instruction set!)
