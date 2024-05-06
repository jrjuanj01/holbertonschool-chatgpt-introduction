def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.

    Parameters:
    - board (list): A 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("__" * 5)

def check_winner(board):
    """
    Check if there is a winner on the Tic-Tac-Toe board.

    Parameters:
    - board (list): A 2D list representing the game board.

    Returns:
    - bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Implement the main game logic for Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and any(" " in row for row in board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        except IndexError:
            print("Invalid input. Please enter a number within the range (0, 1, or 2).")
            continue
        board[row][col] = player
        player = "O" if player == "X" else "X"  # Update player after each move
    print_board(board)
    
    # After the game loop ends, check for the winner
    if check_winner(board):
        # If there's a winner, the player symbol should be switched back
        player = "O" if player == "X" else "X"
        print("Player " + player + " wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()