from board import Board
import random


def decide_computer_move(board: Board) -> tuple:
    """
    Function which decides the computer's next move
    :param board: The game board
    :return: Tuple (row, column)
    """
    candidates = []
    # TODO Make the board module remember the list of still available squares
    for i in range(3):
        for j in range(3):
            if board.get(i, j) == ' ':
                candidates.append((i, j))
    # import random brings the "random" name into scope, but not "choice"
    return random.choice(candidates)


class Game:
    def __init__(self, board: Board):
        self.__board = board

    def move_human(self, row: int, col: int):
        self.__board.move(row, col, 'X')

    def move_computer(self):
        x, y = decide_computer_move(self.__board)
        self.__board.move(x, y, 'O')
