"""
User Interface for game
"""
import board
import game


def process_command(user_command):
    # remove leading and trailing whitespace
    user_command = user_command.strip()
    # split the command into two - command word and params
    tokens = user_command.split(maxsplit=1)
    # one of move, takeback, ragequit
    command_word = tokens[0]
    if len(tokens) == 1:
        return command_word, []

    tokens = tokens[1].split(",")
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()
    # command parameters
    command_params = tokens
    return command_word, command_params


def start():
    """
    move 1,1
    takeback
    ragequit
    """
    game_board = board.create_board()

    while True:
        print(board.str_board(game_board))
        user_command = input(">")
        command, params = process_command(user_command)
        if command == 'move':
            # TODO Detect when game is won
            # TODO Detect when board is full :)
            try:
                row = int(params[0])
                col = int(params[1])
                game.human_move(game_board, row, col)
                game.computer_move(game_board)
            except ValueError as ve:
                print(str(ve))


        elif command == 'ragequit':
            print("Computer won!")
            return
        else:
            print("Invalid command")


start()

# print(process_command("    move    1,     4    "))
