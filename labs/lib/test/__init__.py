from collections.abc import Callable
from typing import Optional

import lib.labs
from lib.test.annotations import *
from lib.test.parameters import TestParameters
from lib.test.source_code import TestSourceCode
from lib.magic import to_repr


class Test:
    _full_id: Optional[str]
    _func: Callable
    _parameters: Optional[TestParameters]
    _source_code: Optional[TestSourceCode]

    def __init__(self, func: Callable) -> None:
        self._full_id = None
        self._func = func
        self._parameters = None
        self._source_code = None

    @property
    def id(self) -> str:
        return self._func.__name__

    @property
    def full_id(self) -> str:
        if self._full_id is None:
            labs = lib.labs.Labs.instance()
            for full_id, test in labs.tests:
                if test is self:
                    self._full_id = full_id
                    break
            assert self._full_id is not None
        return self._full_id

    @property
    def parameters(self) -> TestParameters:
        if self._parameters is None:
            self._parameters = TestParameters(self._func)
        return self._parameters

    @property
    def source_code(self) -> TestSourceCode:
        if self._source_code is None:
            self._source_code = TestSourceCode(self._func)
        return self._source_code

    def preamble(self, case: tuple) -> str:
        return "\n".join(
            f"{parameter} = {to_repr(argument)}" for parameter, argument in zip(self.parameters.names, case)
        )

    def __call__(self, case: tuple):
        return self._func(*case)
