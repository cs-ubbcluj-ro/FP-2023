from texttable import Texttable


class BattleshipError(Exception):
    pass


class GameOver(BattleshipError):
    pass


class Board:
    def __init__(self, size: int = 5):
        self._size = 5
        """
        What do we need to represent here and what do we use !?        
            empty square -> ' '
            ship         -> 'X'
            a miss       -> '.'
            a hit        -> '*' 
        """
        self._data = [' '] * 25
        self._hit_counter = None

    @property
    def size(self):
        return self._size
    """
    0 1 2 3 4
    5 6 7 => C2
    """

    def place_ship(self, row: int, column: int):
        """
        Places a length 3 ship from left to right, first square is at (row, column)
        Raise BattleshipError if ship could not be placed
        """
        if not (0 <= row < self._size):
            raise BattleshipError("Ship on invalid row")
        if not (0 <= column < self._size - 2):
            raise BattleshipError("Ship on invalid row")
        for i in (0, 1, 2):
            self._data[row * self._size + column + i] = 'X'
        # We initialize the hit counter here, because we add the ship(s) to the board here
        self._hit_counter = 3

    def fire(self, row: int, column: int):
        """
        Fire at the given (row, column) square
        :return: True if it's a hit, False otherwise
        Raise GameOver if all ship segments were sunk
        """
        if not (0 <= row < self._size):
            raise BattleshipError("Invalid square attacked")
        if not (0 <= column < self._size):
            raise BattleshipError("Invalid square attacked")
        if self._data[row * self._size + column] in ('.', '*'):
            raise BattleshipError("Square was already attacked")

        if self._data[row * self._size + column] == 'X':
            self._data[row * self._size + column] = '*'
            self._hit_counter -= 1

            if self._hit_counter == 0:
                raise GameOver()
            else:
                return True

        else:
            self._data[row * self._size + column] = '.'
            return False

    def __str__(self):
        # The <=> of this in C++ would be a pure virtual method ( = 0) and the class would be abstract
        # In Java/C# this would be an abstract class
        raise NotImplementedError()


class PlayerBoard(Board):
    def __str__(self):
        t = Texttable()

        header = ['/']
        for i in range(self._size):
            header.append(chr(ord('A') + i))
        t.header(header)

        for i in range(0, self._size ** 2, self._size):
            t.add_row([i // 5 + 1] + self._data[i:i + self._size])
        return t.draw()


class TargetBoard(Board):
    def __str__(self):
        t = Texttable()
        data_copy = [' ' if x == 'X' else x for x in self._data]

        header = ['/']
        for i in range(self._size):
            header.append(chr(ord('A') + i))
        t.header(header)

        for i in range(0, self._size ** 2, self._size):
            t.add_row([i // 5 + 1] + data_copy[i:i + self._size])
        return t.draw()


if __name__ == "__main__":
    b = TargetBoard()
    b.place_ship(2, 2)
    b.fire(1, 2)
    b.fire(3, 3)
    b.fire(2, 2)
    print(b)
    b.fire(2, 4)
    print(b)
