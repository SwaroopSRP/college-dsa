board = [" "] * 9

def print_board():
    print(board[0], "   ", board[1], "   ", board[2])
    print()
    print(board[3], "   ", board[4], "   ", board[5])
    print()
    print(board[6], "   ", board[7], "   ", board[8])

def check_winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    
    for a,b,c in win:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

player = "X"

for turn in range(9):
    print_board()
    move = int(input("Enter position (0-8): "))
    
    if board[move] == " ":
        board[move] = player
        
        if check_winner(player):
            print_board()
            print(player, "wins!")
            break
        
        player = "O" if player == "X" else "X"
    else:
        print("Invalid move")

else:
    print("Draw")

"""
1. board = [" "] * 9
2. print_board()
3. check_winner()
4. loop 9 turns
5. switch player
"""
