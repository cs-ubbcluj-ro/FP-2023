from board import Board


def get_next_computer_move(board: Board) -> tuple:
    """
    Calculate the computer's next move
    :param board:
    :return: (row, column)
    """
    # TODO Make the computer play random, valid moves
    return 0, 0


class Game:
    def __init__(self, board: Board):
        self.__board = board

    def human_move(self, x: int, y: int):
        self.__board.move(x, y, 'X')  # human plays with X

    def computer_move(self):
        x, y = get_next_computer_move(self.__board)
        self.__board.move(x, y, 'O')
