import enum
from collections import namedtuple


class Player(enum.Enum):
    """
    Player entity
    """
    yellow = 1
    red = 2

    @property
    def other(self):
        """
        Switch player
        """
        return Player.yellow if self == Player.red else Player.red


class Point(namedtuple('Point', 'row col')):
    """
    Individual point on board
    Has row and col attributes
    """

    def neighbors(self):
        """
        Returns the vertical and horizontal neighbours of a point
        """
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]
