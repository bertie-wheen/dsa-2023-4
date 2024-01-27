# from . import tests
from lib.resources import labs_dir


def path_for_lab(lab):
    match lab[-1]:
        case "*":
            return ["lab" + lab[:-1]]
        case "+":
            return ["lab" + lab[:-1], "plus"]
        case _:
            return ["lab" + lab, "core"]


def path_for_exercise(exercise):
    for labs_item in labs_dir.iterdir():
        if labs_item.name.startswith("lab"):
            lab = labs_item.name
            for lab_item in labs_item.iterdir():
                if lab_item.name in ["core", "plus"]:
                    core_or_plus = lab_item.name
                    for item in lab_item.iterdir():
                        if item.name == exercise:
                            return [lab, core_or_plus, exercise]
    raise ValueError
