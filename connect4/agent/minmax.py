import random

from connect4.agent.base import Agent
from connect4.c4board import Move


class MinMaxAgent(Agent):

    def select_move(self, game_state):
        """
        Choose a random valid move thra preserves our own eyes
        """
        legal_moves = game_state.legal_moves()

        next_player = game_state.next_player

        winning_move = self.find_winning_move(game_state, next_player)
        if winning_move:
            return Move.play(winning_move)

        if not legal_moves:
            # todo board full, game over
            print('**No candidates')
        return Move.play(random.choice(legal_moves))

    def find_winning_move(self, game_state, next_player):
        for col in game_state.legal_moves():
            next_state = game_state.apply_move(next_player, Move.play(col))
            if next_state.is_over() and next_state.winner == next_player:
                return col
        return None
