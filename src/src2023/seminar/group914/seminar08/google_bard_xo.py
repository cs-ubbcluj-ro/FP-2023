class Board:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def display_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=' ')
            print()

    def check_win(self, player):
        # Check for horizontal wins
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check for vertical wins
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check for diagonal wins
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def make_move(self, player, position):
        row = position // 3
        col = position % 3

        if self.board[row][col] != '-':
            return False

        self.board[row][col] = player
        return True

    def check_available_moves(self):
        available_moves = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    available_moves.append(row * 3 + col)

        return available_moves

    def is_full(self):
        return all(cell != '-' for row in self.board for cell in row)


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_move(self, board):
        print(f"{self.name}'s turn...")

        while True:
            position = int(input(f"Enter your move ({self.mark}): "))

            if board.make_move(self.mark, position):
                break
            else:
                print("Invalid move. Please try again.")


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer", 'O')

    def make_move(self, board):
        print(f"{self.name}'s turn...")

        available_moves = board.check_available_moves()
        best_move = None

        for move in available_moves:
            board.make_move(self.mark, move)
            if board.check_win(self.mark):
                best_move = move
                board.make_move('-', move)  # Undo the move
                break
            else:
                board.make_move('-', move)  # Undo the move

        if not best_move:
            # Choose a random move
            best_move = random.choice(available_moves)

        board.make_move(self.mark, best_move)


def play_game():
    board = Board()
    human_player = Player("Human", 'X')
    computer_player = ComputerPlayer()

    current_player = human_player

    while True:
        board.display_board()

        current_player.make_move(board)

        if board.check_win(current_player.mark):
            board.display_board()
            print(f"{current_player.name} wins!")
            break

        if board.is_full():
            board.display_board()
            print("It's a tie!")
            break

        current_player = computer_player if current_player == human_player else human_player


if __name__ == "__main__":
    play_game()
