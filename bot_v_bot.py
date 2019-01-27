import time
import random

from connect4.agent import naive
from connect4 import c4types
from connect4 import c4board
from connect4.utils import print_board, print_move


def main():
    board_size = 9
    game = c4board.GameState.new_game(board_size)

    bots = {
        c4types.Player.red: naive.RandomBot(),
        c4types.Player.yellow: naive.RandomBot()
    }
    go_num = 0
    while not game.is_over():
        # time.sleep(0.3)
        print_board(game.board)

        bot_move = bots[game.next_player].select_move(game)
        player = game.next_player
        print_move(game.next_player, bot_move)
        game = game.apply_move(player, bot_move)

        go_num += 1
        if go_num > 30:
            break

    print('Game over man!')

if __name__ == '__main__':
    main()
