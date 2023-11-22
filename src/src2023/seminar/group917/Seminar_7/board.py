# Voda Ioan
import numpy as np


def generate_board():
    """
    Generate empty board (empty: with values -1)
    :return: the created board
    :rtype: 2D list
    """
    return [[-1, -1, -1] for _ in range(3)]


# Soptelea Sebastian
def update_position(board, row, column, symbol):
    """
    Updates the position (row,column) on the board with the given symbol, if possible
    :param board: the board to be updated
    :type board: list
    :param row: the row on which we want to modify
    :type row: int
    :param column: the column on which we want to modify
    :type column: int
    :param symbol: the symbol we want to place on position (row,column)
    :type symbol: str ("X" or "O")
    :return: -; board is updated to contain symbol symbol at position (row, column)
                if move was possible, no changes otherwise
    :raises: ValueError if illegal move
    """
    if not 0 < row < 4:
        raise ValueError("Invalid row.")

    if not 0 < column < 4:
        raise ValueError("Invalid column.")

    if board[row - 1][column - 1] != -1:
        raise ValueError("Space has been played.")

    board[row - 1][column - 1] = symbol


def get_symbol_at_postion(board, row, column):
    """
    Get symbol at position row, column on the board
    :param board: board we are checking
    :type board: list
    :param row: row number
    :type row: int
    :param column: column number
    :type column: int
    :return: symbol at position row, column on board
    :rtype:
    :raises: ValueError if row, column are invalid
    """
    if not 0 < row < 4:
        raise ValueError("Invalid row.")

    if not 0 < column < 4:
        raise ValueError("Invalid column.")

    return board[row - 1][column - 1]


def get_board_status(board) -> int:
    """
    Checks if someone won the game
    :param board: the board we are checking
    :type board: list
    :return: code corresponding to status of board
            1 - won by human
            2 - won by computer
            0 - draw
            3 - game is still being played
    :rtype: int
    """
    # Q: is implementation efficient?
    # Q: will it work if we change the board (e.g. the size)?

    winning_x = ['X', 'X', 'X']
    winning_o = ['O', 'O', 'O']

    for i in range(3):
        row = board[i]
        if row == winning_x:
            return 1
        if row == winning_o:
            return 2

        column = [row[i] for row in board]
        if column == winning_x:
            return 1
        if column == winning_o:
            return 2

    main_diagonal = [board[0][0], board[1][1], board[2][2]]
    secondary_diagonal = [board[0][2], board[1][1], board[2][0]]
    if main_diagonal == winning_x or secondary_diagonal == winning_x:
        return 1
    if main_diagonal == winning_o or secondary_diagonal == winning_o:
        return 2

    if is_full(board):
        return 0
    else:
        return 3


def is_full(board):
    """
    Checks if the given board is full
    :param board: the board we are checking
    :type board: list
    :return: True if board is full, False otherwise
    :rtype: bool
    """
    for row_index in range(3):
        for col_index in range(3):
            if board[row_index][col_index] == -1:
                return False
    return True


def to_str(board):
    """
    Returns a string of the board for nice printing
    """
    board_str = ''
    for row in board:
        # .join(list/tuple/...) -> joins elements of the list/tuple/... IF they are all string, else raises Error
        # Initially: [str(elem) for elem in row]: create the list (see: parantheses []) which contains the string
        # representation (str(elem)) for each element in the row list ("for elem in row")
        # Current version: if elem!=-1 means X or O -> take it as is (elem if elem!=-1 else put a - instead of
        # -1 (better visibility of empty positions) (else "-") where we go over each elem in list row (for elem in row)
        board_str += ' | '.join([elem if elem != -1 else "-" for elem in row])
        board_str += '\n'
    return board_str


def test_update_postion():
    board = generate_board()
    update_position(board, 1, 1, 'X')
    assert (get_symbol_at_postion(board, 1, 1) == 'X')

    try:
        update_position(board, 10, 1, 'X')
        assert False
    except ValueError:
        assert True

    try:
        update_position(board, 1, 100, 'X')
        assert False
    except ValueError:
        assert True

    try:
        update_position(board, 1, 1, 'X')
        assert False
    except ValueError:
        assert True


def test_check_status():
    board = generate_board()
    update_position(board, 1, 1, 'X')
    update_position(board, 1, 3, 'X')
    update_position(board, 2, 3, 'O')
    assert (get_board_status(board) == 3)
    update_position(board, 3, 1, 'O')
    update_position(board, 3, 2, 'O')
    update_position(board, 3, 3, 'X')
    assert (get_board_status(board) == 3)
    # board is now:
    # X | - | X
    # - | - | O
    # O | O | X

    update_position(board, 1, 2, 'X')
    assert (get_board_status(board) == 1)

    board2 = generate_board()
    update_position(board2, 1, 1, 'X')
    update_position(board2, 3, 1, 'O')
    update_position(board2, 3, 2, 'O')
    update_position(board2, 2, 2, 'O')
    update_position(board2, 1, 2, 'O')
    # X | O | -
    # - | O | -
    # O | O | -
    assert (get_board_status(board2) == 2)

    board3 = generate_board()
    update_position(board3, 1, 1, 'X')
    update_position(board3, 1, 3, 'X')
    update_position(board3, 2, 3, 'O')

    update_position(board3, 1, 2, 'O')
    update_position(board3, 2, 1, 'X')
    update_position(board3, 2, 2, 'O')
    update_position(board3, 3, 1, 'O')
    update_position(board3, 3, 2, 'X')
    update_position(board3, 3, 3, 'X')
    # X | O | X
    # X | O | O
    # O | X | X
    assert (get_board_status(board3) == 0)
