# from my_module import *
from texttable import Texttable


class Board:
    def __init__(self):
        """
         0 is empty square
        -1 is O
         1 is X
        """
        # data is public => it can be accessed from outside the class
        # self.data = [0] * 9
        # _data is protected => it shouldn't be accessed from outside the class
        # self._data = [0] * 9
        # __data is private => it (almost) cannot be accessed from outside the class
        # (almost) = Python name mangling, it should be treated as private
        self.__data = [0] * 9
        self.__move_count = 0

    def move(self, x: int, y: int, symbol: str):
        """
        Make a move on the board
        :param board: Game board
        :param x: Row
        :param y: Column
        :param symbol: One of 'X' or 'O'
        :return: None
        Raises ValueError if:
            - trying to make a move outside the board
            - trying to take an already occupied square
            - symbol not an X or O
        """
        if symbol.lower() not in ['x', 'o']:
            raise ValueError("Invalid symbol used")
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Symbol is outside of board")
        # first check that position is valid
        if self.get(x, y) != 0:
            raise ValueError("Symbol overlaps existing one")
        self.__data[3 * x + y] = (1 if symbol.lower() == 'x' else -1)
        self.__move_count += 1

    def get(self, x: int, y: int) -> int:
        # TODO ValueError if (x,y) outside of board
        return self.__data[3 * x + y]

    def is_won(self) -> bool:
        # check for win on rows
        for i in range(0, 9, 3):  # 0, 3, 6
            if abs(sum(self.__data[i:i + 3])) == 3:
                return True

        # check for win on columns
        for i in range(3):
            if abs(sum(self.__data[i::3])) == 3:
                return True

        # check for wins on diagonal
        b = self.__data  # aliasing
        if abs(b[0] + b[4] + b[8]) == 3:
            return True
        if abs(b[2] + b[4] + b[6]) == 3:
            return True

        return False

    def is_full(self) -> bool:
        return self.__move_count == 9

    def __display_version(self):
        result = []
        for el in self.__data:
            if el == 0:
                result.append(' ')
            elif el == -1:
                result.append('O')
            elif el == 1:
                result.append('X')
        return result

    def __str__(self):
        data = self.__display_version()
        t = Texttable()  # Texttable is a class, this calls __init__
        for index in (0, 3, 6):
            t.add_row(data[index:index + 3])
        return t.draw()


"""
    class  = data type  // int
    object = instance   //  10
    
    Python predefined classes = tuple, dict, list, int, double, str, bool, function, ValueError
    We write our own classes now -- start with Board
"""

"""
We've done 2 things
    1. We have an actual type called Board
    2. The state of the board cannot be changed uncontrollably?
"""
if __name__ == "__main__":
    b = Board()
    # b._Board__data = "s"
    # print(dir(b))
    # b.__data[6] = "abc "  # !!!!!

    b.get(1, 1)  # b plays the rols of 'self'
    Board.get(b, 1, 1)  # same as the line above

    b.move(1, 1, 'X')
    b.move(0, 0, 'O')

    # b.move()
    # print(b.__data)

    print(b)
