from board import create_board, to_str, is_board_won, is_board_drawn
from game import move_human, move_computer

# FIXME Error handling, other details :)
board = create_board()
turn = 1  # X plays

while True:
    print(to_str(board))

    if turn == 1:
        row = int(input("X="))
        col = int(input("Y="))
        move_human(board, row, col)
    else:
        move_computer(board)

    if is_board_won(board):
        if turn == 1:
            print("Congrats!")
        else:
            print("Comiserations!")
        break

    if is_board_drawn(board):
        print("draw!")
        break
    turn = 1 - turn
