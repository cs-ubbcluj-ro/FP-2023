from texttable import Texttable


class GameException(Exception):
    pass


class GameOver(GameException):
    pass


class Board:
    def __init__(self, width, height: int):
        self._width = width
        self._height = height
        # board representation
        # None - empty cell
        # <dash> - taken square
        # 'X', 'O' - explicit player moves
        self._data = [[None for i in range(self._width)] for j in range(self._height)]
        print(id(self._data[0]))
        print(id(self._data[1]))
        self._data[0][0] = 'V'

    def move(self, symbol: str, row, col: int) -> None:
        row -= 1
        col -= 1
        if symbol not in ['X', 'O']:
            raise GameException("Incorrect symbol played")
        if not (0 <= col < self._width) or not (0 <= row < self._height):
            raise GameException("Symbol is outside board!")
        if row == 0 and col == 0:
            raise GameOver("You lost!")
        if self._data[row][col] is not None:
            raise GameException("Square already played!")
        # mark the actual square
        self._data[row][col] = symbol
        # mark the other occupied squares
        for i in range(row, self._height):
            for j in range(col, self._width):
                if self._data[i][j] is None:
                    self._data[i][j] = '-'

    def get_symbol(self, row, col: int) -> str:
        # TODO To implement
        pass

    def _row_repr(self, row: list) -> list:
        result = []
        for symbol in row:
            if symbol is None:
                result.append(' ')
            else:
                result.append(symbol)
        return result

    def __str__(self):
        board = Texttable()
        # board header
        board.header(['/'] + list(range(1, self._width + 1)))

        board.add_row(['A'] + self._row_repr(self._data[0]))
        for i in range(self._height - 1):
            board.add_row([chr(ord('B') + i)] + self._row_repr(self._data[i + 1]))

        return board.draw()


class ComputerStrategy:
    def get_next_move(self, board: Board) -> tuple:
        raise NotImplementedError


class Game:
    def __init__(self, ai_strategy: ComputerStrategy, width, height: int):
        self._board = Board(width, height)
        self._ai = ai_strategy

    def move_human(self, row, col: int):
        raise NotImplementedError()

    def move_computer(self):
        # raise NotImplementedError()
        self._board.move('O', *self._ai.get_next_move(self._board))


b = Board(5, 4)
b.move('X', 4, 4)
b.move('O', 3, 3)
b.move('X', 2, 2)

print(b)
