from importlib import import_module
import sys
from types import ModuleType

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.message import Message
from textual.widgets import Button, Footer, Label, ProgressBar, Rule, Tree

from lib.labs import path_for_lab, path_for_exercise
from lib.resources import lab_numbers, core_exercises, plus_exercises
from lib.test import Test


class Sidebar(ScrollableContainer):
    BINDINGS = [
        ("a", "show_all", "Show all"),
        ("c", "show_core", "Show core"),
        ("l", "show_labs", "Show labs"),
    ]

    def compose(self) -> ComposeResult:
        tree: Tree[dict] = Tree("DSA Labs")
        tree.guide_depth = 3
        for lab_number in lab_numbers:
            lab_tree = tree.root.add(f"Lab {lab_number}", data=f"lab{lab_number}")
            core_tree = lab_tree.add("Core", data="core")
            plus_tree = lab_tree.add("Plus", data="plus")
            for core_exercise in core_exercises(lab_number):
                core_tree.add_leaf(core_exercise, data=core_exercise)
            for plus_exercise in plus_exercises(lab_number):
                plus_tree.add_leaf(plus_exercise, data=plus_exercise)
        tree.root.expand_all()
        yield tree

    def select(self, path: list[str], toggle: bool = False) -> None:
        tree = self.query_one(Tree)
        node = tree.root
        for part in path:
            for child in node.children:
                if part == child.data:
                    node = child
                    break
        if toggle:
            node.toggle()
        tree.select_node(node)
        self.on_tree_node_selected(Tree.NodeSelected(node))

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        node = event.node
        node.toggle()
        nodes = []
        while node.parent is not None:
            nodes.append(node)
            node = node.parent
        nodes.reverse()
        name = [str(node.label) for node in nodes]
        path = [node.data for node in nodes]
        match name:
            case []:
                name = "Overall"
            case [lab_name]:
                name = lab_name
            case [lab_name, core_or_plus]:
                name = f"{lab_name} ({core_or_plus})"
            case [lab_name, core_or_plus, exercise_name]:
                name = f"{lab_name} ({core_or_plus}): {exercise_name} exercise"
            case _:
                assert False
        self.post_message(self.Selected(name, path))

    def action_show_all(self) -> None:
        root = self.query_one(Tree).root
        root.expand_all()

    def action_show_core(self) -> None:
        root = self.query_one(Tree).root
        root.expand_all()
        for lab_tree in root.children:
            for sub_tree in lab_tree.children:
                if sub_tree.data == "plus":
                    sub_tree.collapse()

    def action_show_labs(self) -> None:
        root = self.query_one(Tree).root
        root.collapse_all()
        root.expand()
        for lab_tree in root.children:
            lab_tree.expand()

    class Selected(Message):
        def __init__(self, name: str, path: list[str]) -> None:
            super().__init__()
            self.name = name
            self.path = path


def _get_tests(module: ModuleType) -> dict[str, Test]:
    tests = {}
    for name, thing in module.__dict__.items():
        if isinstance(thing, Test):
            tests[name] = thing
        elif isinstance(thing, ModuleType):
            for test_name, test in _get_tests(thing).items():
                tests[f"{name}.{test_name}"] = test
    return tests


def get_tests(path: list) -> dict[str, Test]:
    module_name = f"lib.labs{''.join('.' + part for part in path)}.tests"
    loaded_module = import_module(module_name)
    return _get_tests(loaded_module)


class DSAApp(App):
    CSS_PATH = "app.tcss"
    TITLE = "Data Structures & Algorithms"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    name = ""
    path = []

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar()
            with Container():
                yield Label("Select a lab or exercise from the sidebar", id="title")
                with Container(id="main"):
                    yield ScrollableContainer(id="test-results")
                    with Horizontal(id="bars-and-buttons"):
                        with Container(id="bars"):
                            with Horizontal(id="loading-bar"):
                                yield Label("Running: ")
                                yield ProgressBar(show_eta=False)
                            with Horizontal(id="success-bar"):
                                yield Label("Success: ")
                                yield ProgressBar(show_eta=False)
                            with Horizontal(id="failure-bar"):
                                yield Label("Failure: ")
                                yield ProgressBar(show_eta=False)
                        yield Button("Quit", id="quit")
        yield Footer()

    def on_mount(self) -> None:
        args = sys.argv[1:]
        if len(args) != 1:
            return
        arg = args[0]
        path = path_for_lab(arg) if arg[0].isdigit() else path_for_exercise(arg)
        self.query_one(Sidebar).select(path, toggle=True)

    async def on_sidebar_selected(self, event: Sidebar.Selected) -> None:
        self.name = event.name
        self.path = event.path
        await self.run_tests()

    async def run_tests(self) -> None:
        self.query_one("#title").update(self.name)
        self.query_one("#bars-and-buttons").add_class("shown")
        tests = get_tests(self.path)
        total = len(tests)
        loading_bar = self.query_one("#loading-bar").query_one(ProgressBar)
        loading_bar.update(progress=0, total=total)
        success_bar = self.query_one("#success-bar").query_one(ProgressBar)
        success_bar.update(progress=0, total=total)
        failure_bar = self.query_one("#failure-bar").query_one(ProgressBar)
        failure_bar.update(progress=0, total=total)
        test_results = self.query_one("#test-results")
        await test_results.remove_children()
        was_first = True
        was_success = False
        for name, test in tests.items():
            failure = test.run()
            is_success = failure is None
            if is_success:
                if not (was_first or was_success):
                    await test_results.mount(Rule())
                await test_results.mount(Label(name, classes="success"))
            else:
                if not was_first:
                    await test_results.mount(Rule())
                await test_results.mount(
                    Label(name, classes="failure"),
                    Label(str(failure)),
                )
            loading_bar.advance()
            if is_success:
                success_bar.advance()
            else:
                failure_bar.advance()
            was_first = False
            was_success = is_success

    @on(Button.Pressed, "#quit")
    def action_quit(self) -> None:
        sys.exit()
