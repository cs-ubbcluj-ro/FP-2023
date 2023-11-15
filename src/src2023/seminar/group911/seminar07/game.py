"""
Game module
    -- decide the computer's next move
"""
from board import move


def human_move(board, x: int, y: int):
    move(board, x, y, 'X')  # human plays with X


def computer_move(board):
    x, y = get_next_computer_move(board)
    move(board, x, y, 'O')


def get_next_computer_move(board) -> tuple:
    """
    Calculate the computer's next move
    :param board:
    :return: (row, column)
    """
    # TODO Make the computer play random, valid moves
    return 0, 0
