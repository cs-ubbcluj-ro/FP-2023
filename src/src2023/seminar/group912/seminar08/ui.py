from game import Game, computer_player_level_1, computer_player_level_2
from board import Board


class UI:
    def start(self):
        #
        # computer player uses the Strategy design pattern
        # https://refactoring.guru/design-patterns/strategy
        #
        levels = {"1": computer_player_level_1, "2": computer_player_level_2}
        level = "1"  # set a default level

        level_selected = False
        while not level_selected:
            level = input("Computer level=")

            if level not in levels:
                print("Valid levels are " + str(levels.keys()))
            else:
                level_selected = True

        game = Game(levels[level])
        game_board = game.get_board()
        human_move = True

        while True:
            print(game_board)

            if human_move:
                try:
                    x = int(input("x="))
                    y = int(input("y="))
                    game.human_move(x, y)
                except ValueError as ve:
                    print(ve)
                    continue

            else:
                game.computer_move()

            if game_board.is_won():
                if human_move:
                    print("You won! Congrats!")
                else:
                    print("All your base are belong to us!")
                print(game_board)
                break
            elif game_board.is_full():
                print("Game is a draw :-|")
                break

            human_move = not human_move


ui = UI()
ui.start()
