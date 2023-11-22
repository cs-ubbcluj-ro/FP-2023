class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--|---|--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--|---|--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. The position is already occupied.")

    def human_move(self):
        position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1

        if 0 <= position <= 8 and self.board[position] == ' ':
            self.make_move(position)
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

    def computer_move(self):
        best_score = float('-inf')
        best_move = -1

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(False)
                self.board[i] = ' '

                if score > best_score:
                    best_score = score
                    best_move = i

        self.make_move(best_move)

    def minimax(self, maximizing_player):
        scores = {'X': -1, 'O': 1, 'Tie': 0}

        if self.check_winner():
            if self.current_player == 'X':
                return -1  # Favorable score for the human player
            else:
                return 1  # Favorable score for the computer player
        elif self.is_board_full():
            return scores['Tie']

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    eval = self.minimax(False)
                    self.board[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    eval = self.minimax(True)
                    self.board[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True  # We have a winner

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def play_game(self):
        while not self.check_winner() and not self.is_board_full():
            self.display_board()

            if self.current_player == 'X':
                self.human_move()
            else:
                self.computer_move()

        self.display_board()

        if self.check_winner():
            print(f"Player {self.current_player} wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
