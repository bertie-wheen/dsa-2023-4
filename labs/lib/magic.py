from typing import Any, Callable, Iterable, Iterator


def to_string(thing: Any) -> str:
    if isinstance(thing, Iterator):
        thing_type = "Iterator"
    else:
        thing_type = type(thing).__name__
    if isinstance(thing, str):
        thing_str = repr(thing)
    elif isinstance(thing, Iterable):
        thing_str = ", ".join(map(to_string, thing))
    elif hasattr(thing, "iterator") and isinstance(thing.iterator, Callable) and isinstance(thing.iterator(), Iterable):
        thing_str = ", ".join(map(to_string, thing.iterator()))
    else:
        thing_str = str(thing)
    return f"{thing_type}{{{thing_str}}}"


def _equal_members(thing_a: Any, thing_b: Any, *members: Iterator[str]) -> bool:
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
    Type = type(thing_a)
    match Type.__name__:
        case "Pair":
            return _equal_members(thing_a, thing_b, "_first", "_second")
        case "Player":
            return _equal_members(thing_a, thing_b, "_xp", "_position")
    return thing_a == thing_b
