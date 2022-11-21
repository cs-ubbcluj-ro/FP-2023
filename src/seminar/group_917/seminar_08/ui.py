import sys

import board
import game

"""
move 1,1
takeback
ragequit
"""


def read_command():
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


def start():
    game_board = board.create_board()
    # game_board[1][1] = "abcd"
    human_move = True

    while True:
        print(board.str_board(game_board))

        if human_move:
            command, params = read_command()
            if command == 'move':
                params = params.split(",")
                try:
                    row = int(params[0])
                    col = int(params[1])
                    game.play_human(game_board, row, col)
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
            row, col = game.play_computer(game_board)
            print("Computer moved at (" + str(row) + "," + str(col) + ")")

        # TODO Is board full?
        # TODO Is the game won?
        human_move = not human_move

start()