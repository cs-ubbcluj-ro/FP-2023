"""
Board module
"""


# This class is a subclass of Python's Exception class
# That allows us to raise and catch it
class BoardFullException(Exception):
    pass


class GameWonException(Exception):
    pass


class Board():
    """
    this is Java
    public Board() { ... }
    Python's self is kind of like C++'s this
    """

    def __init__(self):
        """
        Create the game board
        :return: the board
        """
        # board is a local var in the __init__ method
        # board = []
        # self.board is an attribute of the Board class -> will be visible
        # across all Board methods

        """
        How do we protect self.board from being changed outside the class?
        
        C++/JAVA/C#
        private -> field/methods accessible only from within the class
        public  -> field/methods accessible from everywhere
        protected -> field/methods accessible from within the class and derived classes
                     (and in the same package in Java)
        
        Python -> private, etc keywords aren't used
            <name> -> public (e.g., self.board)
            _<name> -> private (by convention) (e.g., self._board)
            __<name> -> private (using name mangling) (e.g., self.__board)
        """
        self.__board = []
        self.__free_squares = 9
        for i in [0, 1, 2]:
            self.__board.append([' ', ' ', ' '])

    def get_symbol(self, row, col):
        # TODO Missing exceptions
        symbol = self.__board[row][col]
        if symbol != ' ':
            return symbol
        return None
        # return symbol if symbol =! ' ' else None

    def move(self, symbol, row, col):
        """
        Play a move on the board
        :param game_board: The game board
        :param symbol: one of 'X' or 'O'
        :param row: one of 0,1,2
        :param col: one of 0,1,2
        :return: None
        Raise ValueError if (row,col) outside board, symbol not one of (X,O) and
        if square already taken

        Raise BoardFullException if the board is full but it's not won
        Raise GameWonException if the game was won
        """
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            raise ValueError("Move outside the board")
        if symbol not in ['X', 'O']:
            raise ValueError("Invalid symbol")
        if self.get_symbol(row, col) is not None:
            raise ValueError("Square already taken")
        self.__board[row][col] = symbol
        self.__free_squares -= 1

        if self._is_won():
            raise GameWonException()
        if self._is_full():
            raise BoardFullException()

    def _is_won(self):
        gb = self.__board
        # checking for wins on rows
        for row in [0, 1, 2]:
            if gb[row][0] == ' ':
                # jump to the next iteration in the innermost loop
                continue
            if gb[row][0] == gb[row][1] == gb[row][2]:
                return True
        # checking for wins on columns
        for col in [0, 1, 2]:
            if gb[0][col] == ' ':
                # jump to the next iteration in the innermost loop
                continue
            if gb[0][col] == gb[1][col] == gb[2][col]:
                return True
        # checking on diagonals
        if gb[1][1] == ' ':
            return False
        if gb[0][0] == gb[1][1] == gb[2][2]:
            return True
        if gb[2][0] == gb[1][1] == gb[0][2]:
            return True

    def _is_full(self):
        return self.__free_squares == 0

    def __str__(self):
        result = ""
        gb = self.__board

        for row in [0, 1]:
            result += gb[row][0] + " | " + gb[row][1] + " | " + gb[row][2] + "\n"
            result += '--+---+--\n'
        result += gb[2][0] + " | " + gb[2][1] + " | " + gb[2][2] + "\n"
        return result


#
# def test_move_on_board():
#     game_board = Board()
#     # Test empty board
#     for row in [0, 1, 2]:
#         for col in [0, 1, 2]:
#             assert game_board.get_symbol(row, col) is None
#
#     # check for placing moves on the board
#     game_board.move('X', 1, 1)
#     assert game_board.get_symbol(1, 1) == 'X'
#     game_board.move('X', 0, 0)
#     assert game_board.get_symbol(0, 0) == 'X'
#     game_board.move('O', 2, 2)
#     assert game_board.get_symbol(2, 2) == 'O'
#
#     # check error handling
#     try:
#         game_board.move('X', 1, 1)
#         assert False
#     except ValueError:
#         assert True


if __name__ == "__main__":
    # Board.__init__ is called here implicitly
    # __init__ must return a reference to the new object --> handled by the
    # Python runtime
    b = Board()
    b.move('X', 1, 1)
    b.move('O', 2, 2)

    # we can use this but it's not very Pythonic :)
    # print(b.str_board())
    # print(str(b))
    # print(b)

    # each Board object (e.g., b1, b2) has its own independent copy of
    # self.__board
    b1 = Board()
    b2 = Board()
    b1.move('O', 1, 1)
    b2.move('X', 1, 1)

    print(b1)
    print(b2)

    # b plays the role of self implicitly
    # print(b.get_symbol(1, 1))
    # in this version of the call, b plays the role of self explicitly
    # print(Board.get_symbol(b, 1, 1))

    # print(b.__board)
    # b.__board[1][1] = 'X'
    # print(b.__board)
    # Python is called a dict programming language :)
    # print(b.__dict__)

    # print(type(b))
    # print(type([]))
    # print(type(str_board))

    # b = create_board()
    # move_on_board(b, 'X', 1, 1)
    # move_on_board(b, 'O', 0, 0)
    # move_on_board(b, 'X', 2, 2)
    # print(str_board(b))
