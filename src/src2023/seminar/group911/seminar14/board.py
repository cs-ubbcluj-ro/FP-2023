import texttable
from random import shuffle


class Board:
    def __init__(self, rows: int, cols: int, mines: int):
        self.__rows = rows
        self.__cols = cols
        self.__mines = mines
        self.__first_move = False
        """
        0 - 8 number of adjacent mines
        9 - mine
        
        +10 for all squares that are revelead
        
        e.g;,
        0 is a square with no adjacent mines but unrevealed
        10 is a square with no adjacent mines but revealed
        """
        self.__data = [[0 for i in range(self.__cols)] for i in range(self.__rows)]

    def move(self, row: int, col: int):
        if not self.__first_move:
            locations = []
            # 1. generate all candidate squares to be mined
            for i in range(self.__rows):
                for j in range(self.__cols):
                    locations.append((i, j))

            # 2. remove where the user clicked first & adjacent
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (row + i, col + j) in locations:
                        locations.remove((row + i, col + j))
            # 3. lay the mines
            self.__lay_mines(locations)
            self.__first_move = True
        # FIXME Fix this
        stack = [(row, col)]
        while len(stack) > 0:
            row, col = stack.pop()
            self.__data[row][col] += 10  # make it visible

            if self.__data[row][col] > 10:  # has a mine as neighbour
                continue

            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (0 <= row + i < self.__rows) and (0 <= col + j < self.__cols):
                        if self.__data[row][col] < 10:
                            stack.append((row + i, col + j))

    def __lay_mines(self, locations: list):
        shuffle(locations)
        for i in range(self.__mines):
            row, col = locations[0]

            # lay the mine
            self.__data[row][col] = 9
            # mark adjacent squares
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (0 <= row + i < self.__rows) and (0 <= col + j < self.__cols):
                        if self.__data[row + i][col + j] != 9:
                            self.__data[row + i][col + j] += 1

            locations.pop(0)

    def __str__(self):
        t = texttable.Texttable()

        header = []
        for i in range(ord('A'), ord('A') + self.__cols):
            header.append(chr(i))
        header.append("\\")
        t.header(header)

        for i in range(self.__rows):
            t.add_row(self.__data[i] + [(i + 1)])

        return t.draw()


b = Board(8, 10, 10)
b.move(4, 4)
print(b)
