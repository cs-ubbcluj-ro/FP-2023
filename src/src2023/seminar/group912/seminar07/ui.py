import game
import board


def start():
    game_board = board.create_board()
    human_move = True

    while True:
        print(board.to_str(game_board))

        if human_move:

            try:
                x = int(input("x="))
                y = int(input("y="))
                game.human_move(game_board, x, y)
            except ValueError as ve:
                print(ve)
                continue

        else:
            game.computer_move(game_board)

        if board.is_board_won(game_board):
            if human_move:
                print("You won! Congrats!")
            else:
                print("All your base are belong to us!")
            print(board.to_str(game_board))
            break
        elif board.is_board_drawn(game_board):
            print("Game is a draw :-|")
            break

        human_move = not human_move


start()
