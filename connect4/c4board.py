import copy

from connect4.c4types import Point, Player


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


class GameState():
    """
    Captures the current state of the game
    Know about the board positions, next player, prev state and last move
    """
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    def apply_move(self, player, move):
        if player != self.next_player:
            raise ValueError(player)

        col = move.col
        next_board = copy.deepcopy(self.board)

        high = self.board.find_highest_empty(col)
        if high is None:
            print('No room in column {}'.format(col))
            return False
        else:
            point = Point(high, col)
            print('Applying at {}'.format(point))
            next_board.place_piece(point, player)
        return GameState(next_board, player.other, self, move)

    @classmethod
    def new_game(cls, board_size):
        """
        Creates a new blank GameState
        """
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.red, None, None)

    def is_over(self):
        # TODO
        return False
