from board import move_board, get_board


def get_next_computer_move(board):
    # TODO
    # v2 -- make a random, but valid move
    # v3 -- prevent the human's instant win
    for i in range(3):
        for j in range(3):
            if get_board(board, i, j) == 0:
                return i, j
    # board is full
    raise ValueError("Board is full")


def computer_move(board):
    x, y = get_next_computer_move(board)
    move_board(board, x, y, 'O')


def human_move(board, x: int, y: int):
    move_board(board, x, y, 'X')
