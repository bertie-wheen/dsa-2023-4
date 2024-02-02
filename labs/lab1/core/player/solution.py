"""
Data Structures & Algorithms

Lab 1: Getting Ready

Players Solution
"""


from lib.base import Base


class Player(Base):
    """
    A player type.

    Space: O(1)
    """

    _xp: int
    _position: tuple[int, int]

    def __init__(self, xp: int = 0, position: tuple[int, int] = (0, 0)) -> None:
        """
        Initialize this player.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter xp: the player's initial xp (default 0)
        :parameter position: the player's initial position (default (0, 0))
        :raises ValueError: if ``xp`` is negative
        """
        if xp < 0:
            raise ValueError
        self._xp = xp
        self._position = position

    def get_xp(self) -> int:
        """
        Get the amount of xp this player has gained.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the total xp
        """
        return self._xp

    def get_level(self) -> int:
        """
        Get this player's level.
        Levels start at 1 and increase linearly with every 1000 xp.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the level
        """
        return 1 + self._xp // 1000

    def get_position(self) -> tuple[int, int]:
        """
        Get the player's position within the game world.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the current position
        """
        return self._position

    def get_x(self) -> int:
        """
        Get the player's x position.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the current x
        """
        x, y = self._position
        return x

    def get_y(self) -> int:
        """
        Get the player's y position.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the current y
        """
        x, y = self._position
        return y

    def gain(self, gained_xp: int) -> bool:
        """
        Make this player gain the given amount of xp.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter gained_xp: the amount of xp to gain
        :returns: ``True`` if by gaining the xp the player's level increased, else ``False``
        :raises ValueError: if ``xp <= 0``
        """
        if gained_xp <= 0:
            raise ValueError
        old_level = self.get_level()
        self._xp += gained_xp
        new_level = self.get_level()
        return new_level != old_level

    def move(self, delta_x: int, delta_y: int) -> None:
        """
        Move this player the given amount.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter delta_x: the change to the x position
        :parameter delta_y: the change to the y position
        """
        old_x, old_y = self._position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        self._position = new_x, new_y
