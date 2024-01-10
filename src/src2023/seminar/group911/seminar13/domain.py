from texttable import Texttable

"""
Game must display two boards

Player's own board
    -> the position of your own ship(s) = S
    -> opponent's hits and misses       = x (opponent miss), $ (opponent hit)
    
Player's targeting board
    -> player's hits and misses = x (opponent miss), $ (opponent hit)

"""


class BattleshipError(Exception):
    pass


class GameOver(BattleshipError):
    pass


class Board:
    def __init__(self, size: int = 5):
        self._size = size
        self._data = [[' ' for i in range(size)] for j in range(size)]
        # print(self.__data)
        self._hit_count = 0

    @property
    def size(self):
        return self._size

    def place_ship(self, row: int, column: int):
        """
        Places the ship on the board. The ship has a length of exactly 3, is
        placed from left to right and (row, column) represent the leftmost square
        :return:
        """
        # FIXME What to do if calling this method twice (replace the ship, raise exception?)
        if not (0 <= column <= self._size - 3):
            raise BattleshipError("Ship outside bounds")
        if not (0 <= row <= self._size - 1):
            raise BattleshipError("Ship outside bounds")
        for i in (0, 1, 2):
            self._data[row][column + i] = 'S'

    def fire(self, row: int, column: int):
        """
        :param row:
        :param column:
        :return: True if hit, False if miss
        """
        # check that attacked square is on the board
        if not (0 <= row < self._size) or not (0 <= column < self._size):
            raise BattleshipError("Attack outside the board")
        # check that square was not attacked before
        if self._data[row][column] in ('$', '*'):
            raise BattleshipError("The square was attacked before")
        if self._data[row][column] == ' ':
            # hit an empty square
            self._data[row][column] = '*'
            return False
        if self._data[row][column] == 'S':
            # hit a ship
            self._data[row][column] = '$'
            # increase hit count and check for victory
            self._hit_count += 1
            if self._hit_count == 3:
                raise GameOver("I won")
            return True

    def __str__(self):
        """
        In C++ this method would be pure virtual and the class
        would be abstract

        In Java/C# this would be an abstract class with this method
        bein undefined
        """
        raise NotImplementedError()


class PlayerBoard(Board):
    def __str__(self):
        t = Texttable()
        header = []
        for i in range(ord('A'), ord('A') + self._size):
            header.append(chr(i))
        header.append("\\")
        t.header(header)

        for i in range(self._size):
            t.add_row(self._data[i] + [i + 1])
        return t.draw()


class TargetBoard(Board):
    def __str__(self):
        t = Texttable()
        header = []
        for i in range(ord('A'), ord('A') + self._size):
            header.append(chr(i))
        header.append("\\")
        t.header(header)

        for i in range(self._size):
            # Hide the computer player's unhit ship segments
            row = [char == 'S' and ' ' or char for char in self._data[i]] + [i + 1]
            t.add_row(row)
        return t.draw()


if __name__ == "__main__":
    b = PlayerBoard()
    b.place_ship(2, 2)
    b.fire(1, 2)
    b.fire(2, 2)
    b.fire(2, 3)
    # b.fire(2,4)
    print(b)
