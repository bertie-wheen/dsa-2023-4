from pathlib import Path

labs_dir = Path.cwd()
if labs_dir.name != "labs":
    labs_dir /= "labs"


def _lab_numbers():
    for item in labs_dir.iterdir():
        name = item.name
        if name.startswith("lab"):
            yield int(name[len("lab") :])


lab_numbers = sorted(list(_lab_numbers()))


def _lab_dir(lab_number):
    return labs_dir / f"lab{lab_number}"


def _exercises(lab_number, core_or_plus):
    lab_dir = _lab_dir(lab_number) / core_or_plus
    for item in lab_dir.iterdir():
        if not item.is_dir():
            continue
        name = item.name
        if name.startswith(".") or name.startswith("_"):
            continue
        yield name


def core_exercises(lab_number):
    yield from _exercises(lab_number, "core")


def plus_exercises(lab_number):
    yield from _exercises(lab_number, "plus")


resources_dir = labs_dir / "lib" / "resources"
