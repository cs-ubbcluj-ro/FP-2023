from texttable import Texttable


class ChompError(Exception):
    pass


class GameOver(ChompError):
    pass


class Board:
    def __init__(self, width: int = 5, height: int = 4):
        """
        Board representation
            X, O -> moves on board
               - -> bitton off squares
               ! -> don't eat this!
        """
        self.__width = width
        self.__height = height
        self.__board = [[' ' for i in range(width)] for j in range(height)]
        self.__board[0][0] = '!'

        # all sqaures are available at the start
        self.__open_squares = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                self.__open_squares.append((i, j))
        self.__open_squares.remove((0, 0))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def available_moves(self):
        # NOTE This is a reference to the live list
        return self.__open_squares

    def get(self, row: int, col: int):
        # TODO Validations
        return self.__board[row][col]

    def move(self, symbol, row: int, column: int):
        if row == 0 and column == 0:
            raise GameOver()
        if not (0 <= row < self.__height):
            raise ChompError("Invalid row")
        if not (0 <= column < self.__width):
            raise ChompError("Invalid column")
        if self.__board[row][column] != ' ':
            raise ChompError("Square is eaten!")
        # place the symbol
        self.__board[row][column] = symbol
        self.__open_squares.remove((row, column))
        # mark remaining squares
        for i in range(row, self.__height):
            for j in range(column, self.__width):
                if self.__board[i][j] == ' ':
                    self.__board[i][j] = '-'
                    self.__open_squares.remove((i, j))

    def __str__(self):
        t = Texttable()
        hrow = ['/']
        for i in range(self.__width):
            hrow.append(chr(ord('A') + i))
        t.header(hrow)

        for i in range(self.__height):
            t.add_row([i + 1] + self.__board[i])
        return t.draw()


if __name__ == "__main__":
    b = Board(5, 4)
    print(len(b.available_moves))
    b.move('X', 2, 2)
    b.move('O', 2, 1)
    b.move('X', 1, 0)
    print(len(b.available_moves))
    print(b)
