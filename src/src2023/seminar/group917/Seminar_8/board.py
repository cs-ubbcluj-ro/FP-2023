from texttable import Texttable


# KEY CONCEPTS
# class -> construct used as a template to create instances of itself
#       e.g. Car
# object -> particular instance of the class
#       e.g. CJ 10 ABC

class Board:
    # Class variable -> shared among all instances of the class
    # Changes made to it affect all instances
    # boardsCreated = 0

    # .board -> public
    # ._board -> protected
    # .__board -> private, name mangling
    # Python name mangling: https://dev.to/ayushbisht2001/mangling-in-python-3b0h

    def __init__(self):
        # Instance variable -> changes made to it only affect the instance
        # on which the change is applied
        self.__board = [[-1, -1, -1] for _ in range(3)]
        # Board.boardsCreated += 1
        # self.__boardsCreated = 10
        self.__number_of_moves = 0

    def get_board(self):
        return self.__board

    def update_position(self, row, column, symbol):
        """
        Updates the position (row,column) on the board with the given symbol, if possible
        :param board: the board to be updated
        :type board: list
        :param row: the row on which we want to modify
        :type row: int
        :param column: the column on which we want to modify
        :type column: int
        :param symbol: the symbol we want to place on position (row,column)
        :type symbol: str ("X" or "O")
        :return: -; board is updated to contain symbol symbol at position (row, column)
                    if move was possible, no changes otherwise
        :raises: ValueError if illegal move
        """
        if not 0 < row < 4:
            raise ValueError("Invalid row.")

        if not 0 < column < 4:
            raise ValueError("Invalid column.")

        if self.__board[row - 1][column - 1] != -1:
            raise ValueError("Space has been played.")

        self.__board[row - 1][column - 1] = symbol
        self.__number_of_moves += 1

    def get_symbol_at_postion(self, row, column):
        """
        Get symbol at position row, column on the board
        :param board: board we are checking
        :type board: list
        :param row: row number
        :type row: int
        :param column: column number
        :type column: int
        :return: symbol at position row, column on board
        :rtype:
        :raises: ValueError if row, column are invalid
        """
        if not 0 < row < 4:
            raise ValueError("Invalid row.")

        if not 0 < column < 4:
            raise ValueError("Invalid column.")

        return self.__board[row - 1][column - 1]

    def get_board_status(self) -> int:
        """
        Checks if someone won the game
        :param board: the board we are checking
        :type board: list
        :return: code corresponding to status of board
                1 - won by human
                2 - won by computer
                0 - draw
                3 - game is still being played
        :rtype: int
        """
        # Q: is implementation efficient?
        # Q: will it work if we change the board (e.g. the size)?

        winning_x = ['X', 'X', 'X']
        winning_o = ['O', 'O', 'O']

        for i in range(3):
            row = self.__board[i]
            if row == winning_x:
                return 1
            if row == winning_o:
                return 2

            column = [row[i] for row in self.__board]
            if column == winning_x:
                return 1
            if column == winning_o:
                return 2

        main_diagonal = [self.__board[0][0], self.__board[1][1], self.__board[2][2]]
        secondary_diagonal = [self.__board[0][2], self.__board[1][1], self.__board[2][0]]
        if main_diagonal == winning_x or secondary_diagonal == winning_x:
            return 1
        if main_diagonal == winning_o or secondary_diagonal == winning_o:
            return 2

        if self.is_full():
            return 0
        else:
            return 3

    def is_full(self):
        """
        Checks if the given board is full
        :param board: the board we are checking
        :type board: list
        :return: True if board is full, False otherwise
        :rtype: bool
        """
        return self.__number_of_moves == 9

    def __str__(self):
        # use texttable module
        # https://pypi.org/project/texttable/
        table = Texttable()
        for row in self.__board:
            row = [' ' if elem == -1 else elem for elem in row]
            table.add_row(row)
        return table.draw()

    # def __eq__(self, other):
    #     print('__eq__ was called')
    #     return self.__board == other.get_board()


if __name__ == '__main__':
    # Board is the class
    # board, another_board are particular instances of the class
    # __init__ called
    board = Board()
    another_board = Board()

    # This gives an error now
    # print(board.__board)
    # This does not...
    # print(board._Board__board)

    # __str__ called
    print(board)

    # __eq__ called
    print(board == another_board)

    # Other magic methods: https://www.tutorialsteacher.com/python/magic-methods-in-python

    board.update_position(1, 1, 'X')
