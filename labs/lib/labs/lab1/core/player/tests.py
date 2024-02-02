from typing import Annotated

from lib.test import Test
from lib.test.annotations import GE, GT

from lab1.core.player.exercise import Player


@Test
def get_xp_after_init(xp: Annotated[int, GE(0)]):
    player = Player(xp=xp)
    yield xp
    yield player.get_xp()


@Test
def get_xp_after_gain(initial: Annotated[int, GE(0)], gained: Annotated[int, GT(0)]):
    player = Player(xp=initial)
    player.gain(gained)
    yield initial + gained
    yield player.get_xp()


@Test
def get_y_after_init(x: int, y: int):
    player = Player(position=(x, y))
    yield y
    yield player.get_y()


@Test
def get_y_after_move(initial_x: int, initial_y: int, delta_x: int, delta_y: int):
    player = Player(position=(initial_x, initial_y))
    player.move(delta_x, delta_y)
    yield initial_y + delta_y
    yield player.get_y()
