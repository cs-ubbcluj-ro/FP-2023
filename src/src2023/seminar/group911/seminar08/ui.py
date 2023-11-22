from game import Game
from board import Board


class UI:
    def start(self):
        board = Board()
        game = Game(board)

        # TODO Check game has ended, victory conditions, error
        # handling for input, ...
        while True:
            print(board)
            x = int(input("x="))
            y = int(input("y="))
            game.human_move(x, y)
            game.computer_move()


ui = UI()
ui.start()
