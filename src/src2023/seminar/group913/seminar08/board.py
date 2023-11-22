from texttable import Texttable


class Board:
    def __init__(self):
        """
        Board representation
        ' ' -> empty square
        'X' -> X
        'O' -> O
        """
        # .data is public => it can be accessed from anywhere
        # self.data = [' '] * 9  # board is 3 x 3
        # _data is protected => it should not be accessed from outside the class
        # self._data = [' '] * 9  # board is 3 x 3
        # .__data is private => Python changes its name (name mangling)
        self.__data = [' '] * 9  # board is 3 x 3
        self.__move_count = 0
        self.__last_symbol = None  # who played last

    def get(self, row: int, col: int) -> str:
        """
        Return the symbol at (row, col) on the board
        :return: The symbol
        Raise ValueError if:
            - row or column are invalid
        """
        if row not in (0, 1, 2) or col not in (0, 1, 2):
            raise ValueError("Square is outside board")
        return self.__data[row * 3 + col]

    def move(self, row: int, column: int, symbol: str):
        """
        Record a move with given symbol on the board, at location (row, column)
        :return: None
        Raises ValueError if:
            - symbol is not one of [X, O]
            - row or column are invalid
            - there is already a symbol at (row, column)
        """
        if symbol not in ('X', 'O'):
            raise ValueError("Invalid symbol")
        if row not in (0, 1, 2) or column not in (0, 1, 2):
            raise ValueError("Move would fall outside board")
        if self.get(row, column) != ' ':
            raise ValueError("Move would overlap existing symbol")
        self.__data[3 * row + column] = symbol
        self.__move_count += 1
        self.__last_symbol = symbol

    def get_status(self) -> int:
        """
        Get the status of the board
        :return: One of
            "Player wins", "Computer wins", "Still playing", "Draw"
                        1,              -1,               0,   200
        """
        if self.__move_count < 5:
            # can only win when more than 4 symbols have been placed (XOXOX)
            return 0

        sym = self.__last_symbol
        data = self.__data
        # check for win on rows
        for index in (0, 3, 6):
            if all(ele == sym for ele in data[index:index + 3]):
                return 1 if sym == 'X' else -1
        # check for win on columns
        for index in (0, 1, 2):
            if all(ele == sym for ele in data[index::3]):
                return 1 if sym == 'X' else -1
        # data[0::4]
        # data[2:-1:2] ??
        # check diagonals
        if all(ele == sym for ele in (data[0], data[4], data[8])):
            return 1 if sym == 'X' else -1
        if all(ele == sym for ele in (data[2], data[4], data[6])):
            return 1 if sym == 'X' else -1

        return 0 if self.__move_count < 9 else 200

    def __str__(self):
        """
        Return the str representation of the board
        when we str(board) => __str__ is called
        """
        t = Texttable()
        for i in range(3):
            t.add_row(self.__data[3 * i:3 * i + 3])
        return t.draw()


if __name__ == "main":
    b = Board()  # Board() calls the class constructor => __init__
    print(b)  # __str__ is called here

    b.move(1, 1, 'X')  # self is the current object, b in this case
    # line below is equivalent to the line above
    Board.move(b, 0, 0, 'O')
    print(b)  # __str__ is called here
