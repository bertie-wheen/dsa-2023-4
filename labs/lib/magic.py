from collections.abc import Callable, Iterable, Iterator
from typing import Any


def to_type_string(thing: Any) -> str:
    if isinstance(thing, Iterator):
        return "Iterator"
    return type(thing).__name__


def members_to_string(thing: Any, *members: str) -> str:
    return ", ".join(f"{member} = {to_typed_string(getattr(thing, member))}" for member in members)


def to_string(thing: Any) -> str:
    if hasattr(thing, "to_string"):
        return thing.to_string()
    match type(thing).__name__:
        case "Player":
            return members_to_string(thing, "_xp", "_position")
    if hasattr(thing, "iterator") and isinstance(thing.iterator, Callable):
        return ", ".join(map(to_typed_string, thing.iterator()))
    if isinstance(thing, str):
        return repr(thing)
    if isinstance(thing, Iterable):
        return ", ".join(map(to_typed_string, thing))
    return str(thing)


def to_typed_string(thing: Any) -> str:
    return f"{to_type_string(thing)}{{{to_string(thing)}}}"


def members_are_equal(thing_a: Any, thing_b: Any, *members: str) -> bool:
    for member in members:
        member_a = getattr(thing_a, member)
        member_b = getattr(thing_b, member)
        if not are_equal(member_a, member_b):
            return False
    return True


def are_equal(thing_a: Any, thing_b: Any) -> bool:
    if isinstance(thing_a, Iterator):
        if not isinstance(thing_b, Iterator):
            return False
        return all(are_equal(a, b) for a, b in zip(thing_a, thing_b))
    if type(thing_a) is not type(thing_b):
        return False
    match type(thing_a).__name__:
        case "Pair":
            return members_are_equal(thing_a, thing_b, "_first", "_second")
        case "Player":
            return members_are_equal(thing_a, thing_b, "_xp", "_position")
    return thing_a == thing_b
