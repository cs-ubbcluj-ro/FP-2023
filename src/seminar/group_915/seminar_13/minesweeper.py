import random

from texttable import Texttable


class Minefield:
    def __init__(self, width, height, mines: int):
        self._width = width
        self._height = height
        self._mines = mines

        self._move_count = 0

        # * - mine
        # 0 - 8 -> count adjacent mines
        # adding 10 -> square is visible
        self._data = [[0 for i in range(self._width)] for j in range(self._height)]

    def reveal(self, row, col: int):
        if self._move_count == 0:
            self._lay_mines(row, col)
        self._move_count += 1

        if self._data[row][col] == '*':
            raise Exception("Game Over")
        elif 0 < self._data[row][col] < 10:
            # 10+ means the square is visible to the player
            self._data[row][col] += 10
        elif self._data[row][col] == 0:
            self._fill(row, col)

    def _fill(self, row, col: int):
        # this square is adjacent to a mine, so don't recursively reveal
        self._data[row][col] += 10

        # NOTE Create a method here?
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (0 <= row + i < self._height) and (0 <= col + j < self._width):
                    if self._data[row + i][col + j] == 0:
                        # reveal this square
                        # self._data[row][col] += 10
                        # continue the recursive fill
                        self._fill(row + i, col + j)
                    elif self._data[row + i][col + j] < 9:
                        self._data[row + i][col + j] += 10

    def _lay_mines(self, row_empty, col_empty):
        # Don't lay mines at row_empty, col_empty or adjacent to it
        candidates = []
        for i in range(self._width):
            for j in range(self._height):
                if abs(row_empty - j) <= 1 and abs(col_empty - i) <= 1:
                    continue
                candidates.append((i, j))

        for m in range(self._mines):
            x, y = random.choice(candidates)
            candidates.remove((x, y))
            # mark the square containing the mine
            self._data[y][x] = '*'
            # update number of mines in adjacent squares
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (0 <= y + i < self._height) and (0 <= x + j < self._width):
                        if self._data[y + i][x + j] != '*':
                            self._data[y + i][x + j] += 1

    def _hide_row(self, row):
        hidden = []
        for symbol in row:
            if symbol == '*' or symbol < 10:
                # hidden square
                hidden.append('?')
            elif symbol == 10:
                # visible, no mines adjacent
                hidden.append(' ')
            else:
                # visible, at least one mine adjacent
                hidden.append(symbol % 10)
        return hidden

    def __str__(self):
        t = Texttable()

        header = []
        for i in range(self._width):
            header.append(chr(ord('A') + i))
        t.header(header + ['/'])

        for i in range(self._height):
            t.add_row(self._hide_row(self._data[i]) + ['(' + str(i + 1) + ')'])

        return t.draw()


m = Minefield(10, 8, 10)
m.reveal(1, 1)
print(str(m))
