import copy

from connect4.c4types import Point, Player
from .board import Board
from .move import Move


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
        """
        Apply a move to the current state
        Returns the next state of the game
        """
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
        """
        Return a list of valid moves
        - List of columns that aren't full
        """
        candidates = []
        for candidate in range(1, self.board.num_cols + 1):
            if self.is_valid_move(Move.play(candidate)):
                candidates.append(candidate)
        return candidates

    def is_win_move(self, player, point):
        """
        TODO optimise this

        Does a move result in a win for the player
        """

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
