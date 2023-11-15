from game import move_computer, move_human
from board import create_board, to_str

# TODO To be continued ...
board = create_board()

while True:
    print(to_str(board))
    x = int(input("X="))
    y = int(input("Y="))

    move_human(board, x, y)
    move_computer(board)
