from src2023.seminar.group912.seminar12.seminar13.board import PlayerBoard, TargetBoard, BattleshipError, GameOver
from src2023.seminar.group912.seminar12.seminar13.computer_player import ComputerPlayer


class UI:
    def __init__(self):
        self.__player_board = PlayerBoard()
        self.__target_board = TargetBoard()
        self.__computer = ComputerPlayer(self.__target_board, self.__player_board)

    def __place_ship(self):
        location = input("Where to place ship>")
        # TODO Error handling
        # B2
        column = ord(location[0]) - ord('A')
        row = int(location[1]) - 1
        self.__player_board.place_ship(row, column)

    def start(self):
        self.__computer.place_ship()
        self.__place_ship()

        print("Welcome to Battleships!")

        while True:
            print("Player")
            print(self.__player_board)
            print("Computer")
            print(self.__target_board)

            try:
                target = input("Where to fire>")
                row = int(target[1]) - 1
                column = ord(target[0]) - ord('A')
                self.__target_board.fire(row, column)
            except GameOver:
                print("Congrats human player !")
                break
            except BattleshipError as ve:
                print(ve)
                continue

            try:
                self.__computer.fire()
            except GameOver:
                print("You lost !")
                break


ui = UI()
ui.start()
