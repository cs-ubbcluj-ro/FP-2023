from board import Board
from random import choice


class ComputerPlayer:
    def __init__(self, symbol, game_board: Board):
        self._symbol = symbol
        self._board = game_board

    # def _get_free_squares(self):
    #     squares = []
    #     for i in range(0, self._board.height):
    #         for j in range(0, self._board.width):
    #             if self._board.get(i, j) == ' ':
    #                 squares.append((i, j))
    #     return squares

    def move(self):
        """
        Calculate and make a move on the board
        :return: (row,column) of the move
        """
        raise NotImplementedError()


class RandomMovePlayer(ComputerPlayer):
    def move(self):
        if len(self._board.available_moves) == 0:
            self._board.move(self._symbol, 0, 0)
        row, col = choice(self._board.available_moves)
        self._board.move(self._symbol, row, col)


if __name__ == "__main__":
    b = Board(5, 4)
    ai = RandomMovePlayer('O', b)

    b.move('X', 2, 2)
    ai.move()

    # b.move('X', 1, 0)
    print(b)
