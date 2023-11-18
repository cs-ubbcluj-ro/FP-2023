import random

from board import update_position


def make_user_move(board, row, column, symbol):
    """
    Make a move by the user
    :param board: the board which we modify
    :type board: list
    :param row: row of the position that we want to update
    :type row: int
    :param column: column of the position we want to update
    :type column: int
    :param symbol: symbol which user uses to play
    :type symbol: str
    :return: -; board is modified with the position (row, column) containing symbol, if move was possible
    :raises: ValueError if move was illegal
    """
    update_position(board, row, column, symbol)


def make_computer_move(board, symbol):
    """
    Make a move by the computer
    :param board: the board on which we make the move
    :type board: list
    :param symbol: the symbol which the computer uses to play
    :type symbol: str
    :return: position that computer played in form (row,column)
    :rtype: tuple
    """
    row = random.randint(1, 3)
    column = random.randint(1, 3)
    valid_move = False
    while not valid_move:
        try:
            update_position(board, row, column, symbol)
            valid_move = True
            return row, column
        except ValueError:
            row = random.randint(1, 3)
            column = random.randint(1, 3)
