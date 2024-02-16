from argparse import ArgumentParser, ArgumentTypeError

from lib.labs import Labs, Component


def _component(arg: str) -> Component:
    labs = Labs.instance()
    if arg[0].isdigit():
        try:
            week = int(arg)
            lab = labs[week]
            return lab.core
        except ValueError:
            week = int(arg[:-1])
            lab = labs[week]
            match arg[-1]:
                case "*":
                    return lab
                case "+":
                    return lab.plus
    elif arg == "*":
        return labs
    else:
        return labs.exercise(arg)
    raise ArgumentTypeError(f"'{arg}' does not identify a component")


def _interface(arg: str) -> str:
    interface = arg.lower()
    if interface in ["cli", "tui"]:
        return interface
    raise ArgumentTypeError(f"'{arg} is not an available interface")


class DSAArgumentParser(ArgumentParser):
    def __init__(self) -> None:
        super().__init__(prog="python labs", description="Data Structures & Algorithms (Labs)")
        self.add_argument(
            "component",
            type=_component,
            nargs="?",
            default=None,
            help="the component (lab/exercise) to test (e.g. * for everything, 2* for lab 2, 2 for lab 2's core exercises, "
            "2+ for its plus exercises, singly_linked_list for the singly-linked lists exercise)",
        )
        self.add_argument(
            "-i",
            "--interface",
            type=_interface,
            dest="interface",
            default="tui",
            help="which interface to use (either cli or tui)",
        )
        self.add_argument(
            "-min",
            "--min-time-ms",
            type=int,
            dest="min_time_ms",
            default=25,
            help="the minimum number of milliseconds each test should run cases for before declaring success (default 25)",
        )
        self.add_argument(
            "-max",
            "--max-time-ms",
            type=int,
            dest="max_time_ms",
            default=None,
            help="the maximum number of milliseconds each test case should run for before assuming an infinite loop (default None)",
        )
