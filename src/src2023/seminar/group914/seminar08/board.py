"""
class = data type

predefined classes = list, dict, int, float, str, ValueError
            object = an instance of a class

class = Toyota Corolla
object = Corolla CJ 03 TOY
"""
from texttable import Texttable


class Board:
    """
    Class that represent a game board for Tic Tac Toe
    """

    def __init__(self):
        # initialize the status of the board
        """
        -10 --> empty square
        1 --> X
        0 --> O
        """

        # vars starting with _ -> protected
        # self._data = [-10] * 9
        # vars starting with __ -> private, Python name mangling
        self.__data = [-10] * 9
        self.__moves = 0  # number of moves on the board

    def get(self, row: int, column: int):
        """
        Get the symbol at (row, column)
        :param row:
        :param column:
        :return: 0 for O, 1 for X, and -1 for empty square
        Raise ValueError if:
            - row or column outside of board
        """
        if row not in (0, 1, 2) or column not in (0, 1, 2):
            raise ValueError("Cell outside board!")
        return self.__data[3 * row + column]

    def move(self, row: int, column: int, symbol: int):
        """
        Record a move on the board
        :param board:
        :param symbol: One of [0, 1] (means O or X)
        :return:
        Raises ValueError if:
            - symbol is invalid
            - outside of the board
            - coordinates not empty
        """
        if symbol not in [0, 1]:
            raise ValueError("Invalid symbol")
        if row not in (0, 1, 2) or column not in (0, 1, 2):
            raise ValueError("Move outside board")
        if self.get(row, column) != -10:
            raise ValueError("Coordinates already taken")
        self.__data[3 * row + column] = symbol
        self.__moves += 1

    def is_full(self) -> bool:
        """
        Return True if board is full, and not won
        :param board:
        """
        return self.__moves == 9

    def is_won(self) -> bool:
        """
        Return True if board is won, False otherwise
        :param board:
        """

        # check rows for win
        for index in (0, 3, 6):
            if sum(self.__data[index:index + 3]) in (0, 3):
                return True

        # check columns for win
        for index in (0, 1, 2):
            if sum(self.__data[index::3]) in (0, 3):
                return True
        # check diagonals
        # TODO Is not very nice
        b = self.__data
        if sum((b[0], b[4], b[8])) in (0, 3):
            return True
        if sum((b[2], b[4], b[6])) in (0, 3):
            return True
        return False

    def __for_display(self):
        result = [' '] * 9
        for index in range(9):
            if self.__data[index] == 0:
                result[index] = 'O'
            elif self.__data[index] == 1:
                result[index] = 'X'
        return result

    def __str__(self):
        """
        str representation of board --> called when str(game_board)
        :return:
        """
        display_str = self.__for_display()
        t = Texttable()  # calls __init__ in class Texttable
        for index in (0, 3, 6):
            t.add_row(display_str[index:index + 3])
        return t.draw()


if __name__ == "main":
    # Board() calls the __init__ function of class Board
    game_board = Board()
    print(str(game_board))

    # game_board plays the role of self
    game_board.move(1, 1, 1)
    # equivalent to the call above
    # Board.move(game_board, 1, 1, 1)

    game_board.move(0, 0, 0)
    print(str(game_board))

    game_board.is_full()

    # print(type(game_board))
