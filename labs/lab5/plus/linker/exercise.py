"""
Data Structures & Algorithms

Lab 5: Hash Maps

Linkers Exercise
"""

from lib.array import Array
from lib.errors import EmptyCollectionError
from lib.string import split_on_whitespace

from lab3.core.linked_queue import LinkedQueue as Queue
from lab3.plus.virtual_stack_machine import Opcode
from lab5.core.chaining_hash_map import ChainingHashMap as Map


def assemble(source_code: str) -> Array[int | str]:
    """
    Convert the given assembly code to object code.

    :parameter source_code: assembly code
    :returns: object code
    :raises ValueError: if an instruction is unknown or is a ``PUSH`` with no argument
    """
    object_code = Queue[int | str]()
    source_items = Queue.build(split_on_whitespace(source_code))
    while not source_items.is_empty():
        source_item = source_items.dequeue()
        if source_item.endswith(":"):
            object_code.enqueue(source_item.removesuffix(":").lower())
        else:
            try:
                opcode = Opcode[source_item.upper()]
            except KeyError:
                raise ValueError  # unknown instruction
            object_code.enqueue(opcode.value)
            if opcode is Opcode.PUSH:
                try:
                    argument = source_items.dequeue()
                except EmptyCollectionError:
                    raise ValueError  # push with no argument
                try:
                    object_code.enqueue(int(argument))
                except ValueError:
                    if argument.startswith("'") and argument.endswith("'"):
                        match argument.removeprefix("'").removesuffix("'").lower():
                            case r"\n":
                                object_code.enqueue(ord("\n"))
                            case char:
                                object_code.enqueue(ord(char))
                    else:
                        object_code.enqueue(argument)
    return Array.build(object_code.iterator())


def link(object_codes: Queue[Array[int | str]]) -> Array[int]:
    """
    Link the given object codes into one machine code program.

    :parameter object_codes: zero or more object codes
    :returns: machine code
    :raises ValueError: if a label is a duplicate (defined twice) or unknown (referenced but not defined)
    """
    label_addresses = Map[str, int]()
    current_address = 0
    for object_code in object_codes.iterator():
        object_index = 0
        object_length = object_code.get_length()
        while object_index < object_length:
            match object_code.get_at(object_index):
                case str(object_code_label):
                    if label_addresses.contains(object_code_label):
                        raise ValueError(f"duplicate label {object_code_label}")
                    label_addresses.insert(object_code_label, current_address)
                    object_index += 1
                case Opcode.PUSH.value:
                    current_address += 2
                    object_index += 2
                case _:
                    current_address += 1
                    object_index += 1
    machine_code = Queue[int]()
    for object_code in object_codes.iterator():
        object_index = 0
        object_length = object_code.get_length()
        while object_index < object_length:
            opcode = object_code.get_at(object_index)
            object_index += 1
            if type(opcode) is str:
                continue
            machine_code.enqueue(opcode)
            if opcode == Opcode.PUSH.value:
                argument = object_code.get_at(object_index)
                object_index += 1
                match argument:
                    case str(label):
                        if not label_addresses.contains(label):
                            raise ValueError(f"unknown label {label}")
                        address = label_addresses.get(label)
                        machine_code.enqueue(address)
                    case int(value):
                        machine_code.enqueue(value)
    return Array.build(machine_code.iterator())


def assemble_and_link(source_codes: Queue[str]) -> Array[int]:
    object_codes = Queue()
    for source_code in source_codes.iterator():
        object_code = assemble(source_code)
        object_codes.enqueue(object_code)
    return link(object_codes)


# I: ... n
# O: ...
print_int = """
print_int:
    empty
    retc
    push 0
    ge
    push print_int__nonneg
    push '-'
    neg
print_int__nonneg:
    dupe
    push 10
    mod
    push '0'
    add
    print
    push 0
    eq
    retc
    push 10
    div
    push print_int__nonneg
    j
"""


# I: ... 0 c_{n-1} ... c_0
# O: ...
print_str = """
print_str:
    empty
    retc
    dupe
    push 0
    eq
    retc
    print
    push print_str
    j
"""


# I: ... thing print_thing
# O: ...
print_line = r"""
print_line:
    call
    push '\n'
    print
    ret
"""


# I: ... n
# O: ...
print_int_line = """
print_int_line:
    push print_str
    push print_line
    call
    ret
"""


# I: ... 0 c_{n-1} ... c_0
# O: ...
print_str_line = """
print_str_line:
    push print_str
    push print_line
    call
    ret
"""


# I: ... n
# O: ... 0 c_{n-1} ... c_0
int_to_str = """
int_to_str:
    empty
    retc
    push 0
    swap
    dupe
    push 0
    ge
    dupe
    push 2
    movd
    push int_to_str__loop
    jc
    neg
int_to_str__loop:
    dupe
    push 10
    mod
    push '0'
    add
    push 2
    movd
    push 10
    div
    dupe
    push 0
    eq
    push int_to_str__loop_done
    jc
    push int_to_str__loop
    j
int_to_str__loop_done:
    pop
    push int_to_str__done
    jc
    push '-'
int_to_str__done:
    ret
"""

# I: ... n
# O: ...
print_int_2 = """
print_int:
    push int_to_str
    call
    push print_str
    call
    ret
"""

# I: ... i_{n-1} ... i_0 n
# O: ...
pop_n = """
pop_n:
    dupe
    push 0
    le
    push pop_n__done
    jc
    swap
    pop
    push 1
    sub
    push pop_n
    j
pop_n__done:
    pop
    ret
"""

# I: ... i ... n
# O: ... i ... i
dupe_n = """
dupe_n:
    push 1
    add
    dupe
    movu
    dupe
    push 2
    movu
    movd
    ret
"""

# I: ... start stop step func(index)
# O: ...
for_range = """
for_range:
    push 3
    movu
for_range__loop:
    dupe
    push 4
    push dupe_n
    call
    ge
    push for_range__done
    jc
    dupe
    push 2
    push dupe_n
    call
    call
    push 2
    push dupe_n
    call
    add
    push for_range__loop
    j
for_range__done:
    push 4
    push pop_n
    call
    ret
"""

# I: ... n f(i)
# O: ...
call_n = """
call_n:
    push 0
    push 2
    movd
    push 1
    push 1
    movd
    push for_range
    call
    ret
"""

# I: ... start stop step
# O: ...
print_range = """
print_range:
    push print_int_line
    push for_range
    call
    ret
"""
