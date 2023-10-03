import sys

from board import game_board
from game import game, computer_player_lvl_1, computer_player_lvl_2

"""
move 1,1
takeback
ragequit
"""


class UI:
    def __read_command(self):
        """
        :return: (user_command,user_parameters) tuple
        """
        user_command = input(">")

        index = user_command.find(" ")
        if index == -1:
            return user_command, None
        command = user_command[:index]
        params = user_command[index:]
        return command, params

    def start(self):
        board = game_board()
        # tic_tac_toe = game(board, computer_player_lvl_1())
        tic_tac_toe = game(board, computer_player_lvl_2())
        # game_board[1][1] = "abcd"
        human_move = True

        while True:
            # print(board.str_board(game_board))
            print(str(board))

            if human_move:
                command, params = self.__read_command()
                if command == 'move':
                    params = params.split(",")
                    try:
                        row = int(params[0])
                        col = int(params[1])
                        tic_tac_toe.play_human(row, col)
                    except ValueError as ve:
                        print("try again -- " + str(ve))
                        continue
                        # Flipping the flag twice allows the human to try again
                        # human_move = not human_move
                elif command == 'ragequit':
                    print("Computer wins!")
                    return
                else:
                    print("Invalid command")
            else:
                row, col = tic_tac_toe.play_computer()
                print("Computer moved at (" + str(row) + "," + str(col) + ")")

            # TODO Is board full?
            # TODO Is the game won?
            human_move = not human_move


ui = UI()
ui.start()
