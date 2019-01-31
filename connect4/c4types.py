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

    def above(self):
        return Point(self.row - 1, self.col)

    def below(self):
        return Point(self.row + 1, self.col)

    def left(self):
        return Point(self.row, self.col - 1)

    def right(self):
        return Point(self.row, self.col + 1)

    def above_left(self):
        return Point(self.row - 1, self.col - 1)

    def below_left(self):
        return Point(self.row + 1, self.col - 1)

    def above_right(self):
        return Point(self.row - 1, self.col + 1)

    def below_right(self):
        return Point(self.row + 1, self.col + 1)

    def neighbors(self):
        """
        Returns the vertical and horizontal neighbours of a point
        """
        return [
            self.above,
            self.below,
            self.left,
            self.right
        ]
