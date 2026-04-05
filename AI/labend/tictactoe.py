import random

board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
        print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def ai_move():
    # 1. try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if win("O"):
                return
            board[i] = " "
    
    # 2. block human
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if win("X"):
                board[i] = "O"
                return
            board[i] = " "
    
    # 3. random move
    empty = [i for i in range(9) if board[i] == " "]
    board[random.choice(empty)] = "O"

# Game loop
for _ in range(9):
    print_board()
    
    # Human move
    m = int(input("Enter (0-8): "))
    if board[m] != " ":
        print("Invalid"); continue
    board[m] = "X"
    
    if win("X"):
        print_board()
        print("You win")
        break
    
    # AI move
    ai_move()
    
    if win("O"):
        print_board()
        print("AI wins")
        break

else:
    print_board()
    print("Draw")

"""
AI:
1. try win
2. try block
3. random
"""
