from dataclasses import dataclass


class Even:
    pass


class Odd:
    pass


@dataclass
class EQ:
    value: str | int


@dataclass
class GE:
    value: str | int


@dataclass
class GT:
    value: str | int


@dataclass
class LE:
    value: str | int


@dataclass
class LT:
    value: str | int
