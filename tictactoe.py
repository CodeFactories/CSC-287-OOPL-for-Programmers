print()
print("Welcome to our tictactoe game")
print()

# Reprsent the board using a list
board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

# Function to display the list as a board.
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

# Player's move function
def user_move(board, player):
    while True:
        move = input(f"Player {player}: Enter a number (1-9): ")
        if move in board:
            index = int(move) - 1
            board[index] = player
            break
        else:
            print(" Invalid move. Please choose an available number.")
            print()

# Function for draw
def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

# Check Win Function
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Start with Player X
current_player = 'X'

# Game loop
while True:
    display_board(board)
    user_move(board, current_player)

    # Check win
    if check_win(board, current_player):
        display_board(board)
        print(f" Player {current_player} wins!")
        break

    current_player = 'O' if current_player == 'X' else 'X'

    # Check draw
    if is_draw(board):
        display_board(board)
        print(" It's a draw!")
        break