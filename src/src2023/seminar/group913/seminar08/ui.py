from board import Board
from game import Game


class UI:
    def start(self):
        # TODO To be continued ...
        board = Board()
        game = Game(board)

        while True:
            print(board)
            x = int(input("X="))
            y = int(input("Y="))

            game.move_human(x, y)
            game.move_computer()


ui = UI()
ui.start()
