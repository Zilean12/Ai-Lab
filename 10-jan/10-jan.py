import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    # Check rows and columns
    for p in range(3):
        if all(board[p][q] == player for q in range(3)) or all(board[q][p] == player for q in range(3)):
            return True

    # Check diagonals
    if all(board[p][p] == player for p in range(3)) or all(board[p][2 - p] == player for p in range(3)):
        return True

    return False

def check_Null_positions(board):
    return [(p, q) for p in range(3) for q in range(3) if board[p][q] == ' ']

def Best_Move(board):
    # Rule A
    for p in range(3):
        if board[p].count('x') == 2 and board[p].count(' ') == 1:
            q = board[p].index(' ')
            board[p][q] = 'x'
            return

        if [board[q][p] for q in range(3)].count('x') == 2 and [board[q][p] for q in range(3)].count(' ') == 1:
            q = [board[q][p] for q in range(3)].index(' ')
            board[q][p] = 'x'
            return

    # Rule B
    for p in range(3):
        if board[p].count('O') == 2 and board[p].count(' ') == 1:
            q = board[p].index(' ')
            board[p][q] = 'x'
            return

        if [board[q][p] for q in range(3)].count('o') == 2 and [board[q][p] for q in range(3)].count(' ') == 1:
            q = [board[q][p] for q in range(3)].index(' ')
            board[q][p] = 'x'
            return

    # Rule C
    for p in range(3):
        if board[p].count('x') == 1 and board[p].count(' ') == 2:
            q = board[p].index(' ')
            board[p][q] = 'x'
            return

        if [board[q][p] for q in range(3)].count('x') == 1 and [board[q][p] for q in range(3)].count(' ') == 2:
            q = [board[q][p] for q in range(3)].index(' ')
            board[q][p] = 'x'
            return

    # Rule D
    for p in range(3):
        if board[p].count('O') == 1 and board[p].count(' ') == 2:
            q = board[p].index(' ')
            board[p][q] = 'x'
            return

        if [board[q][p] for q in range(3)].count('O') == 1 and [board[q][p] for q in range(3)].count(' ') == 2:
            q = [board[q][p] for q in range(3)].index(' ')
            board[q][p] = 'x'
            return

    # Rule E
    Null_positions = check_Null_positions(board)
    if Null_positions:
        p, q = random.choice(Null_positions)
        board[p][q] = 'x'
        return

def main():
    board = [[' ']*3 for _ in range(3)]

    while True:
        print_board(board)

        # Player 'x' move
        Best_Move(board)

        # Check if 'x' wins
        if check_winner(board, 'x'):
            print_board(board)
            print("Player 'x' wins!")
            break

        # draw
        if not check_Null_positions(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

        # Player 'O' move
        p, q = map(int, input("Enter row and column for 'O' (e.g., 1 2): ").split())
        if board[p-1][q-1] == ' ':
            board[p-1][q-1] = 'O'
        else:
            print("Invalid move!")
            continue

        # Check if 'O' wins
        if check_winner(board, 'O'):
            print_board(board)
            print("Player 'O' wins!")
            break

if __name__ == "__main__":
    main()
