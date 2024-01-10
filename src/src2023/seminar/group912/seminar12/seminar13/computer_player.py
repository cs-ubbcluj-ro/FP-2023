from src2023.seminar.group912.seminar12.seminar13.board import TargetBoard, PlayerBoard
from random import randint, choice


class ComputerPlayer:
    def __init__(self, target_board: TargetBoard, player_board: PlayerBoard):
        self.__target_board = target_board
        self.__player_board = player_board

        self.__targets = list(range(self.__player_board.size ** 2))
        self.__hits = []
        self.__misses = []

    def place_ship(self):
        row = randint(0, self.__target_board.size - 1)
        column = randint(0, self.__target_board.size - 3)
        self.__target_board.place_ship(row, column)

    def fire(self):
        target = choice(self.__targets)
        self.__targets.remove(target)

        # 23 -> row 4, column 3
        result = self.__player_board.fire(target // self.__player_board.size, target % self.__player_board.size)
        if result:
            self.__hits.append(target)
        else:
            self.__misses.append(target)


if __name__ == "__main__":
    tb = TargetBoard()
    pb = PlayerBoard()
    pb.place_ship(2, 2)

    ai = ComputerPlayer(target_board=tb, player_board=pb)
    for i in range(5):
        ai.fire()

    print(pb)
