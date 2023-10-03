def create_board():
    """
    Create the Tic Tac Toe board
    :return: The empty game board
    """
    board = []
    for i in range(3):
        board.append([None, None, None])
    return board


def get_position_on_board(board, row, col: int):
    """
    Return the symbol at (row,col)
    :param row:
    :param col:
    :return: X, O or None
    Raise ValueError if (row,col) outside of board
    """
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        raise ValueError("Position not on board - (" + str(row) + "," + str(col) + ")")
    return board[row][col]


def str_position(board, row, col):
    symbol = get_position_on_board(board, row, col)

    # This is <=> to what is below
    # return ' ' if symbol is None else symbol
    if symbol is not None:
        return symbol
    else:
        return ' '


def str_board(board):
    """
    Return the board's str representation
    :param board: The game board
    :return: In str form
    """
    gp = str_position
    result = "-----\n"
    for i in range(3):
        result += gp(board, i, 0) + "|" + gp(board, i, 1) + "|" + gp(board, i, 2) + "\n"
        result += "-----\n"
    return result


def make_move_on_board(board, symbol, row, column):
    """
    Represent a move on the board
    :param board: The game board
    :param symbol: One of ['X', 'O']
    :param row, column: Position to play
    :return: None
    Raise ValueError if invalid symbol, already occupied square or play
    outside of board
    """
    if symbol not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if row not in [0, 1, 2] or column not in [0, 1, 2]:
        raise ValueError("Move outside board")
    if get_position_on_board(board, row, column) is not None:
        raise ValueError("Cannot overwrite board at (" + str(row) + "," + str(column) + ")")
    # This works as a setter function
    board[row][column] = symbol


def test_board():
    board = create_board()
    # Check that the board is empty
    for i in range(3):
        for j in range(3):
            assert get_position_on_board(board, i, j) is None
    # Make some moves on the board
    make_move_on_board(board, 'X', 1, 1)
    assert get_position_on_board(board, 1, 1) == 'X'

    make_move_on_board(board, 'O', 0, 0)
    assert get_position_on_board(board, 0, 0) == 'O'

    # Check that moving outside of board raises a ValueError
    try:
        make_move_on_board(board, 'X', 3, 3)
        assert False
    except ValueError:
        assert True

    # Check that we cannot overwrite a square
    try:
        make_move_on_board(board, 'O', 0, 0)
        assert False
    except ValueError:
        assert True
