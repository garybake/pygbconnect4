import random

from connect4.agent.base import Agent
from connect4.c4board import Move


class MinMaxAgent(Agent):

    def select_move(self, game_state):
        """
        Choose a random valid move
        """
        next_player = game_state.next_player

        # If we can win then yey
        winning_move = self.find_winning_move(game_state, next_player)
        if winning_move:
            return Move.play(winning_move)

        # Get a list of moves that won't setup a win for the other player
        possible_moves = self.eliminate_losing_moves(game_state, next_player)
        # possible_moves = game_state.legal_moves()

        if not possible_moves:
            possible_moves = game_state.legal_moves()
            if not possible_moves:
                # todo board full, game over
                print('**No candidates')
            else:
                print('**Expecting to loose')
        return Move.play(random.choice(possible_moves))

    def find_winning_move(self, game_state, next_player):
        """
        If the player can win with this move then do it
        """
        for col in game_state.legal_moves():
            next_state = game_state.apply_move(next_player, Move.play(col))
            if next_state.is_over() and next_state.winner == next_player:
                return col
        return None

    def eliminate_losing_moves(self, game_state, next_player):
        """
        Avoid giving opponent a winning move on the next turn
        """
        opponent = next_player.other  # red
        possible_moves = []
        for candidate_move in game_state.legal_moves():
            # for all my possible moves
            next_state = game_state.apply_move(next_player, Move.play(candidate_move))
            opponent_winning_move = \
                self.find_winning_move(next_state, opponent)
            if opponent_winning_move:  # DEBUG
                print('opponent can win here: {}'.format(opponent_winning_move))
            if opponent_winning_move is None:
                possible_moves.append(candidate_move)
        return possible_moves
