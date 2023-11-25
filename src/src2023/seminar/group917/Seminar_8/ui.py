from src2023.seminar.group917.Seminar_8.board import Board
from src2023.seminar.group917.Seminar_8.game import Game, ComputerRandomMoves, ComputerBetterStrategy


class UI:
    def __init__(self):
        pass

    def check_play_cmd_params(self, parameters: str):
        elems = parameters.split(" ")
        if len(elems) != 2:
            raise ValueError("Incorrect number of parameters!")

        is_digit = elems[0].isdigit() and elems[1].isdigit()

        if not is_digit:
            raise ValueError("Incorrect parameters - should be numbers!")

        return int(elems[0]), int(elems[1])

    def get_computer_player(self, game_level = 'easy'):
        #Read more about the Strategy pattern here:
        #https://refactoring.guru/design-patterns/strategy

        if game_level == 'easy':
            return ComputerRandomMoves()
        elif game_level == 'hard':
            return ComputerBetterStrategy()
        else:
            raise ValueError('Cannot start game. Difficulty level does not exist.')

    def start(self):

        board_game = Board()
        computer_player = self.get_computer_player('easy')
        game = Game(board_game, computer_player)

        is_running = True
        user_turn = True

        while is_running:
            print('The current board is:')
            print(board_game)
            if user_turn:

                user_input = input(">>>").strip()
                command, params = user_input.split(" ", maxsplit=1)
                if command == 'play':
                    try:
                        x, y = self.check_play_cmd_params(params)
                        game.make_user_move(x, y, 'X')
                        print("User wants to put an X on row", x, "column", y)
                    except ValueError as v:
                        print("Error occurred %s" % v)
                        continue
                elif command == 'exit':
                    is_running = False
            else:
                row, column = game.make_computer_move('O')
                print("Computer moved to put an O on row", row, "column", column)

            board_status = board_game.get_board_status()
            if board_status == 1:
                print(board_game)
                print('Game was won by human player.')
                return
            elif board_status == 2:
                print(board_game)
                print('Game was won by computer player.')
                return
            elif board_status == 0:
                print(board_game)
                print('Game results in a draw.')
                return

            user_turn = not user_turn


