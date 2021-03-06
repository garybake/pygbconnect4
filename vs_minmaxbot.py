import time
import random

from connect4.agent import minmax
from connect4 import c4types
from connect4.gamestate import GameState
from connect4.utils import print_board, print_move


def main():
    rows = 6
    cols = 7
    game = GameState.new_game((rows, cols))

    bots = {
        c4types.Player.red: minmax.MinMaxAgent(),
        c4types.Player.yellow: minmax.MinMaxAgent()
    }

    while not game.is_over():
        print('\n\n\n')
        # time.sleep(0.3)
        bot_move = bots[game.next_player].select_move(game)
        player = game.next_player

        print_move(game.next_player, bot_move)
        game = game.apply_move(player, bot_move)
        print_board(game.board)

    if game.winner:
        print('*** WINNER : {}'.format(game.winner))
    else:
        print('*** DRAW ***')

if __name__ == '__main__':
    main()
