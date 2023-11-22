import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = (i, j)
    return best_move

def get_player_move():
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column separated by space): ").split())
            if not (0 <= row < 3) or not (0 <= col < 3) or board[row][col] != ' ':
                raise ValueError("Invalid move. Please enter valid and unoccupied row and column numbers.")
            return row, col
        except ValueError as e:
            print(e)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row, col = get_player_move()
        board[row][col] = 'X'

        # Check if player wins
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer's move
        print("Computer's move:")
        row, col = get_best_move(board)
        board[row][col] = 'O'

        # Check if computer wins
        if is_winner(board, 'O'):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
