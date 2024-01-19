from src2023.seminar.group913.seminar13.minesweeper import Minefield, GameOver


class UI:

    def __init__(self):
        self.__minefield = None

    def __print_start_menu(self):
        print("1. Start easy")
        print("2. Start hard")
        print("0. Exit")

    def start(self):
        while True:
            self.__print_start_menu()
            opt = input(">").strip()
            if opt == "1":
                self.__minefield = Minefield(4, 5, 3)
                break
            elif opt == "2":
                self.__minefield = Minefield(8, 10, 11)
                break
            elif opt == "0":
                print("Bye!")
                return
            else:
                print("Invalid option!")
        self.__play()

    def __play(self):
        try:
            while True:
                try:
                    print(self.__minefield)
                    opt = input(">").strip()

                    if opt.startswith("reveal"):
                        tokens = opt.split(" ")
                        coordinates = tokens[1]
                        col = ord(coordinates[0]) - ord('A')
                        row = int(coordinates[1]) - 1
                        self.__minefield.click(row, col)
                except ValueError as ve:
                    print(ve)
        except GameOver:
            print("All your base are belong to us!")


if __name__ == "__main__":
    ui = UI()
    ui.start()
