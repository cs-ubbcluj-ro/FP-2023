import random

from texttable import Texttable


class Minefield:
    def __init__(self, rows, cols, mines: int):
        self._rows = rows
        self._cols = cols
        self._mines = mines
        '''
        Data representation
        None -> empty square
        '''

        # TODO Border all the matrices !!
        self._data = [0] * ((self._rows + 2) * (self._cols + 2))
        self._mines_laid = False

    def reveal(self, row, col: int):
        if not self._mines_laid:
            # the first call of this method
            self._lay_mines(row, col)
            self._mines_laid = True
        pass

    def _set_value(self, row, col, value):
        """
        Transform row, col coordinates to padded matrix coordinates
        :param value: Set this value in the matrix
        """
        pass

    def _get_value(self, row, col) -> int:
        """
        Return the value at row,col from the padded matrix
        :param row:
        :param col:
        :return: Square value
        """
        pass

    def _lay_mines(self, empty_row, empty_col):
        """
        Lay the mines
        :param empty_row: there is no mine here
        :param empty_col: there is no mine here
        """
        locations = []
        for i in range(1, self._rows + 1):
            for j in range(1, self._cols + 1):
                # if i != (empty_row + 1) or j != (empty_col + 1):
                locations.append((i, j))
        # random.shuffle(locations)
        for i in range(self._mines):
            x, y = locations.pop(0)
            print(x, y)
            # self._data[x * self._cols + y] = 'X'
            self._set_value(x, y, 'X')

    def __str__(self):
        t = Texttable()
        t.set_max_width(0)

        # FIXME Separate into another function so we don't recompute header
        # at each __str__ call
        header = ['/']
        for i in range(0, self._cols):
            header.append(chr(ord('A') + i))

        t.header(header)
        for index in range(self._cols + 1, self._rows * (self._cols + 2), self._cols + 2):
            t.add_row([index // (self._cols + 1)] + self._data[index:index + self._cols])

        return t.draw()


field = Minefield(5, 5, 25)
field.reveal(0, 0)
print(field)
