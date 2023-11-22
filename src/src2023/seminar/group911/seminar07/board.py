"""
Board module
    -- how is the board represented??
    -- build the board's str representation
    -- check if the game was won
    -- check if the game was drawn
"""


def create_board():
    """
    Create an empty game board
    :return: the empty board
    """

    """
    Board representation
    ' ' - empty square
    'X' - X
    'O' - O
    """

    result = []
    for i in range(3):
        result.append([' '] * 3)
    return result


def move(board, row: int, col: int, symbol: str):
    """
    Record move on the board
    :param board:
    :param row:
    :param col:
    :param symbol:
    :return:
    Raises ValueError if:
        - symbol not one of 'X', 'O'
        - row or column are invalid (not in 0, 1, 2)
        - there is already a symbol at (row, col)
    """
    # TODO implement error handling
    board[row][col] = symbol


def is_won_board(board) -> str:
    """
    Check if the board was won
    :param board:
    :return: The symbol of the winning player, None if no one won yet
    """
    # FIXME This function is very, very slow :)
    # The idea is that the game is won by the most recent move,
    # so only check that row, column and diagonal (if applicable)
    row0 = board[0]
    row1 = board[1]
    row2 = board[2]

    # check for win on rows
    for row in (row0, row1, row2):
        if "".join(row) == "XXX":
            return "X"
        elif "".join(row) == "OOO":
            return "O"
    # check for win on columns
    for col in (0, 1, 2):
        column = row0[col] + row1[col] + row2[col]
        if column == 'XXX':
            return 'X'
        elif column == 'OOO':
            return 'O'

    # check for win on diagonal
    diag1 = row0[0] + row1[1] + row2[2]
    diag2 = row0[2] + row1[1] + row2[0]
    if diag1 == 'XXX' or diag2 == 'XXX':
        return 'X'
    if diag1 == 'OOO' or diag2 == 'OOO':
        return 'O'


def is_full_board(board) -> bool:
    """
    Check is board is full
    :param board:
    :return: True if no moves can be made
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def to_str(board) -> str:
    """
    Build the board's str representation
    """
    b = board
    return f"{b[0][0]}|{b[0][1]}|{b[0][2]}\n{b[1][0]}|{b[1][1]}|{b[1][2]}\n{b[2][0]}|{b[2][1]}|{b[2][2]}"


# in the UI module
b = create_board()
# b[1][1] = "abcd"
print(to_str(b))
print(type(b))

# print("|".join(["X","O","X"]))
