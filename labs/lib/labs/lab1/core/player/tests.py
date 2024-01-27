from itertools import product

from lib.test import Test, cases

from lab1.core.player.exercise import Player


positives = [
    1,
    2,
    10,
    907,
    1995,
    2004,
    9001,
]
non_negatives = [0, *positives]
integers = [0, *positives, *map(lambda n: -n, positives)]


@Test
@cases(*non_negatives)
def get_xp_after_init(xp):
    yield xp
    player = Player(xp=xp)
    yield player.get_xp()


@Test
@cases(*product(non_negatives, positives))
def get_xp_after_gain(initial, gained):
    yield initial + gained
    player = Player(xp=initial)
    player.gain(gained)
    yield player.get_xp()


@Test
@cases(*product(integers, repeat=2))
def get_y_after_init(x, y):
    yield y
    player = Player(position=(x, y))
    yield player.get_y()


@Test
@cases(*product(integers, repeat=4))
def get_y_after_move(initial_x, initial_y, delta_x, delta_y):
    yield initial_y + delta_y
    player = Player(position=(initial_x, initial_y))
    player.move(delta_x, delta_y)
    yield player.get_y()
