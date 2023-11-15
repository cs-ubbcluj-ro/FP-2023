def create_board():
    """
    Create a game board for Tic Tac Toe
    :return:
    """

    """
    Board representation
    ' ' -> empty square
    'X' -> X
    'O' -> O
    """
    board = []
    for i in range(3):
        board.append([' ', ' ', ' '])
    return board


def move_board(board, row: int, column: int, symbol: str):
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
    if get_board(board, row, column) != ' ':
        raise ValueError("Move would overlap existing symbol")
    board[row][column] = symbol


def get_board(board, row: int, col: int) -> str:
    """
    Return the symbol at (row, col) on the board
    :return: The symbol
    Raise ValueError if:
        - row or column are invalid
    """
    if row not in (0, 1, 2) or col not in (0, 1, 2):
        raise ValueError("Square is outside board")
    return board[row][col]


def get_board_status(board) -> int:
    """
    Get the status of the board
    :return: One of
        "Player wins", "Computer wins", "Still playing", "Draw"
                    1,              -1,               0,    200
    """

    # FIXME This is all very slow code :)
    # 1. Check if the game was won
    b = board
    for i in range(3):
        if b[i] == ['X' * 3]:
            return 1
        if b[i] == ['O' * 3]:
            return -1
        if b[0][i] == b[1][i] == b[2][i] == 'X':
            return 1
        if b[0][i] == b[1][i] == b[2][i] == 'O':
            return -1

    if b[0][0] + b[1][1] + b[2][2] == 'XXX':
        return 1
    if b[0][0] + b[1][1] + b[2][2] == 'OOO':
        return -1
    if b[2][0] + b[1][1] + b[0][2] == 'XXX':
        return 1
    if b[2][0] + b[1][1] + b[0][2] == 'OOO':
        return -1

    # 2. If there's a free square then it's still playing
    for row in range(3):
        for col in range(3):
            if get_board(board, row, col) == ' ':
                return 0

    # 3. Game is not won and there is no free square available
    return 200

    # def is_won_board(board) -> bool:


#     pass
#
#
# def is_drawn_board(board) -> bool:
#     pass


def test_board():
    board = create_board()

    # Test the board is empty
    assert get_board_status(board) == 0
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            assert get_board(board, i, j) == ' '

    # Test some moves on the board
    move_board(board, 1, 1, "X")
    assert get_board_status(board) == 0
    assert get_board(board, 1, 1) == 'X'

    # Invalid move -- square already occupied
    try:
        move_board(board, 1, 1, "O")
        assert False  # if this line runs, move_board did not raise the expected ValueError
    except ValueError:
        assert True  # does not do anything, only shows us the test passed

    # Invalid symbol
    try:
        move_board(board, 2, 2, "T")
        assert False
    except ValueError:
        assert True

    # Invalid square -- more extensive test
    b = create_board()
    for i in range(-5, 5):
        for j in range(-5, 5):
            if j in (0, 1, 2) and i in (0, 1, 2):
                # don't test for valid values
                continue

            try:
                move_board(board, i, j, "O")
                assert False, (i, j)
            except ValueError:
                assert True


def to_str(board) -> str:
    result = ""
    b = board

    for i in range(3):
        result += b[i][0] + "|" + b[i][1] + "|" + b[i][2] + "\n"
        if i != 2:
            result += "-" * 5 + "\n"
    return result


test_board()

b = create_board()
print(to_str(b))
