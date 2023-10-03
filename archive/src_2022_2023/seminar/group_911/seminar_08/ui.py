from board import game_board
from game import game, skynet_level_1, skynet_level_2


def start_game():
    board = game_board()
    # Strategy design pattern - https://en.wikipedia.org/wiki/Strategy_pattern
    # computer_player = skynet_level_1(board)
    computer_player = skynet_level_2(board)
    ttt_game = game(board, computer_player)
    humans_turn = True

    while True:
        # print(board.str_board(game_board))
        print(str(board))

        if humans_turn:
            user_input = input(">")
            command, params = user_input.split(" ", maxsplit=1)
            if command == 'play':
                params = params.split(",")
                try:
                    row = int(params[0])
                    col = int(params[1])
                    ttt_game.human_move(row, col)
                except ValueError as ve:
                    # TODO Allow user to attempt to make a move
                    print(ve)
            elif command == 'takeback':
                # Take back human's last move, if possible
                pass
            elif command == 'ragequit':
                print("Computer wins!")
                return
            else:
                print("Invalid command")
        else:
            # Computer player's turn
            row, col = ttt_game.computer_move()
            print("Computer moved at (" + str(row) + "," + str(col) + ")")
        humans_turn = not humans_turn


start_game()
