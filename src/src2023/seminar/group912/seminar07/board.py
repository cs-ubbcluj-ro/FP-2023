"""
Board module
    -- represent the board's state
    -- check if the game was won / drawn
    -- check for any errors? (trying to place outside the board)
"""


def create_board():
    """
    Create an empty game board
    :return: The new board
    """

    """
     0 is empty square
    -1 is O
     1 is X
    """
    return [0] * 9


def move_board(board, x: int, y: int, symbol: str):
    """
    Make a move on the board
    :param board: Game board
    :param x: Row
    :param y: Column
    :param symbol: One of 'X' or 'O'
    :return: None
    Raises ValueError if:
        - trying to make a move outside the board
        - trying to take an already occupied square
        - symbol not an X or O
    """
    if symbol.lower() not in ['x', 'o']:
        raise ValueError("Invalid symbol used")
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Symbol is outside of board")
    # first check that position is valid
    if get_board(board, x, y) != 0:
        raise ValueError("Symbol overlaps existing one")
    board[3 * x + y] = (1 if symbol.lower() == 'x' else -1)


def get_board(board, x: int, y: int) -> str:
    # TODO ValueError if (x,y) outside of board
    return board[3 * x + y]


def to_str(board) -> str:
    """
    Represent the board as an str
    :return: str representation of board
    """
    result = ""

    for i in range(9):
        if board[i] == -1:
            result += 'O'
        elif board[i] == 0:
            result += ' '
        elif board[i] == 1:
            result += 'X'
        if (i + 1) % 3 == 0:
            result += "\n"
        else:
            result += "|"
    return result


def is_board_won(game_board) -> bool:
    # check for win on rows
    for i in range(0, 9, 3):  # 0, 3, 6
        if abs(sum(game_board[i:i + 3])) == 3:
            return True

    # check for win on columns
    for i in range(3):
        if abs(sum(game_board[i::3])) == 3:
            return True

    # check for wins on diagonal
    b = game_board  # aliasing
    if abs(b[0] + b[4] + b[8]) == 3:
        return True
    if abs(b[2] + b[4] + b[6]) == 3:
        return True

    return False


def is_board_drawn(game_board) -> bool:
    for el in game_board:
        if el == 0:
            return False
    return True


def test_move_board():
    board = create_board()
    # check that board is empty
    for i in range(3):
        for j in range(3):
            assert get_board(board, i, j) == 0  # 0 means empty square

    # try to make a move on the board
    move_board(board, 1, 1, "X")
    assert get_board(board, 1, 1) == 1
    # make another valid board move
    move_board(board, 0, 0, "X")  # board does not check alternance
    assert get_board(board, 0, 0) == 1
    assert get_board(board, 1, 1) == 1

    # try to take an occupied square -> should raise ValueError
    # i want a test that fails in case no ValueError was raised
    # i want nothing to happen if the error was raised
    try:
        move_board(board, 1, 1, "X")
        assert False
    except ValueError:
        assert True  # we have to get to this point

    # TODO Tests to check valid symbol and placement inside the board


if __name__ == "__main__":
    test_move_board()

    b = create_board()
    move_board(b, 1, 1, 'x')
    move_board(b, 0, 40, 'o')
    print(to_str(b))
