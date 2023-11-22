# import all functions except those beginning with an _
# from my_module import *
from texttable import Texttable  # not a built-in Python module


class Board:
    def __init__(self):
        """
        Board representation
        ' ' - empty square
        'X' - X
        'O' - O
        """
        # data is public, so it's accessible from outside the class
        # self.data = [' '] * 9

        # _data is protected, so it should not be accessed from outside
        # the class (convention)
        # self._data = [' '] * 9

        # __data is private, and its name is changed (name mangling)
        self.__data = [' '] * 9
        # __data = [' '] * 9
        self.__last_symbol = None
        self.__move_count = 0

    def move(self, row: int, col: int, symbol: str):
        """
        Record move on the board
        :param board:
        :param row:
        :param col:
        :param symbol:
        :return:
        Raises ValueError if:
            - symbol not one of 'X', 'O'
            - row or column are invalid (not in 0, 1, 2)
            - there is already a symbol at (row, col)
        """
        # TODO implement error handling
        self.__data[3 * row + col] = symbol
        self.__last_symbol = symbol
        self.__move_count += 1

    def is_won(self):
        """
        Check if the board was won
        :param board:
        :return: The symbol of the winning player, None if no one won yet
        """

        if self.__move_count < 5:
            return None

        # check for win on rows
        sym = self.__last_symbol
        for index in (0, 3, 6):
            # len(set(self.__data[index:index + 3])) == 1
            if all(i == sym for i in self.__data[index:index + 3]):
                return sym

        # check for win on columns
        for index in (0, 1, 2):
            if all(i == sym for i in self.__data[index::3]):
                return sym

        # check for win on diagonal
        if all(i == sym for i in self.__data[0::4]):
            return sym
        if all(i == sym for i in self.__data[2:7:2]):
            # secondary diagonal
            return sym

        return None

    def is_full(self) -> bool:
        """
        Check is board is full
        :param board:
        :return: True if no moves can be made
        """
        return self.__move_count == 9

    def __str__(self):
        """
        0 1 2
        3 4 5
        6 7 8
        :return:
        """
        t = Texttable()
        for index in (0, 3, 6):
            t.add_row(self.__data[index:index + 3])
        return t.draw()


"""
class  = data type (template)    // Toyota RAV4
object = instance                // CJ 99 TOY

classes in Python -> str, int, float, list, dict, tuple, set, bool,
                     ValueError

"""

"""
What we managed to do
    1. hide the board's representation
    2. print the board in a Pythonic way
"""

if __name__ == "main":
    b = Board()  # call to class constructor, method __init__
    print(b)  # calls Board.__str__

    b.move(1, 1, 'X')  # self is b here
    Board.move(b, 0, 0, 'O')

    print(b)  # calls Board.__str__
