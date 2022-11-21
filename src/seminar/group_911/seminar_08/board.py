# def test_board():
#     board = create_board()
#     # Check that the board is empty
#     for i in range(3):
#         for j in range(3):
#             assert get_position_on_board(board, i, j) is None
#     # Make some moves on the board
#     make_move_on_board(board, 'X', 1, 1)
#     assert get_position_on_board(board, 1, 1) == 'X'
#
#     make_move_on_board(board, 'O', 0, 0)
#     assert get_position_on_board(board, 0, 0) == 'O'
#
#     # Check that moving outside of board raises a ValueError
#     try:
#         make_move_on_board(board, 'X', 3, 3)
#         assert False
#     except ValueError:
#         assert True
#
#     # Check that we cannot overwrite a square
#     try:
#         make_move_on_board(board, 'O', 0, 0)
#         assert False
#     except ValueError:
#         assert True

class game_board:
    def __init__(self):
        """
        Create the Tic Tac Toe board
        :return: The empty game board
        """
        # board is a local variable in __init__
        # board = []
        # Let's make the game_board object "remember it"
        self.__board = []

        for i in range(3):
            self.__board.append([None, None, None])
        # The interpreter returns the object reference in __init__
        # return board

    def str_position(self, row, col):
        symbol = self.get_position_on_board(row, col)

        # This is <=> to what is below
        # return ' ' if symbol is None else symbol
        if symbol is not None:
            return symbol
        else:
            return ' '

    def get_position_on_board(self, row, col: int):
        """
        Return the symbol at (row,col)
        :param row:
        :param col:
        :return: X, O or None
        Raise ValueError if (row,col) outside of board
        """
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            raise ValueError("Position not on board - (" + str(row) + "," + str(col) + ")")
        return self.__board[row][col]

    def make_move_on_board(self, symbol, row, column):
        """
        Represent a move on the board
        :param board: The game board
        :param symbol: One of ['X', 'O']
        :param row, column: Position to play
        :return: None
        Raise ValueError if invalid symbol, already occupied square or play
        outside of board
        """
        if symbol not in ['X', 'O']:
            raise ValueError("Invalid symbol")
        if row not in [0, 1, 2] or column not in [0, 1, 2]:
            raise ValueError("Move outside board")
        if self.get_position_on_board(row, column) is not None:
            raise ValueError("Cannot overwrite board at (" + str(row) + "," + str(column) + ")")
        # This works as a setter function
        self.__board[row][column] = symbol

    def __str__(self):
        """
        Return the board's str representation
        :param board: The game board
        :return: In str form
        """
        gp = self.str_position
        result = "-----\n"
        for i in range(3):
            result += gp(i, 0) + "|" + gp(i, 1) + "|" + gp(i, 2) + "\n"
            result += "-----\n"
        return result


# gb = game_board()


# data = list()  # []
# data.append(1)
# list.append(data, 1)
# print(str(data))

gb = game_board()
# print(game_board.str_board(gb))  # gb is self from str_board
# print(gb.str_board())  # gb is passed as self implicitely by the interpreter
print(str(gb))  # how do we tell the interpreter what to call here?

# gb.__board[1][1] = '1234'
# print(gb.__dict__)
# print(gb.__board)
