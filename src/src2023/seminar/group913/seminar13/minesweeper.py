from texttable import Texttable
from random import randint, shuffle


class GameOver(Exception):
    pass


class Minefield:
    def __init__(self, rows: int, columns: int, mines: int):
        self.__rows = rows
        self.__columns = columns
        self.__mines = mines
        """
        -1 -> square is mined
         1 - 8 -> number of adjacent mines 
         0 -> square is empty and unrevealed
        """
        self.__data = [[0 for _ in range(self.__columns)] for _ in range(self.__rows)]

        """
        Flags placed to mark mines
        Which squares are visible
        
        ' ' - revealed square with no mines adjacent
        '*' - unrevealed square
        'F' - marked with a flag
        'n' - number of adjacent mines 
        """
        self.__revealed_board = [['*' for _ in range(self.__columns)] for _ in range(self.__rows)]
        self.__mined = False

    def __is_inside(self, row, col) -> bool:
        return 0 <= row < self.__rows and 0 <= col < self.__columns

    def __increase_square(self, row, col):
        # NOTE Maybe two for loops?
        di = [-1, -1, -1, 0, 0, 1, 1, 1]
        dj = [-1, 0, 1, -1, 1, -1, 0, 1]
        for d in range(8):
            if self.__is_inside(row + di[d], col + dj[d]) and self.__data[row + di[d]][col + dj[d]] != -1:
                self.__data[row + di[d]][col + dj[d]] += 1

    def click(self, row: int, column: int):
        if self.__is_inside(row, column) is False:
            raise ValueError("Square not on minefield")
            # TODO Also if you try to reveal something that was already revealed!

        # FIXME Implement validation
        if self.__mined is False:
            # NOTE Lazy initialization => resources are not initialized before they are needed
            self.__lay_mines(row, column)
            self.__mined = True

        # 1. Check if user hit a mine
        if self.__data[row][column] == -1:
            raise GameOver()

        # 2. If square has at least one adjacent mine
        if self.__data[row][column] > 0:
            self.__revealed_board[row][column] = self.__data[row][column]
            return

        # 3. If square has no adjacent mines
        # we continue to reveal transitively
        if self.__data[row][column] == 0:
            stack = [(row, column)]
            while len(stack) > 0:
                row, column = stack.pop()
                self.__revealed_board[row][column] = self.__data[row][column] if self.__data[row][column] > 0 else ' '

                # TODO Write a __get_neighbours() function to replace these loops
                #  find all neighbours
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if i == 0 and j == 0:
                            continue
                        if self.__is_inside(row + i, column + j) == False:
                            continue
                        if self.__data[row + i][column + j] == 0:
                            if self.__revealed_board[row + i][column + j] == '*':
                                self.__revealed_board[row + i][column + j] = ' '
                                # continue only for squares that have no adjacent mines
                                stack.append((row + i, column + j))
                        elif self.__data[row + i][column + j] > 0:
                            self.__revealed_board[row + i][column + j] = self.__data[row + i][column + j]

    def __lay_mines(self, no_mine_row: int, no_mine_col: int):
        """
        Lay the mines
        :param no_mine_row, no_mine_col: There is no mine placed here
        :return:
        """

        # generate list of all valid minefield squares
        locations = []
        for i in range(self.__rows):
            for j in range(self.__columns):
                locations.append((i, j))

        # remove those the user clicked on and adjacent ones
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if self.__is_inside(no_mine_row + i, no_mine_col + j):
                    locations.remove((no_mine_row + i, no_mine_col + j))

        shuffle(locations)
        for i in range(self.__mines):
            row, col = locations.pop()
            self.__data[row][col] = -1
            self.__increase_square(row, col)

        # mines = self.__mines
        # while mines > 0:
        #     row = randint(0, self.__rows - 1)
        #     col = randint(0, self.__columns - 1)
        #     if row == no_mine_row and col == no_mine_col:
        #         # TODO - don't place any mines in the neighbouring squares either
        #         continue
        #     if self.__data[row][col] != -1:
        #         self.__data[row][col] = -1
        #         self.__increase_square(row, col)
        #         mines -= 1

    def __str__(self):
        """
        Return the str representation of the field

        1. Use a Texttable instance (size is rows * columns)
        2. Have a '*' in all squares
        3. The first row and column should be headers
            - the first row is (A, B, C, ...) - variable number of columns
            - the first columns is (1, 2, 3, ...) - variable number of rows
        """
        table = Texttable()
        table.set_cols_align(["c"] * (self.__columns + 1))
        table.set_cols_valign(["m"] * (self.__columns + 1))
        table.set_cols_width([3] * (self.__columns + 1))
        table.add_row([" "] + [chr(i + 65) for i in range(self.__columns)])
        for i in range(self.__rows):
            # table.add_row([i + 1] + ["*"] * self.__columns)
            # table.add_row([i + 1] + self.__data[i])
            table.add_row([i + 1] + self.__revealed_board[i])
        return table.draw()


if __name__ == "__main__":
    miefield = Minefield(8, 10, 2)
    miefield.click(3, 4)
    print(miefield)
