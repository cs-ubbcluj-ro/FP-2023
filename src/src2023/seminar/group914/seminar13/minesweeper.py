import random

import texttable


class GameOver(Exception):
    pass


class Minefield:
    def __init__(self, width: int, height: int, mines: int):
        self.__width = width
        self.__height = height
        self.__mines = mines
        self.__mines_lain = False
        """
        How do we represent the states of one square?
        (no_adjacent_mines or -1, is_square_visible)
            0 - 8 -> number of adjacent mines
            -1    -> square is mined
        
        
        """
        self.__data = [[[0, False] for i in range(width)] for j in range(height)]

    def click(self, row, column):
        if self.__mines_lain == False:
            self.__lay_mines(row, column)
            self.__mines_lain = True

        if self.__data[row][column][0] == -1:
            raise GameOver("Game Over")
        # set square to revealed
        self.__data[row][column][1] = True
        if self.__data[row][column][0] == 0:
            # flood fill the board !!
            queue = [(row, column)]
            while len(queue) > 0:
                crow, ccol = queue.pop()
                # TODO Function to retreive the neighbours of a given square
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if (0 <= crow + i <= self.__height - 1) and (0 <= ccol + j <= self.__width - 1):
                            # only continue for squares that have no mines adjacent
                            if self.__data[crow + i][ccol + j][0] == 0:
                                # and squares that have not been revealed
                                if self.__data[crow + i][ccol + j][1] is False:
                                    self.__data[crow + i][ccol + j][1] = True
                                    queue.append((crow + i, ccol + j))
                            else:
                                self.__data[crow + i][ccol + j][1] = True

    def __lay_mines(self, x: int, y: int):
        """
        Function to lay the mines
        x, y - the user clicked here first, so there should be no mines here
        (x - row, y - column)
        """
        # list of all mineable locations
        locations = list(range(self.__width * self.__height))
        # remove the user's first click
        locations.pop(x * self.__width + y)
        # randomize list
        random.shuffle(locations)
        # place the mines at the first locations in list
        for mine in range(self.__mines):
            # place the mine at row, col
            index = locations[mine]  # the i-th mine is the i-th location in list
            row = index // self.__width
            col = index % self.__width
            self.__data[row][col] = (-1, False)
            # increase the adjacency in neighbouring squares
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    # check that square is inside the playing field
                    if (0 <= row + i <= self.__height - 1) and (0 <= col + j <= self.__width - 1):
                        # square is not mined
                        if self.__data[row + i][col + j][0] != -1:
                            # increase number of adjacent mines
                            self.__data[row + i][col + j][0] += 1

    def __str__(self):
        """
        " " character in all squares (as there are no mines yet)
        first row is a header (A, B, C, ...) - variable number of columns (def 10)
        first column is a header (1, 2, 3, ...) - variable number of rows (def 8)
        use a Texttable object
        """
        """
        " "chracter in al squares
        first row is a header
        first column is a header 1 2 3
        usee texttable

        :return:
        """
        table = texttable.Texttable()
        header = []
        header.append(' ')
        letter = 'ABCDEFGHIJKLMNOP'
        for i in range(self.__width):
            header.append(letter[i])
        table.header(header)
        for i in range(self.__height):
            row = [str(i + 1)]
            for j in range(self.__width):
                # row.append(str(self.__data[i][j][0]))
                value = "*"
                if self.__data[i][j][1]:
                    value = ' ' if self.__data[i][j][0] == 0 else str(self.__data[i][j][0])
                row.append(value)
            table.add_row(row)

        return table.draw()


field = Minefield(10, 8, 3)
field.click(3, 3)
print(str(field))
