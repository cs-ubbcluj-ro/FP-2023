"""
Human and computer moves
"""
import board
from random import choice


def human_move(game_board, row, col):
    board.move_on_board(game_board, 'X', row, col)


def computer_move(game_board):
    positions = []
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            if board.get_symbol(game_board, row, col) is None:
                positions.append((row, col))
    pos = choice(positions)
    board.move_on_board(game_board, 'O', pos[0], pos[1])
    return pos
