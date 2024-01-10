import random

from domain import PlayerBoard, TargetBoard
from random import randint, choice


class ComputerPlayer:
    def __init__(self, player_board: PlayerBoard, target_board: TargetBoard):
        self.__player_board = player_board
        self.__target_board = target_board

        # all the coordinates that the computer has not fired upon yet
        self.__candidates = []
        for i in range(self.__target_board.size):
            for j in range(self.__target_board.size):
                self.__candidates.append((i, j))

        # all the coordinates that were hits
        self.__hits = set()
        # all the coordinates that were misses
        self.__misses = set()

    def place_ship(self):
        row = randint(0, self.__target_board.size - 1)
        column = randint(0, self.__target_board.size - 3)
        self.__target_board.place_ship(row, column)

    def fire(self):
        target = choice(self.__candidates)
        self.__candidates.remove(target)
        if self.__player_board.fire(*target):
            self.__hits.add(target)
        else:
            self.__misses.add(target)


player_board = PlayerBoard()
player_board.place_ship(1, 2)

target_board = TargetBoard()
ai = ComputerPlayer(player_board, target_board)
ai.place_ship()

for i in range(5):
    ai.fire()

print(target_board)
print(player_board)
