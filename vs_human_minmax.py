import time
import random
from six.moves import input

from connect4.agent import minmax
from connect4 import c4types
from connect4.gamestate import GameState
from connect4.utils import print_board, print_move
from connect4.move import Move


def main():
    rows = 6
    cols = 7
    game = GameState.new_game((rows, cols))

    bot = minmax.MinMaxAgent()
    bot = minmax.MinMaxAgent()

    while not game.is_over():
        print('\n\n\n')
        # time.sleep(0.3)
        if game.next_player is c4types.Player.yellow:
            human_move = input('--- ')
            move_from_coords = int(human_move.strip())
            # TODO validate human move
            bot_move = Move.play(move_from_coords)
        else:
            bot_move = bot.select_move(game)
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
