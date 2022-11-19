def create_board():
    """
    Create the game board
    :return:
    """
    game_board = []
    for i in range(3):
        game_board.append([None, None, None])
    return game_board


def update_board(game_board, symbol, row, col):
    """
    Make a move on the board
    :param game_board:
    :param symbol: One of X or O
    :param row: the row
    :param col: the column
    :return:
    Raise ValueError if move outside of board or square already taken, or
    symbol not an X or O
    """
    if symbol not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        raise ValueError("Move outside board - (" + str(row) + "," + str(col)
                         + ")")
    if get_symbol_on_board(game_board, row, col) is not None:
        raise ValueError("Cannot overwrite squares")
    game_board[row][col] = symbol


def get_symbol_on_board(game_board, row, col):
    """
    Return the symbol on board at (row,col)
    :param game_board:
    :param row:
    :param col:
    :return: 'X', 'O' or None
    """
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        raise ValueError("Outside board")
    return game_board[row][col]


def str_board(game_board):
    """
    Represent the game board as an str
    :param game_board:
    :return:
    """
    result = ""
    for row in [0, 1, 2]:
        result += "|"
        for col in [0, 1, 2]:
            symbol = get_symbol_on_board(game_board, row, col)
            result += (" " if symbol is None else symbol) + "|"
            # <=> to the row above :)
            # if symbol is None:
            #     result += " " + "|"
            # else:
            #     result += symbol + "|"
        result += '\n'

    return result


# b = create_board()
# print(str_board(b))

def test_board():
    game_board = create_board()
    # Check that board is empty
    for i in range(3):
        for j in range(3):
            assert get_symbol_on_board(game_board, i, j) is None

    # Make some moves on the board
    update_board(game_board, 'X', 1, 1)
    assert get_symbol_on_board(game_board, 1, 1) == 'X'
    update_board(game_board, 'O', 0, 0)
    assert get_symbol_on_board(game_board, 0, 0) == 'O'

    # Make sure we can't overwrite symbols
    try:
        update_board(game_board, 'X', 1, 1)
        assert False
    except ValueError:
        assert True

    # Make sure you can't move outside the board
    try:
        update_board(game_board, 'X', 3, 1)
        assert False
    except ValueError:
        assert True
