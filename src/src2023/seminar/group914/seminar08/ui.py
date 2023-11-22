from board import Board
from game import Game, ComputerPlayerFirstSquare, ComputerPlayerSmarter


class UI:

    def __init__(self):
        self.__ai = None

    def start(self):
        board = Board()
        """
        Change the ai = ... line to another computer player in order to play better
        Instance of the Strategy design pattern
            https://refactoring.guru/design-patterns/strategy
        """
        ai = ComputerPlayerFirstSquare(board)
        # ai = ComputerPlayerSmarter(board)
        game = Game(board, ai)
        turn = 1  # X plays

        while True:
            print(game.get_board())

            if turn == 1:
                try:
                    row = int(input("X="))
                    col = int(input("Y="))
                    game.move_human(row, col)
                except ValueError as ve:
                    print(str(ve))
                    continue
                    # turn = 1 - turn
            else:
                x, y = game.move_computer()
                print("Computer moves at " + str(x) + ", " + str(y))

            if game.get_board().is_won():
                if turn == 1:
                    print("Congrats!")
                else:
                    print("Comiserations!")
                break

            if game.get_board().is_full():
                print("draw!")
                break
            turn = 1 - turn


ui = UI()
ui.start()
