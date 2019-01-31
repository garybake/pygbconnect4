import random

from connect4.agent.base import Agent
from connect4.c4board import Move


class RandomBot(Agent):

    def select_move(self, game_state):
        """
        Choose a random valid move thra preserves our own eyes
        """
        candidates = []
        for candidate in range(1, game_state.board.num_cols + 1):
            if game_state.is_valid_move(Move.play(candidate)):
                candidates.append(candidate)
        if not candidates:
            # todo board full, game over
            print('**No candidates')
        return Move.play(random.choice(candidates))
