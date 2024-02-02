from enum import Enum

from lib.base import Base
from lib.iterator import iterator
from lib.random import generate_bool, generate_index
from lib.type_vars import Item

from lab2.core.static_array_list import StaticArrayList


class Sex(Base, Enum):
    MALE = 0
    FEMALE = 1


neutral_prefixes = StaticArrayList.build(
    iterator(
        "Bold",
        "Cunning",
        "Great",
    )
)

female_prefixes = StaticArrayList.build(
    iterator(
        "Baroness",
        "Countess",
        "Duchess",
        "Lady",
        "Princess",
        "Queen",
        "Shieldmaiden",
    )
)

male_prefixes = StaticArrayList.build(
    iterator(
        "Baron",
        "Count",
        "Duke",
        "King",
        "Lord",
        "Prince",
        "Sir",
    )
)

female_first_names = StaticArrayList.build(
    iterator(
        "Andora",
        "Astrid",
        "Brynhildr",
        "Eir",
        "Embla",
        "Freya",
        "Helga",
        "Ingvild",
        "Thora",
        "Ulvhild",
    )
)

male_first_names = StaticArrayList.build(
    iterator(
        "Agnar",
        "Fenrir",
        "Geir",
        "Harald",
        "Ivar",
        "Ragnar",
        "Rune",
        "Sigurd",
        "Thor",
        "Varg",
    )
)

last_name_firsts = StaticArrayList.build(
    iterator(
        "Dark",
        "Deep",
        "Great",
        "Grim",
        "Half",
        "Iron",
        "Light",
        "Raw",
        "Rough",
        "Storm",
        "Thunder",
    )
)

last_name_lasts = StaticArrayList.build(
    iterator(
        "back",
        "bear",
        "belly",
        "brew",
        "buck",
        "chest",
        "hill",
        "horn",
        "pass",
        "rock",
        "storm",
        "tree",
        "wind",
    )
)

suffixes = StaticArrayList.build(
    iterator(
        " of Ironforge",
        " of Orgrimmar",
        " of Varrock",
        " of the Wilderness",
        " the Adventurous",
        " the Bold",
        " the Courageous",
        " the Great",
        " the Humble",
        " the Questioning",
        " the Strong",
        " the Swift",
        " the Thoughtful",
        " the Undefeated",
        " the Unfazed",
        ", Ducal Court Wizard",
        ", Greatest of the Age",
        ", Siegebreaker",
    )
)


def _generate_item(list: StaticArrayList[Item]) -> Item:
    count = list.get_length()
    index = generate_index(count)
    return list.get_at(index)


def generate_sex() -> Sex:
    if generate_bool():
        return Sex.FEMALE
    return Sex.MALE


def generate_prefix(sex: Sex) -> str:
    if generate_bool():
        return _generate_item(neutral_prefixes)
    match sex:
        case Sex.FEMALE:
            return _generate_item(female_prefixes)
        case Sex.MALE:
            return _generate_item(male_prefixes)


def generate_first_name(sex: Sex) -> str:
    match sex:
        case Sex.FEMALE:
            return _generate_item(female_first_names)
        case Sex.MALE:
            return _generate_item(male_first_names)


def generate_last_name() -> str:
    return _generate_item(last_name_firsts) + _generate_item(last_name_lasts)


def generate_suffix() -> str:
    return _generate_item(suffixes)


def generate_name(sex: Sex) -> str:
    name = ""
    has_prefix_or_suffix = generate_bool()
    has_prefix = has_prefix_or_suffix and generate_bool()
    if has_prefix:
        name += generate_prefix(sex)
        name += " "
    name += generate_first_name(sex)
    name += " "
    name += generate_last_name()
    has_suffix = has_prefix_or_suffix and not has_prefix
    if has_suffix:
        name += generate_suffix()
    return name
