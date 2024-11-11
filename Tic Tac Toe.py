def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the current player has won the game."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check reverse diagonal
        return True
    return False


def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)


def player_move(board, player):
    """Handles the player's move. Ensures valid input."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 9.")


def main():
    """Main function to play Tic Tac Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']  # Player X and O
    current_player = 0  # Start with player X

    # Game loop
    while True:
        print_board(board)
        player_move(board, players[current_player])

        # Check if current player has won
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        # Check if board is full (tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 1 - current_player


if __name__ == "__main__":
    main()
