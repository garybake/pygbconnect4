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


class GameState():
    """
    Captures the current state of the game
    Know about the board positions, next player, prev state and last move
    """
    def __init__(self, board, next_player, previous, move, winner=None):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move
        self.winner = winner

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
            next_board.place_piece(point, player)

            if self.is_win_move(player, point):
                self.winner = player

        return GameState(next_board, player.other, self, move, self.winner)

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
        """
        Is the game over
        - Player wins
        - No more places to play
        """
        if self.winner:
            print('****** {} WINS ******'.format(self.winner))
        if self.board.is_full():
            print('****** DRAW ******')
        return (self.winner is not None or self.board.is_full())

    def is_valid_move(self, move):
        """
        Is a move valid
        - Is the column full
        """
        if self.board.is_column_full(move.col):
            return False
        return True

    def legal_moves(self):
        candidates = []
        for candidate in range(1, self.board.num_cols + 1):
            if self.is_valid_move(Move.play(candidate)):
                candidates.append(candidate)
        return candidates

    def is_win_move(self, player, point):
        # TODO optimise this

        # Check vertical
        # Only need to check down
        vert_count = 1
        view_point = point.below()
        while self.board.get(view_point) == player:
            vert_count += 1
            view_point = view_point.below()
            if vert_count == 4:
                return True

        # Check horizontal
        horiz_count = 1
        view_point = point.left()
        while self.board.get(view_point) == player:
            horiz_count += 1
            view_point = view_point.left()
            if horiz_count == 4:
                return True

        view_point = point.right()
        while self.board.get(view_point) == player:
            horiz_count += 1
            view_point = view_point.right()
            if horiz_count == 4:
                return True

        # Check up_right
        diagr_count = 1
        view_point = point.above_right()
        while self.board.get(view_point) == player:
            diagr_count += 1
            view_point = view_point.above_right()
            if diagr_count == 4:
                return True

        view_point = point.below_left()
        while self.board.get(view_point) == player:
            diagr_count += 1
            view_point = view_point.below_left()
            if diagr_count == 4:
                return True

        # Check up_left
        diagl_count = 1
        view_point = point.above_left()
        while self.board.get(view_point) == player:
            diagl_count += 1
            view_point = view_point.above_left()
            if diagl_count == 4:
                return True

        view_point = point.below_right()
        while self.board.get(view_point) == player:
            diagl_count += 1
            view_point = view_point.below_right()
            if diagl_count == 4:
                return True

        return False
