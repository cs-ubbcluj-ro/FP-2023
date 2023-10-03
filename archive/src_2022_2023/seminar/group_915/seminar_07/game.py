"""
Game playing code
"""
import board
from random import choice


def human_move(game_board, row, col):
    board.make_move(game_board, row, col, 'X')


def computer_move(game_board):
    positions = []
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            if board.get_symbol(game_board, row, col) == ' ':
                positions.append((row, col))
    pos = choice(positions)
    board.make_move(game_board, pos[0], pos[1], 'O')
