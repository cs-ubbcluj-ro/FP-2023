from texttable import Texttable

from src2023.seminar.group917.Seminar_13.RepoExceptions import OutsideOfBoundsError, AlreadyHitPlaceError


# Serban Dragos
class GameOver(Exception):
    pass


class BattleshipsBoard:
    def __init__(self, size=5):
        self.__size = size
        self._board = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]
        self.__hits = 0

    @property
    def size(self):
        return self.__size

    def place_ship(self, row, column):
        row -= 1
        column -= 1
        if not (0 <= row < self.size) or not (0 <= column <= self.size - 3):
            raise OutsideOfBoundsError()
        for i in range(column, column + 3):
            self._board[row][i] = 'X'

    def hit(self, row, column):

        row -= 1
        column -= 1
        if not (0 <= row < self.size) or not (0 <= column < self.size):
            raise OutsideOfBoundsError()
        if self._board[row][column] in ['O', '*']:
            raise AlreadyHitPlaceError()
        elif self._board[row][column] == 'X':
            self.__hits += 1
            self._board[row][column] = 'O'
            if self.__hits == 3:
                raise GameOver()
        else:
            self._board[row][column] = '*'


class PlayerBoard(BattleshipsBoard):
    def __str__(self):
        table = Texttable()
        header = [' '] + [str(i + 1) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = [str(i + 1)] + self._board[i]
            table.add_row(row)

        return table.draw()


class ComputerBoard(BattleshipsBoard):
    def __str__(self):
        table = Texttable()
        #indices of columns
        header = [' '] + [str(i + 1) for i in range(self.size)]
        table.header(header)

        for i in range(self.size):
            row = self._board[i]
            #Replaced the if-else, renamed
            row_with_boat_hidden = [' ' if cell == 'X' else cell for cell in row]
            #add index of row
            row = [str(i + 1)] + row_with_boat_hidden
            table.add_row(row)

        return table.draw()
