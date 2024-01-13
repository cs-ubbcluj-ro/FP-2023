from colorama import Fore, Style

from src2023.seminar.group917.Seminar_13.RepoExceptions import RepositoryExceptions
from src2023.seminar.group917.Seminar_13.game import ComputerPlayer
from src2023.seminar.group917.Seminar_13.board import BattleshipsBoard, PlayerBoard, ComputerBoard, GameOver


class Console:
    def __init__(self):
        self.__user_board = PlayerBoard()
        self.__computer_board = ComputerBoard()
        self.__computer_player = ComputerPlayer(self.__computer_board, self.__user_board)

    def __place_user_ship(self):
        try:
            print("Place ship:")
            row = int(input("Row:"))
            column = int(input("Column:"))
            self.__user_board.place_ship(row, column)

        except RepositoryExceptions as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            self.__place_user_ship()

    def print_current_game_state(self):
        #Moved to function & added colors
        print(Fore.YELLOW)
        print('The computer\'s board')
        print(self.__computer_board)
        print(Style.RESET_ALL)
        print(Fore.BLUE)
        print('The user board (my board):')
        print(self.__user_board)
        print(Style.RESET_ALL)



    def start_game(self):

        self.__computer_player.place_ship()
        self.__place_user_ship()

        human_player_turn = True
        while True:
            if human_player_turn:
                print("Input coordinates for hit:")
                row = int(input("Row:"))
                column = int(input("Column:"))
                try:
                    self.__computer_board.hit(row, column)
                    human_player_turn = False
                    self.print_current_game_state()

                except GameOver as e:
                    print("Human has won the game.")
                    break
                except RepositoryExceptions as e:
                    print(e)
            else:
                try:
                    computer_attempt = self.__computer_player.hit()
                    row, column = computer_attempt
                    print("Computer player attempting to hit:", row, column)
                    human_player_turn = True
                    self.print_current_game_state()

                except GameOver as e:
                    print("Computer has won the game.")
                    break
                except RepositoryExceptions as e:
                    print(e)

