# Original strategy
from random import random, randint


# Two strategies for the computer player
# Key point: these strategies should be interchangeable
# E.g. User could choose level of difficulty

class ComputerRandomMoves:
    def __init__(self):
        pass

    def move(self, board):
        row = randint(1, 3)
        column = randint(1, 3)
        valid_move = False
        while not valid_move:
            try:
                board.update_position(row, column, 'O')
                valid_move = True
                return row, column
            except ValueError:
                row = randint(1, 3)
                column = randint(1, 3)


# What other strategies can the computer employ?
class ComputerBetterStrategy:
    def __init__(self):
        pass

    def move(self, board):
        # play smarter - look ahead
        # for instance, implement minimax
        # (Extra-reading) https://www.neverstopbuilding.com/blog/minimax
        return 1, 1


class Game:
    def __init__(self, board, computer_player):
        self.__board = board
        self.__computer = computer_player

    def make_user_move(self, row, column, symbol):
        """
        Make a move by the user
        :param board: the board which we modify
        :type board: list
        :param row: row of the position that we want to update
        :type row: int
        :param column: column of the position we want to update
        :type column: int
        :param symbol: symbol which user uses to play
        :type symbol: str
        :return: -; board is modified with the position (row, column) containing symbol, if move was possible
        :raises: ValueError if move was illegal
        """
        self.__board.update_position(row, column, symbol)

    def make_computer_move(self, symbol):
        """
        Make a move by the computer
        :param board: the board on which we make the move
        :type board: list
        :param symbol: the symbol which the computer uses to play
        :type symbol: str
        :return: position that computer played in form (row,column)
        :rtype: tuple
        """
        return self.__computer.move(self.__board)
