import board


def human_move(game_board, row, col):
    """
    Record the human's move on the board
    :param game_board:
    :param row:
    :param col:
    :return:
    """
    board.make_move_on_board(game_board, 'X', row, col)


def computer_move(game_board):
    """
    Determine where the computer plays and make the move
    :param game_board:
    :return: The position where computer moved
    """
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            if board.get_position_on_board(game_board, row, col) is None:
                board.make_move_on_board(game_board, 'O', row, col)
                return row, col
