from board import move_board, get_board
from random import choice


def decide_computer_move(board) -> tuple:
    """
    Function which decides the computer's next move
    :param board: The game board
    :return: Tuple (row, column)
    """
    candidates = []
    # TODO Make the board module remember the list of still available squares
    for i in range(3):
        for j in range(3):
            if get_board(board, i, j) == ' ':
                candidates.append((i, j))
    return choice(candidates)


def move_human(board, row: int, col: int):
    move_board(board, row, col, 'X')


def move_computer(board):
    x, y = decide_computer_move(board)
    move_board(board, x, y, 'O')
