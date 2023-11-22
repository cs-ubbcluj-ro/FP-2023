import game
from board import generate_board, to_str, get_board_status
from ui import *




def start():
    board_game = generate_board()

    is_running = True
    user_turn = True
    while is_running:
        print('The current board is:')
        print(to_str(board_game))
        if user_turn:

            user_input = input(">>>").strip()
            command, params = user_input.split(" ", maxsplit=1)
            if command == 'play':
                try:
                    x, y = check_play_cmd_params(params)
                    game.make_user_move(board_game, x, y, 'X')
                    print("User wants to put an X on row", x, "column", y)
                except ValueError as v:
                    print("Error occurred %s" % v)
                    continue
            elif command == 'exit':
                is_running = False
        else:
            row, column = game.make_computer_move(board_game, 'O')
            print("Computer moved to put an O on row", row, "column", column)

        board_status = get_board_status(board_game)
        if board_status == 1:
            print(to_str(board_game))
            print('Game was won by human player.')
            return
        elif board_status == 2:
            print(to_str(board_game))
            print('Game was won by computer player.')
            return
        elif board_status == 0:
            print(to_str(board_game))
            print('Game results in a draw.')
            return

        user_turn = not user_turn


if __name__ == "__main__":
    start()
