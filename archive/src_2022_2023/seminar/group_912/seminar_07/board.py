"""
Board module
"""


def create_board():
    """
    Create the game board
    :return: the board
    """
    board = []
    for i in [0, 1, 2]:
        board.append([' ', ' ', ' '])
    return board


def get_symbol(game_board, row, col):
    # TODO Missing exceptions
    symbol = game_board[row][col]
    return symbol if symbol is not ' ' else None


def move_on_board(game_board, symbol, row, col):
    """
    Play a move on the board
    :param game_board: The game board
    :param symbol: one of 'X' or 'O'
    :param row: one of 0,1,2
    :param col: one of 0,1,2
    :return: None
    Raise ValueError if (row,col) outside board, symbol not one of (X,O) and
    if square already taken
    """
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        raise ValueError("Move outside the board")
    if symbol not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if get_symbol(game_board, row, col) is not None:
        raise ValueError("Square already taken")
    game_board[row][col] = symbol


#
# def test_move_on_board():
#     b = create_board()
#     # Test empty board
#     for row in [0, 1, 2]:
#         for col in [0, 1, 2]:
#             assert get_symbol(b, row, col) is None
#
#     # check for placing moves on the board
#     move_on_board(b, 'X', 1, 1)
#     assert get_symbol(b, 1, 1) == 'X'
#     move_on_board(b, 'X', 0, 0)
#     assert get_symbol(b, 0, 0) == 'X'
#     move_on_board(b, 'O', 2, 2)
#     assert get_symbol(b, 2, 2) == 'O'
#
#     # check error handling
#     try:
#         move_on_board(b, 'X', 1, 1)
#         assert False
#     except ValueError:
#         assert True


def str_board(game_board):
    result = ""
    gb = game_board

    for row in [0, 1]:
        result += gb[row][0] + " | " + gb[row][1] + " | " + gb[row][2] + "\n"
        result += '--+---+--\n'
    result += gb[2][0] + " | " + gb[2][1] + " | " + gb[2][2] + "\n"
    return result


if __name__ == "__main__":
    b = create_board()
    move_on_board(b, 'X', 1, 1)
    move_on_board(b, 'O', 0, 0)
    move_on_board(b, 'X', 2, 2)
    print(str_board(b))
