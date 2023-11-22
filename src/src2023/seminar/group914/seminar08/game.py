from board import Board


class ComputerPlayerFirstSquare:
    def __init__(self, board):
        self.__board = board

    def move(self):
        """
        Calculate the computer's move
        :param board:
        :return: (row,col) where computer move
        """
        # TODO Decide where the computer should move
        for i in range(3):
            for j in range(3):
                if self.__board.get(i, j) == -10:
                    self.__board.move(i, j, 0)  # computer plays with 0
                    return i, j
        raise ValueError("Board is full")


class ComputerPlayerSmarter:
    def __init__(self, board):
        self.__board = board

    def move(self):
        # TODO Implement a smarter move
        pass


class Game:
    def __init__(self, board: Board, computer_level):
        self.__board = board
        self.__ai = computer_level

    def get_board(self) -> Board:
        return self.__board

    def move_human(self, row: int, column: int):
        self.__board.move(row, column, 1)

    def move_computer(self):
        return self.__ai.move()
