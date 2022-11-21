import board

"""
TODO
    1. Create the game class and add the module functions to it
    2. Transmit the board as an __init__ parameter of game class
    3. Update method code so that they work with the board class
"""


def play_human(game_board, row, col):
    """
    Record the human player's move
    :param game_board:
    :param row:
    :param col:
    :return:
    """
    board.update_board(game_board, 'X', row, col)


# TODO v1 - computer plays in the first available square
# TODO v2 - computer plays in a random square
# TODO v3 - computer plays randomly, but it wins if it can and it prevents easy
# human wins
def play_computer(game_board):
    """
    Play the computer's move
    :param game_board:
    :return: The (row, col) where the move was made
    """
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            if board.get_symbol_on_board(game_board, row, col) is None:
                board.update_board(game_board, 'O', row, col)
                return row, col
