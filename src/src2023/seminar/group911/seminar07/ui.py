from board import create_board, to_str
from game import human_move, computer_move

# import board

"""
    UI module --> calls Game module
    UI module --> calls Board module
  Game module --> Board module

  function calls go in a single direction between the modules
"""

board = create_board()

# TODO Check game has ended, victory conditions, error
# handling for input, ...
while True:
    print(to_str(board))
    x = int(input("x="))
    y = int(input("y="))
    human_move(board, x, y)
    computer_move(board)
