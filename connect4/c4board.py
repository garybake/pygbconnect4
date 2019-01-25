from connect4.c4types import Point


class Move():
    """
    User can choose which column to play

    Move.play(col)
    """
    def __init__(self, col=None):
        assert col is not None
        self.col = col

    @classmethod
    def play(cls, col):
        """
        Places a stone on the board
        """
        return Move(col=col)


class Board():
    """
    Holds a game board in the current state
    """

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}  # dict of points

    def apply_move(self, player, move):
        col = move.col
        high = self.find_highest_empty(col)
        if high is None:
            print('No room in column {}'.format(col))
            return False
        else:
            point = Point(high, col)
            print('Applying at {}'.format(point))
            self.place_piece(point, player)

    def find_highest_empty(self, col):
        for row in range(self.num_rows, 0, -1):
            potential_point = Point(row, col)
            if self.get(potential_point):
                continue
            else:
                return row
        return None

    def get(self, point):
        """
        Returns content of point on the board
        Player if stone is on that point
        else None
        """
        player = self._grid.get(point)
        if player is None:
            return None
        return player

    def place_piece(self, point, player):
        grid = self._grid
        if grid.get(point):
            print('Piece already at {}'.format(point))
            return False
        else:
            grid[point] = player
            return True
