from connect4 import c4types

COLS = 'ABCDEFGHIJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    c4types.Player.yellow: ' Y ',
    c4types.Player.red: ' R '
}


def print_move(player, move):
    print('{} drops at {}'.format(player, move.col))


def print_board(board):
    for row in range(1, board.num_rows + 1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(c4types.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('    ' + '  '.join(COLS[:board.num_cols]))
