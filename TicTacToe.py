import sys

'''
Written By-
Hardik Sharma Phuyal
With Love and Passion :D
'''

print('''
Please read this before starting the game:
  Row/Column instruction commands-
    0 = 1
    1 = 2
    2 = 3
Enjoy :D
''')

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
def add_X():
    row = int(input("Player 1 (X), Enter row (0-2): "))
    col = int(input("Player 1 (X), Enter column (0-2): "))
    if row > 2 or row < 0 or col > 2 or col < 0:
        sys.exit("Invalid move. Please restart the game.")
    if board[row][col] != 0:
        sys.exit("That spot is already taken. Please restart the game.")
    board[row][col] = "X"

def add_O():
    row = int(input("Player 2 (O), Enter row (0-2): "))
    col = int(input("Player 2 (O), Enter column (0-2): "))
    if row > 2 or row < 0 or col > 2 or col < 0:
        sys.exit("Invalid move. Please restart the game.")
    if board[row][col] != 0:
        sys.exit("That spot is already taken. Please restart the game.")
    board[row][col] = "O"
def print_board():
    for row in board:
        print(" | ".join(str(cell) if cell != 0 else " " for cell in row))
    print()
def check_win(symbol):
    return (
        any(all(cell == symbol for cell in row) for row in board) or
        any(all(row[i] == symbol for row in board) for i in range(3)) or
        all(board[i][i] == symbol for i in range(3)) or
        all(board[i][2 - i] == symbol for i in range(3))
    )
for turn in range(9): 
    print_board()
    if turn % 2 == 0:
        add_X()
        if check_win("X"):
            print_board()
            sys.exit("🎉 Congrats Player 1! You won.")
    else:
        add_O()
        if check_win("O"):
            print_board()
            sys.exit("🎉 Congrats Player 2! You won.")

print_board()
print("It's a draw!")
