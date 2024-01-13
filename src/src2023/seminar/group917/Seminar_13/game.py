import random

from src2023.seminar.group917.Seminar_13 import RepoExceptions
from src2023.seminar.group917.Seminar_13.RepoExceptions import OutsideOfBoundsError, RepositoryExceptions


class ComputerPlayer:
    def __init__(self, player_board, other_board):
        self.__own_board = player_board
        self.__other_player_board = other_board

    def place_ship(self):
        # place it on its own board
        try:
            row = random.randint(1, self.__own_board.size + 1)
            column = random.randint(1, self.__own_board.size + 1)
            self.__own_board.place_ship(row, column)
            print(row, column)
        except OutsideOfBoundsError:
            self.place_ship()

    def hit(self):
        # try to hit on other player's board

        # If we want to make the computer player smarter, we
        # should record the result of our hits
        # When did we miss? When did we hit the target?
        # Would also avoid hitting the same place twice (we would
        # know what we tried before and choose accordingly)

        #correction: randint inclusive on both ends of the range
        # modified to not add 1
        row = random.randint(1, self.__own_board.size)
        column = random.randint(1, self.__own_board.size)
        #print(row, column)

        self.__other_player_board.hit(row, column)
        return row, column
