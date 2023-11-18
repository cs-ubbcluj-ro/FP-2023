
# Voda Ioan
def generate_board():
    """
    Generate empty board (empty: with values -1)
    :return: the created board
    :rtype: 2D list
    """
    return [[-1, -1, -1] for _ in range(3)]


# Soptelea Sebastian
def update_position(board, row, column, symbol):
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

    if board[row - 1][column - 1] != -1:
        raise ValueError("Space has been played.")

    board[row - 1][column - 1] = symbol


def to_str(board):
    """
    Returns a string of the board for nice printing
    """
    board_str = ''
    for row in board:
        # .join(list/tuple/...) -> joins elements of the list/tuple/... IF they are all string, else raises Error
        # Initially: [str(elem) for elem in row]: create the list (see: parantheses []) which contains the string
        # representation (str(elem)) for each element in the row list ("for elem in row")
        #Current version: if elem!=-1 means X or O -> take it as is (elem if elem!=-1 else put a - instead of
        # -1 (better visibility of empty positions) (else "-") where we go over each elem in list row (for elem in row)
        board_str += ' | '.join([elem if elem != -1 else "-" for elem in row])
        board_str += '\n'
    return board_str
