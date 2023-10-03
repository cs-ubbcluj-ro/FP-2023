import random

from texttable import Texttable


class Minefield():
    def __init__(self, rows, cols, mines: int):
        self._rows = rows
        self._cols = cols
        self._mines = mines

        self._data = [[0 for j in range(self._cols)] for i in range(self._rows)]
        self._visibility = [[False for j in range(self._cols)] for i in range(self._rows)]
        # self._data = [[0] * self._cols for i in range(self._rows)]

        # flag to make sure we only lay mines once
        self._mines_layed = False

    def reveal(self, row, col: int):
        if not self._on_board(row, col):
            raise Exception("Reveal outside board")
        if self._mines_layed is False:
            self._mines_layed = True
            self._lay_mines(row, col)

        if self._data[row][col] == -1:
            raise Exception("GAME OVER!")
        self._visibility[row][col] = True

        if self._data[row][col] == 0:
            self._reveal_rec(row, col)

    def _reveal_rec(self, row, col: int):
        self._visibility[row][col] = True

        if self._data[row][col] != 0:
            return

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if self._on_board(row + i, col + j) is False:
                    continue
                if self._visibility[row + i][col + j] is False:
                    self._reveal_rec(row + i, col + j)

    def _on_board(self, row, col: int) -> bool:
        return 0 <= row < self._rows and 0 <= col < self._cols

    def _lay_mines(self, no_row, no_col: int):
        """
        Lay mines
        :param no_row, no_col: Don't lay a mine here
        """
        locations = []
        for i in range(self._rows):
            for j in range(self._cols):
                # don't lay a mine at the user's first revealed square
                if i != no_row or j != no_col:
                    locations.append((i, j))
        random.shuffle(locations)
        while self._mines > 0:
            row, col = locations.pop(0)

            # lay the mine
            self._data[row][col] = -1
            # calculate the number of adjacent mines
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not self._on_board(row + i, col + j):
                        continue
                    if self._data[row + i][col + j] == -1:
                        continue
                    self._data[row + i][col + j] += 1
            self._mines -= 1

    def __str__(self):
        t = Texttable()

        header = ['X']
        for i in range(self._cols):
            header.append(chr(ord('A') + i))

        t.header(header)
        for row in range(self._rows):
            visible_row = self._data[row][:]
            for i in range(self._cols):
                if self._visibility[row][i] is False:
                    visible_row[i] = '#'
                    continue
                if self._data[row][i] == 0:
                    visible_row[i] = ' '

            t.add_row([row + 1] + visible_row)

        return t.draw()


m = Minefield(8, 10, 10)
m.reveal(4, 5)
print(m)
