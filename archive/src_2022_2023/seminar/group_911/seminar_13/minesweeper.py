import random

from texttable import Texttable


class MineField():
    def __init__(self, rows, cols, mines: int):
        self._rows = rows
        self._cols = cols
        self._mines = mines
        # we always want to create the mine field when initializing
        self._data = []

        """
        Meaning of values in self._data:
            0 - 8 => number of adjacent mines (square is not mined)
                9 => square is mined
              +10 => square is revealed
             +100 => square is flaged  
        """
        for row in range(self._rows):
            self._data.append([0] * self._cols)
        self._lay_mines()

    def _lay_mines(self):
        # 9 means the square is mined
        my_mines = [9] * self._mines
        my_mines += [0] * (self._rows * self._cols - self._mines)
        random.shuffle(my_mines)

        for row in range(self._rows):
            for col in range(self._cols):
                if my_mines[row * self._cols + col] == 9:
                    # lay the mine
                    self._data[row][col] = my_mines[row * self._cols + col]
                    # update mine adjacency
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if i == 0 and j == 0:
                                continue
                            if (0 > row + i) or (row + i >= self._rows):
                                continue
                            if (0 > col + j) or (col + j >= self._cols):
                                continue
                            if self._data[row + i][col + j] != 9:
                                self._data[row + i][col + j] += 1

    def __str__(self):
        t = Texttable()

        header = ['X']
        for ascii in range(self._cols):
            header.append(chr(65 + ascii))

        t.header(header)
        for r in range(self._rows):
            t.add_row([r + 1] + self._data[r])

        return t.draw()


f = MineField(8, 10, 50)
print(f)
