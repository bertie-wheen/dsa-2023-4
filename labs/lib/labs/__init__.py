from collections.abc import Iterator
from importlib import import_module
from typing import Optional, TypeAlias

import lib.test
import lib.test.suite


class Labs:
    _instance: Optional["Labs"] = None

    _labs: list["Lab"]

    @staticmethod
    def instance() -> "Labs":
        if Labs._instance is None:
            Labs._instance = Labs(
                (
                    (
                        "maths",
                        "player",
                        "pair",
                    ),
                    (),
                ),
                (
                    (
                        "singly_linked_list",
                        "doubly_linked_list",
                        "static_array_list",
                    ),
                    (
                        "logger",
                        "character_generator",
                    ),
                ),
                (
                    (
                        "dynamic_array_list",
                        "circular_dynamic_array_list",
                        "linked_stack",
                        "array_stack",
                        "linked_queue",
                        "array_queue",
                    ),
                    (
                        "linked_deque",
                        "array_deque",
                        "shunting_yard",
                        "virtual_stack_machine",
                    ),
                ),
                (
                    (
                        "selection_sort",
                        "insertion_sort",
                        "merge_sort",
                        "binary_search",
                        "unsorted_array_map",
                        "sorted_array_map",
                    ),
                    (
                        "scrabble",
                        "memoization",
                    ),
                ),
                (
                    (
                        "hash_function",
                        "chaining_hash_map",
                        "probing_hash_map",
                    ),
                    (
                        "ecs",
                        "linker",
                    ),
                ),
            )
        return Labs._instance

    def __init__(self, *labs) -> None:
        self._labs = [Lab(self, week, core, plus) for week, (core, plus) in enumerate(labs, start=1)]

    @property
    def full_id(self) -> str:
        return "labs"

    @property
    def tests(self) -> "lib.test.suite.TestSuite":
        return lib.test.suite.TestSuite(
            (f"{lab.id}.{test_name}", test) for lab in self for test_name, test in lab.tests
        )

    @property
    def name(self) -> str:
        return "Labs"

    @property
    def full_name(self) -> str:
        return "Overall"

    def __getitem__(self, week: int) -> "Lab":
        return self._labs[week - 1]

    def __len__(self) -> int:
        return len(self._labs)

    def __iter__(self) -> Iterator["Lab"]:
        return iter(self._labs)

    # def exercises(self, exercises_full_id: str) -> LabExercises:
    #     for lab in self:
    #         for exercises in lab:
    #             if exercises.full_id == exercises_full_id:
    #                 return exercises
    #     raise KeyError

    def exercise(self, exercise_id: str) -> "Exercise":
        for lab in self:
            for exercises in lab:
                for exercise in exercises:
                    if exercise.id == exercise_id:
                        return exercise
        raise KeyError

    def test(self, test_full_id: str) -> "lib.test.Test":
        for full_id, test in self.tests:
            if full_id == test_full_id:
                return test
        raise KeyError


class Lab:
    _labs: Labs
    _week: int
    _core: "LabExercises"
    _plus: "LabExercises"

    def __init__(self, labs: Labs, week: int, core, plus) -> None:
        self._labs = labs
        self._week = week
        self._core = LabExercises(self, True, *core)
        self._plus = LabExercises(self, False, *plus)

    @property
    def week(self) -> int:
        return self._week

    @property
    def name(self) -> str:
        return f"Lab {self.week}"

    @property
    def full_name(self) -> str:
        return self.name

    @property
    def id(self) -> str:
        return f"lab{self.week}"

    @property
    def full_id(self) -> str:
        return f"{self._labs.full_id}.{self.id}"

    @property
    def core(self) -> "LabExercises":
        return self._core

    @property
    def plus(self) -> "LabExercises":
        return self._plus

    @property
    def tests(self) -> "lib.test.suite.TestSuite":
        return lib.test.suite.TestSuite(
            (f"{exercises.id}.{test_name}", test) for exercises in self for test_name, test in exercises.tests
        )

    def __len__(self):
        return len(self._core) + len(self._plus)

    def __iter__(self) -> Iterator["LabExercises"]:
        yield self._core
        yield self._plus


class LabExercises:
    _lab: Lab
    _is_core: bool
    _exercises: list["Exercise"]

    def __init__(self, lab: Lab, is_core: bool, *exercises: str) -> None:
        self._lab = lab
        self._is_core = is_core
        self._exercises = [Exercise(self, exercise) for exercise in exercises]

    @property
    def is_core(self) -> bool:
        return self._is_core

    @property
    def lab(self) -> str:
        return self._lab

    @property
    def id(self) -> str:
        return "core" if self.is_core else "plus"

    @property
    def full_id(self) -> str:
        return f"{self._lab.full_id}.{self.id}"

    @property
    def name(self) -> str:
        return "Core" if self.is_core else "Plus"

    @property
    def full_name(self) -> str:
        return f"{self.lab.name} ({self.name})"

    @property
    def tests(self) -> "lib.test.suite.TestSuite":
        return lib.test.suite.TestSuite(
            (f"{exercise.id}.{test_name}", test) for exercise in self for test_name, test in exercise.tests
        )

    def __len__(self):
        return sum(map(len, self._exercises))

    def __iter__(self):
        return iter(self._exercises)


class Exercise:
    _exercises: LabExercises
    _name: str
    _tests: Optional["lib.test.suite.TestSuite"]

    def __init__(self, exercises: LabExercises, name) -> None:
        self._exercises = exercises
        self._name = name
        self._tests = None

    @property
    def exercises(self) -> LabExercises:
        return self._exercises

    @property
    def id(self) -> str:
        return self._name

    @property
    def full_id(self) -> str:
        return f"{self._exercises.full_id}.{self.id}"

    @property
    def name(self) -> str:
        return self.id

    @property
    def full_name(self) -> str:
        exercises = self.exercises
        lab = exercises.lab
        return f"{lab.name} ({exercises.name}): {self.name} exercise"

    @property
    def tests_full_id(self) -> str:
        return f"lib.{self.full_id}.tests"

    @property
    def tests(self) -> "lib.test.suite.TestSuite":
        if self._tests is None:
            try:
                tests_module = import_module(self.tests_full_id)
                self._tests = lib.test.suite.TestSuite(
                    (test.id, test) for test in tests_module.__dict__.values() if type(test) is lib.test.Test
                )
            except ModuleNotFoundError:
                self._tests = lib.test.suite.TestSuite(())
        return self._tests


Component: TypeAlias = Labs | Lab | LabExercises | Exercise
