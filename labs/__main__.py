import sys

import lib.cli
import lib.tui
from lib.arg_parser import DSAArgumentParser

parser = DSAArgumentParser()

try:
    args = parser.parse_args()
except KeyError:
    print("ERROR: invalid command-line arguments given\n")
    parser.print_help()
    sys.exit(1)

match args.interface:
    case "cli":
        lib.cli.run(args)
    case "tui":
        lib.tui.run(args)


# from lib.labs.structure import labs
#
# min_time_ms = 800
# max_time_ms = 2_000
# for name, test in labs.exercise("singly_linked_list").tests:
#     if "iterator" in name:
#         print(f"Running {name}...")
#         result = test.run(min_time_ms, max_time_ms)
#         print("Result:")
#         print(result)
#         print()


# from lib.iterator import iterator
# from lab3.plus.virtual_stack_machine import *
# from lab4.plus.assembler import *
#
# main = """
#     push 2
#     push 3
#     push 14
#     push print_range
#     call
#     exit
# """
#
# program = assemble_and_link(
#     iterator(
#         main,
#         for_range,
#         int_to_str,
#         # print_int,
#         print_line,
#         print_int_2,
#         print_int_line,
#         print_range,
#         print_str,
#         dupe_n,
#         pop_n,
#     )
# )
#
# vm = VirtualStackMachine(program, debug=True)
# vm.run()
# print()
# print()
# print("Output:")
# print("".join(vm.output()))
# print("Values:")
# print(", ".join(map(str, vm.values())))
# print("Addresses:")
# print(", ".join(map(str, vm.return_addresses())))
