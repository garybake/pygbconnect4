from connect4.c4types import Point


class Board():
    """
    Holds a game board in the current state
    """

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}  # dict of points

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
        """
        Add a point to the grid
        Note this is adding at x,y and not dropping from the top
        """
        grid = self._grid
        if grid.get(point):
            print('Piece already at {}'.format(point))
            return False
        else:
            grid[point] = player
            return True

    def is_column_full(self, col):
        """
        Is a column full
        """
        head_point = Point(row=1, col=col)
        if self.get(head_point):
            return True
        else:
            return False

    def is_full(self):
        """
        Is the board full
        """
        return len(self._grid) == (self.num_cols * self.num_rows)