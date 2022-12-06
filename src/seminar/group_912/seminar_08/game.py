"""
Human and computer moves
"""
from board import Board
from random import choice


class Game:
    def __init__(self):
        # private field of a Game class instance
        self.__board = Board()

    def get_board(self):
        return self.__board

    def human_move(self, row, col):
        self.__board.move('X', row, col)

    def computer_move(self):
        positions = []
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if self.__board.get_symbol(row, col) is None:
                    positions.append((row, col))
        pos = choice(positions)
        self.__board.move('O', pos[0], pos[1])
        return pos
