from argparse import Namespace
import sys
from typing import Optional

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.message import Message
from textual.widgets import Button, Footer, Label, ProgressBar, Rule, Tree
from textual.widgets.tree import TreeNode

from lib.labs import Labs, Lab, LabExercises, Exercise
from lib.test.runner import TestRunner


class Sidebar(ScrollableContainer):
    BINDINGS = [
        ("a", "show_all", "Show all"),
        ("c", "show_core", "Show core"),
        ("l", "show_labs", "Show labs"),
    ]

    def compose(self) -> ComposeResult:
        labs = Labs.instance()
        tree: Tree[dict] = Tree("DSA Labs", data=labs)
        tree.guide_depth = 3
        for lab in labs:
            lab_tree = tree.root.add(lab.name, data=lab)
            for exercises in lab:
                exercises_tree = lab_tree.add(exercises.name, data=exercises)
                for exercise in exercises:
                    exercises_tree.add_leaf(exercise.name, data=exercise)
        tree.root.expand_all()
        yield tree

    def select_node(self, node: TreeNode, toggle: bool = False) -> None:
        if toggle:
            node.toggle()
        node.tree.select_node(node)
        self.on_tree_node_selected(Tree.NodeSelected(node))

    def select_labs(self, toggle: bool = False) -> None:
        tree = self.query_one(Tree)
        self.select_node(tree.root, toggle=toggle)

    def get_lab_node(self, lab: Lab) -> TreeNode:
        tree = self.query_one(Tree)
        for lab_node in tree.root.children:
            if lab_node.data.id == lab.id:
                return lab_node
        raise KeyError

    def select_lab(self, lab: Lab, toggle: bool = False) -> None:
        self.select_node(self.get_lab_node(lab), toggle=toggle)

    def get_exercises_node(self, exercises: LabExercises) -> TreeNode:
        tree = self.query_one(Tree)
        for lab_node in tree.root.children:
            if lab_node.data.id == exercises.lab.id:
                for exercises_node in lab_node.children:
                    if exercises_node.data.id == exercises.id:
                        return exercises_node
        raise KeyError

    def select_exercises(self, exercises: LabExercises, toggle: bool = False) -> None:
        self.select_node(self.get_exercises_node(exercises), toggle=toggle)

    def get_exercise_node(self, exercise: Exercise) -> TreeNode:
        tree = self.query_one(Tree)
        for lab_node in tree.root.children:
            for exercises_node in lab_node.children:
                for exercise_node in exercises_node.children:
                    if exercise_node.data.id == exercise.id:
                        return exercise_node
        raise KeyError

    def select_exercise(self, exercise: Exercise, toggle: bool = False) -> None:
        self.select_node(self.get_exercise_node(exercise), toggle=toggle)

    def get_node(self, full_id: str, root: Optional[TreeNode] = None) -> Optional[TreeNode]:
        if root is None:
            tree = self.query_one(Tree)
            return self.get_node(full_id, root=tree.root)
        if root.data.full_id == full_id:
            return root
        for child in root.children:
            node = self.get_node(full_id, root=child)
            if node is not None:
                return node
        return None

    def select(self, full_id: str, toggle: bool = False) -> TreeNode:
        node = self.get_node(full_id)
        if node is not None:
            self.select_node(node, toggle=toggle)
        return node

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        node = event.node
        node.toggle()
        self.post_message(self.Selected(node))

    def action_show_all(self) -> None:
        root = self.query_one(Tree).root
        root.expand_all()

    def action_show_core(self) -> None:
        root = self.query_one(Tree).root
        root.expand_all()
        for lab_tree in root.children:
            for sub_tree in lab_tree.children:
                if not sub_tree.data.is_core:
                    sub_tree.collapse()

    def action_show_labs(self) -> None:
        root = self.query_one(Tree).root
        root.collapse_all()
        root.expand()
        for lab_tree in root.children:
            lab_tree.expand()

    class Selected(Message):
        _node: TreeNode

        def __init__(self, node: TreeNode) -> None:
            super().__init__()
            self._node = node

        @property
        def node(self) -> TreeNode:
            return self._node


class DSAApp(App):
    CSS_PATH = "app.tcss"
    TITLE = "Data Structures & Algorithms"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    name = ""
    path = []

    args: Namespace

    def __init__(self, args: Namespace) -> None:
        self.args = args
        super().__init__()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar()
            with Container():
                yield Label("Select a lab or exercise from the sidebar", id="title")
                with Container(id="main"):
                    yield ScrollableContainer(id="test-results")
                    with Horizontal(id="runs-info"):
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
                        with Container(id="status-labels"):
                            yield Label("All tests ran successfully!", id="all-success")
                            yield Label("Some tests failed.", id="some-failure")
                        yield Button("Quit", id="quit")
        yield Footer()

    def on_mount(self) -> None:
        sidebar = self.query_one(Sidebar)
        component = self.args.component
        match component:
            case Labs():
                sidebar.select_labs(toggle=True)
            case Lab():
                sidebar.select_lab(component, toggle=True)
            case LabExercises():
                sidebar.select_exercises(component, toggle=True)
            case Exercise():
                sidebar.select_exercise(component, toggle=True)

    def update_title(self, node: TreeNode) -> None:
        self.query_one("#title").update(node.data.full_name)

    async def on_sidebar_selected(self, event: Sidebar.Selected) -> None:
        node = event.node
        self.update_title(node)
        await self.run_tests(node)

    async def run_tests(self, node: TreeNode) -> None:
        self.query_one("#all-success").remove_class("shown")
        self.query_one("#some-failure").remove_class("shown")
        self.query_one("#runs-info").add_class("shown")
        tests = node.data.tests
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
        all_success = True
        runner = TestRunner(self.args.min_time_ms, self.args.max_time_ms)
        for name, test in tests:
            failure_reason = runner.run(test)
            if failure_reason:
                if all_success:
                    all_success = False
                    self.query_one("#some-failure").add_class("shown")
                if not was_first:
                    await test_results.mount(Rule())
                await test_results.mount(Label(name, classes="failure"), Label(failure_reason))
                failure_bar.advance()
            else:
                if not (was_first or was_success):
                    await test_results.mount(Rule())
                await test_results.mount(Label(name, classes="success"))
                success_bar.advance()
            loading_bar.advance()
            was_first = False
            was_success = not failure_reason
        if all_success:
            self.query_one("#all-success").add_class("shown")

    @on(Button.Pressed, "#quit")
    def action_quit(self) -> None:
        sys.exit()
