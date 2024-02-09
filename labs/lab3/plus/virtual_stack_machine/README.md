# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/README.md))

### [Virtual Stack Machines](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/virtual_stack_machine/README.md)
```shell
python labs virtual_stack_machine
```

In this exercise we'll implement a simple emulator, or virtual machine.

The type of machine we'll be emulating is known as a [stack machine](https://en.wikipedia.org/wiki/Stack_machine),
and stack machines - as you might imagine - are a good example of something you can do with stacks.

Our stack machine, being implemented in software rather than hardware, will be what's known as a
[virtual stack machine](https://en.wikipedia.org/wiki/Stack_machine#Virtual_stack_machines).
(Though you could get away with simply calling it a virtual machine, or a stack machine.)

Machines have what's called an instruction set, which is the set of instructions they support. A program written in
["machine code"](https://en.wikipedia.org/wiki/Machine_code) is written in terms of these instructions.

Machine code is the code that the machine actually understands, and is the "lowest-level" language. Because most
programmers find it too troublesome to write in directly (for one reason or another), people have created various
"higher"-level languages - such as Python or Java. Programs in these higher-level languages are either compiled "down"
into machine code so that the machine can run it directly, or are interpreted by another program (an "interpreter"), a
sort of middleman that runs it indirectly.

In a way, emulators like the one in this exercise are interpreters for machine code. You may wonder of the utility of
such a thing - if it's already machine code, then why not just run it directly? Because machine code isn't one thing:
It varies between machines - the code that one understands, another may not.

The machine code of this exercise is, in fact, not understood by _any_ machine. Or at least, not by any physical
machine. The instruction set we're using is made up for these labs - there is no printed circuit board (PCB) that
implements it, and it wasn't created with a physical PCB in mind. Rather, it was made with the intention of being run by
a virtual machine. In cases such as this, rather than talking about machine code, we call the instruction set and
programs written using it ["bytecode"](https://en.wikipedia.org/wiki/Bytecode).

(We're not going to go into why this is, and will gloss over many other things too in this, and in the related exercises
next lab, but if you're interested in this sort of thing then you should look forward to G5035 "Compilers and Computer
Architecture" in the autumn.)

The reason why our machine is called a "stack machine" is because most of its instructions operate on a stack. This is
in contrast to many instruction sets whose instructions whose operands are taken from - and results are put into -
either registers or main memory.

As an example of how this works, here's what some bytecode for our virtual machine might look like:
```
    PUSH 1
    PUSH 2
    ADD
```

This is essentially equivalent to writing $1 + 2$, and after execution will result in the value $3$ being on top of the
stack. The first `PUSH 1` pushes $1$ onto the top of the stack, `PUSH 2` pushes $2$ on top of that, and then `ADD` pops
the top two values off the stack, adds them, and pushes the result, $3$, back onto the stack, to be used by further
instructions. For example, you could write:
```
    PUSH 1
    PUSH 2
    ADD
    PUSH 4
    MUL
```
After the first three instructions, $3$ is on top of the stack. `PUSH 4` pushes $4$ on top of that, and `MUL` pops them
off, multiplies them, and pushes their product ($12$) back onto it.

(You may have noticed that it essentially works in reverse-Polish / postfix form: The above is equivalent to
`(1 + 2) * 4`, which is written using postfix notation as `1 2 + 4 *`.)

Before describing more sorts of instructions, we should note that bytecode / machine code is really just a sequence of
numbers, and what's written above is an example of "assembly" language. Assembly, like machine code, is not one specific
language, but rather describes a sort of language. Though machine code is the lowest-level language, assembly is
essentially the next lowest. It's very simple, and usually maps pretty directly to machine code. It's pretty much just a
text-based, human-readable version of machine code. Compilers for assembly languages, which convert assembly into
machine code, are called "assemblers", and we'll write one in the next lab's plus exercises.

The instructions have what are called "opcodes" (from "operation codes"), which are integers - or really bit sequences -
that identify the instruction. For example, in our instruction set `PUSH` has the opcode `0b00000100`. (This `0b...`
syntax is how you write binary numbers in Python and a number of other languages. It just means to interpret everything
after the `0b` as written in base-2, i.e. binary. So `0b00000100` is the same as writing `4`. The reason we do it this
way is that, though we won't take particular advantage of it, instructions that are similar in various ways will often
have similar opcodes, in that they'll have one or more of their bits set the same.)

Usually machine code instructions will encode not just the opcode, but the operands. For a few reasons (such as because
Python's integers are unbounded, and more importantly because we don't want to deal with bit-shifting / -masking that
would distract from the exercise), our bytecode isn't like this. Instead, for our purposes, bytecode is an `Array[int]`,
with the `int`s being either opcodes or operands. (Incidentally, `PUSH` is the only instruction that directly takes an
argument, the others all take theirs from the stack.)

So, the example
```
    PUSH 1
    PUSH 2
    ADD
    PUSH 4
    MUL
```
would be assembled to
```
[
    0b00000100, 1,
    0b00000100, 2,
    0b00000101,
    0b00000100, 4,
    0b00010101,
]
```
as the opcodes for `PUSH`, `ADD` and `MUL` are `0b00000100`, `0b00000101` and `0b00010101`.

We'd then load the VM with this bytecode as its memory, and thus indices into the array will be memory addresses. The VM
will keep track of the address of the next instruction to be executed, in a variable commonly called either the
"instruction pointer" (IP), or the "program counter" (PC).

When running, the VM processes one instruction at a time. It first fetches the next instruction by going to the address
in memory that the instruction pointer (which it then increments) is pointing at, which in the example above (with the
instruction pointer initially `0`) would initially be `0b00000100`. It then decodes that instruction, in that it figures
out from the opcode which instruction it's supposed to execute. Normally it then executes that instruction, but if the
instruction turns out to be a `PUSH` it additionally fetches the value to be pushed, before pushing it onto its internal
stack. It keeps doing this until the instruction pointer no longer points to a valid address, either because it executed
the last instruction and thus incremented the IP past the end of memory, or because it executed an `EXIT` instruction
(which sets the IP to `-1`).

As well as arithmetic operations, there are various other types of instructions. The ones we're most interested in here
are the stack manipulation instructions. We've discussed `PUSH`, but there's also `POP`, `DUPE`, `MOVU`, `MOVD` and
`SWAP`.

Only `POP`, which pops the top item off the stack, maps directly onto one of our stack operations from the core content.

`DUPE`, the simplest of the others, duplicates the top item on the stack. That is, it pushes the same thing as
whatever's currently on top of the stack onto the stack.

`MOVU` ("move up") moves an item further down in the stack up to the top. As an example, assume the stack starts off
like this:
```
2 (top)
2
3
5
7
```

First `MOVU` pops the top item off, which it interprets as the index of the item to be moved up - in this case, `2`. The
stack then looks like this:
```
2 (top)
3
5
7
```

The item at index `2` is then `5`, and so when the `MOVU` instruction is done the stack looks like this:
```
5 (top)
2
3
7
```

When you are implementing this operation, you should use an additional temporary stack. The process in this case would
be as follows:

Let's start at the point when we've popped the index off, seen that it's `2`, and the stacks are like this:
```
Primary     Temporary
=======     =========

2 (top)
3
5
7           (empty)
```

Twice (because the index is `2`), pop the top item off the stack and push it onto the temporary stack, so that then we
have:
```
Primary     Temporary
=======     =========

5 (top)     3 (top)
7           2
```

Pop the next item off, which is the item to be moved up to the top, and store it in a temporary variable. The stacks are
then:
```
Primary     Temporary
=======     =========

            3 (top)
7 (top)     2
```

Now, pop the items off the temporary stack and push them back onto the main one, to get:
```
Primary     Temporary
=======     =========

2 (top)
3
7           (empty)
```

Then simply push the moving item onto the top of the stack:
```
Primary     Temporary
=======     =========

5 (top)
2
3
7           (empty)
```

Done!

You should hopefully be able to generalise this for any index (i.e. not just `2`).

`MOVD` ("move down") is similar, but moves the top item down to a specified index within the stack.

An example should suffice to communicate the idea. Given the same initial stack:
```
2 (top)
2
3
5
7
```

Then executing `MOVD` would result in:
```
3 (top)
5
2
7
```

The implementation will be similar to `MOVU` - not exactly the same, obviously, but it involves using a temporary stack
in much the same way.

`SWAP` is somewhat redundant, as it's the same as either
```
    PUSH 1
    MOVU
```
or
```
    PUSH 1
    MOVD
```

We include it because it's used relatively frequently, and having a dedicated `SWAP` instruction is both more convenient
and more efficient. Not only does the VM have to fetch, decode and execute only one instruction, but its implementation
need not create a temporary stack - it would only ever push one item onto it, and therefore can make do with a simple
temporary variable.

There are other instructions, and we'll particularly talk more about the "jump" instructions
(`J`/`JC`/`CALL`/`CALLC`/`RET`/`RETC`) in the assembler exercise next lab, but we'll leave this there as all you're
required to implement are `DUPE`, `MOVU`, `MOVD` and `SWAP`. Good luck!
