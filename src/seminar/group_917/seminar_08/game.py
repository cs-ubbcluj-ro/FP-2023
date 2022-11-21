from board import game_board
from random import choice

"""
TODO
    1. Create the game class and add the module functions to it
    2. Transmit the board as an __init__ parameter of game class
    3. Update method code so that they work with the board class
"""

# Strategy design pattern - https://en.wikipedia.org/wiki/Strategy_pattern
class computer_player_lvl_1:
    def play_computer(self, board: game_board):
        """
        Play the computer's move
        :param game_board:
        :return: The (row, col) where the move was made
        """
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if board.get(row, col) is None:
                    board.update('O', row, col)
                    return row, col


class computer_player_lvl_2:
    def play_computer(self, board: game_board):
        """
        Play the computer's move
        :param game_board:
        :return: The (row, col) where the move was made
        """
        available_pos = []

        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if board.get(row, col) is None:
                    available_pos.append((row, col))
        row, col = choice(available_pos)
        board.update('O', row, col)
        return row, col

class computer_player_lvl_3:
    def play_computer(self, board: game_board):
        """
        Play the computer's move
        :param game_board:
        :return: The (row, col) where the move was made
        """
        available_pos = []
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if board.get(row, col) is None:
                    available_pos.append((row, col))
        # TODO to be continued :)


        row, col = choice(available_pos)
        board.update('O', row, col)
        return row, col

class game:
    def __init__(self, board: game_board, computer_player):
        self.__board = board
        self.__computer_player = computer_player

    def play_human(self, row, col):
        """
        Record the human player's move
        :param game_board:
        :param row:
        :param col:
        :return:
        """
        self.__board.update('X', row, col)

    # TODO v1 - computer plays in the first available square
    # TODO v2 - computer plays in a random square
    # TODO v3 - computer plays randomly, but it wins if it can and it prevents easy
    # human wins
    def play_computer(self):
        """
        Play the computer's move
        :param game_board:
        :return: The (row, col) where the move was made
        """
        return self.__computer_player.play_computer(self.__board)
