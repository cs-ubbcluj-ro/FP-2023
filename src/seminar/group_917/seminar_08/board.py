class game_board:
    """
    C++ constructor:
        public:
            board() { ... }
    """

    def __init__(self):
        """
        Create the game board
        :return:
        """
        # Local variable in __init__
        # game_board = []
        # Class-level attribute, self <=> this in C++/Java/C#
        self.__game_board = []

        for i in range(3):
            self.__game_board.append([None, None, None])
        # Interpreter returns reference to newly created object implicitely
        # return game_board

    def get(self, row, col):
        """
        Return the symbol on board at (row,col)
        :param game_board:
        :param row:
        :param col:
        :return: 'X', 'O' or None
        """
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            raise ValueError("Outside board")
        return self.__game_board[row][col]

    def is_won(self):
        # check rows
        for row in [0, 1, 2]:
            if self.__game_board[row][0] is not None and len(set(self.__game_board[row])) == 1:
                return True
        # check columns
        gb = self.__game_board
        for col in [0, 1, 2]:
            if gb[0][col] is not None and gb[0][col] == gb[1][col] == gb[2][col]:
                return True
        # diagonals, center square must be filled in to win diagonally
        if gb[1][1] is not None:
            if gb[0][0] == gb[1][1] == gb[2][2]:
                return True
            if gb[2][0] == gb[1][1] == gb[0][2]:
                return True
        return False

    def update(self, symbol, row, col):
        """
        Make a move on the board
        :param game_board:
        :param symbol: One of X or O
        :param row: the row
        :param col: the column
        :return:
        Raise ValueError if move outside of board or square already taken, or
        symbol not an X or O
        """
        if symbol not in ['X', 'O']:
            raise ValueError("Invalid symbol")
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            raise ValueError("Move outside board - (" + str(row) + "," + str(col)
                             + ")")
        if self.get(row, col) is not None:
            raise ValueError("Cannot overwrite squares")
        self.__game_board[row][col] = symbol

    def __str__(self):
        """
        Represent the game board as an str
        :param game_board:
        :return:
        """
        result = ""
        for row in [0, 1, 2]:
            result += "|"
            for col in [0, 1, 2]:
                symbol = self.get(row, col)
                result += (" " if symbol is None else symbol) + "|"
                # <=> to the row above :)
                # if symbol is None:
                #     result += " " + "|"
                # else:
                #     result += symbol + "|"
            result += '\n'

        return result


def test_board():
    board = game_board()
    # Check that board is empty
    for i in range(3):
        for j in range(3):
            assert board.get(i, j) is None

    # Make some moves on the board
    board.update('X', 1, 1)
    assert board.get(1, 1) == 'X'
    board.update('O', 0, 0)
    assert board.get(0, 0) == 'O'

    # Make sure we can't overwrite symbols
    try:
        board.update('X', 1, 1)
        assert False
    except ValueError:
        assert True

    # Make sure you can't move outside the board
    try:
        board.update('X', 3, 1)
        assert False
    except ValueError:
        assert True

# print(type(board()))
# b = board()
#
# print(str(b))

# print(b.__game_board)
# print(b.__dict__)

# b.create_board()
#
# data = list()
# data.append(1)
# print(str(data))
