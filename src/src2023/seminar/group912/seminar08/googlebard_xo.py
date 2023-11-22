class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class Cell:
    def __init__(self):
        self.marked = False
        self.symbol = None

    def mark(self, player):
        if not self.marked:
            self.marked = True
            self.symbol = player.symbol


class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]

    def print(self):
        for row in self.cells:
            for cell in row:
                if cell.marked:
                    print(cell.symbol, end=" ")
                else:
                    print("-", end=" ")
            print()

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if not cell.marked:
                    return False
        return True

    def check_win(self, player):
        winning_conditions = [
            [self.cells[0][0], self.cells[0][1], self.cells[0][2]],
            [self.cells[1][0], self.cells[1][1], self.cells[1][2]],
            [self.cells[2][0], self.cells[2][1], self.cells[2][2]],
            [self.cells[0][0], self.cells[1][0], self.cells[2][0]],
            [self.cells[0][1], self.cells[1][1], self.cells[2][1]],
            [self.cells[0][2], self.cells[1][2], self.cells[2][2]],
            [self.cells[0][0], self.cells[1][1], self.cells[2][2]],
            [self.cells[0][2], self.cells[1][1], self.cells[2][0]],
        ]

        for condition in winning_conditions:
            if all(cell.symbol == player.symbol for cell in condition):
                return True
        return False


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        while True:
            self.board.print()

            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if self.board.check_win(self.current_player):
                self.board.print()
                print("Player", self.current_player.symbol, "wins!")
                break

            if not self.board.cells[row][col].marked:
                self.board.cells[row][col].mark(self.current_player)
                self.switch_player()



            if self.board.is_full():
                self.board.print()
                print("It's a tie!")
                break


game = Game()
game.play()
