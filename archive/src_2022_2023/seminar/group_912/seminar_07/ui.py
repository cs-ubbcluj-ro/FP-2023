"""
UI module for game

user commands:
    play 1,1  # plays in the center of the board
    takeback  # undo the user's last move
    exit
"""
import board
import game


def help_user():
    print(
        """
        play 1, 1  # plays in the center of the board
        takeback  # undo the user's last move
        exit
        """)


def process_user_command(user_command):
    """
    Return user's command and its parameters
    :param user_command:
    :return:
    """
    user_command = user_command.strip()
    tokens = user_command.split(" ", maxsplit=1)
    command = tokens[0]

    if len(tokens) == 1:
        return command, ""

    tokens = tokens[1].split(",")
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()

    return command, tokens


def start():
    game_board = board.create_board()
    help_user()

    while True:
        print(board.str_board(game_board))
        user_command = input(">")
        command, params = process_user_command(user_command)

        if command == 'play':
            try:
                row = int(params[0])
                col = int(params[1])
                game.human_move(game_board, row, col)
            except ValueError as ve:
                print(str(ve))
            else:
                pos = game.computer_move(game_board)
                print("Computer moved at " + str(pos))
        elif command == 'takeback':
            pass
        elif command == 'exit':
            return
        else:
            print("Valid commands are:")
            help_user()


# print(process_user_command("play 1,1"))
# print(process_user_command("   play     1,  1       "))

start()
