"""
This module handles the game's board
"""
import texttable


def create_board():
    board = []
    for i in range(3):
        board.append([' ', ' ', ' '])
    return board


def get_symbol(game_board, row, col):
    # TODO Handle incorrect row,col
    return game_board[row][col]


def make_move(game_board, row, col, symbol):
    """
    Record a move on the game board
    :param game_board: The board
    :param row: One of 0, 1 or 2
    :param col: One of 0, 1 or 2
    :param symbol: One of 'X' or 'O'
    :return: None
    Raises ValueError if symbol is not appropriate, move is outside the board or
    the square is already taken
    """
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        raise ValueError("Move outside board")
    if symbol not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if get_symbol(game_board, row, col) != ' ':
        raise ValueError("Square already taken")
    game_board[row][col] = symbol


def test_make_move():
    b = create_board()

    # Test that the board is empty
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            assert get_symbol(b, row, col) == ' '

    # Make some moves on the board
    make_move(b, 0, 0, 'X')
    assert get_symbol(b, 0, 0) == 'X'
    make_move(b, 2, 2, 'O')
    assert get_symbol(b, 2, 2) == 'O'

    # Check the function's error handling
    try:
        make_move(b, 4, 4, 'O')
        assert False  # exception was not raised => problem
    except ValueError:
        # exception should be raised
        assert True

    try:
        make_move(b, 1, 1, 'Y')
        assert False  # exception was not raised => problem
    except ValueError:
        # exception should be raised
        assert True

    try:
        make_move(b, 0, 0, 'X')  # cannot overwrite things
        assert False  # exception was not raised => problem
    except ValueError:
        # exception should be raised
        assert True


def str_board(game_board):
    table = texttable.Texttable()
    for row in [0, 1, 2]:
        table.add_row(game_board[row])
    return table.draw()


# test_make_move()
# b = create_board()
# make_move(b, 1, 1, 'X')
# make_move(b, 0, 0, 'O')
# # print(b)
# print(str_board(b))
