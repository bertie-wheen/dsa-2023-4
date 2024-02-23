"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Scrabble Solution
"""

from lib.iterator import iterator

from lab4.core.sorted_array_map import SortedArrayMap

_letter_values = SortedArrayMap[str, int](
    iterator(
        ("A", 1),
        ("B", 3),
        ("C", 3),
        ("D", 2),
        ("E", 1),
        ("F", 4),
        ("G", 2),
        ("H", 4),
        ("I", 1),
        ("J", 8),
        ("K", 5),
        ("L", 1),
        ("M", 3),
        ("N", 1),
        ("O", 1),
        ("P", 3),
        ("Q", 10),
        ("R", 1),
        ("S", 1),
        ("T", 1),
        ("U", 1),
        ("V", 4),
        ("W", 4),
        ("X", 8),
        ("Y", 4),
        ("Z", 10),
    )
)


def get_tile_value(tile: str) -> int:
    """
    Get the value of the given Scrabble tile.

    If ``tile`` is not a letter in the Latin alphabet, assume it's blank tile and return 0.

    :parameter tile_letter: which letter the tile is
    :returns: the number of points that tile is worth
    """
    if not _letter_values.contains(tile):
        return 0
    return _letter_values.get(tile.upper())


def get_word_standard_value(word: str) -> int:
    """
    Get the standard value (not accounting for score multipliers) of the given word in Scrabble.

    Does not check if the word is valid.

    :parameter word: the word to be played
    :returns: the number of points the word is worth
    """
    word_value = 0
    for letter in word:
        word_value += get_tile_value(letter)
    return word_value
