class board:
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
    game_board = board()
    # Check that board is empty
    for i in range(3):
        for j in range(3):
            assert game_board.get(i, j) is None

    # Make some moves on the board
    game_board.update('X', 1, 1)
    assert game_board.get(1, 1) == 'X'
    game_board.update('O', 0, 0)
    assert game_board.get(0, 0) == 'O'

    # Make sure we can't overwrite symbols
    try:
        game_board.update('X', 1, 1)
        assert False
    except ValueError:
        assert True

    # Make sure you can't move outside the board
    try:
        game_board.update('X', 3, 1)
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
