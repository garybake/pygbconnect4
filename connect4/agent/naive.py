import random

from connect4.agent.base import Agent
from connect4.move import Move


class RandomBot(Agent):

    def select_move(self, game_state):
        """
        Choose a random valid move thra preserves our own eyes
        """
        legal_moves = game_state.legal_moves()
        if not legal_moves:
            # todo board full, game over
            print('**No candidates')
        return Move.play(random.choice(legal_moves))
