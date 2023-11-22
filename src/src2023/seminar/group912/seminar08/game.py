import random

from board import Board


def computer_player_level_1(board: Board) -> tuple:
    """
    Computer moves in first available square
    """
    for i in range(3):
        for j in range(3):
            if board.get(i, j) == 0:
                return i, j
    # board is full
    raise ValueError("Board is full")


def computer_player_level_2(board: Board) -> tuple:
    valid_moves = []
    # TODO It would be nice if Board kept track of available positions
    for i in range(3):
        for j in range(3):
            if board.get(i, j) == 0:
                valid_moves.append((i, j))
    return random.choice(valid_moves)


class Game:
    def __init__(self, computer_player):
        self.__board = Board()
        self.__computer_player = computer_player

    def get_board(self):
        return self.__board

    def computer_move(self):
        x, y = self.__computer_player(self.__board)
        self.__board.move(x, y, 'O')

    def human_move(self, x: int, y: int):
        self.__board.move(x, y, 'X')
