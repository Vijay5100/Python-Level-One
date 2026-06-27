import os 
import time 
import random 

player1 = input("Enter Player 1's Name: ")
player2 = input("Enter Player 2's Name: ")

row1 = [" "," "," "," "]
row2 = [" "," "," "," "]
row3 = [" "," "," "," "]
row4 = [" "," "," "," "]

rows = 4 
cols = 4

board = [row1,row2,row3,row4]

turn = False if random.randint(0,1) %2 == 0 else True
winner =  False
counter = 0 

while True:
    if turn == False:
        marker = "X"
        currentplayer = player1
    else:
        marker = "O"
        currentplayer = player2
    print("Board: ")
    for row in range(4):
        for col in range(4):
            if col == 3:
                print(board[row][col],end="")
            else:
                print(board[row][col],end=" | ")
        print()
        if row != 3:
            print("-------------")
    print(f"{currentplayer}'s Turn: ")
    row = int(input("Enter the row number: "))
    col = int(input("Enter the col number: "))
    # valid index check 
    if row-1 < 0 or row-1>=rows or col-1 < 0 or col-1 >= cols:
        print("Sorry unable to place the marker. Due to Invalid row/col value. Try again.")
        continue
    elif board[row-1][col-1] != " ":
        print("Sorry unable to place the marker. Due to the slot is already occupied. Try again")
        continue
    # 2,2 -> 1,1 
    board[row-1][col-1] = marker
    counter += 1 
    
    # checking rows for a winner 
    for row in range(rows):
        if board[row][0] == board[row][1] == board[row][2] == board[row][3] == marker:
            winner = True 
            break 
    
    # checking cols for winner 
    for col in range(cols):
        if board[0][col] == board[1][col] == board[2][col] == board[3][col] == marker:
            winner = True 
            break 
   
    # checking left to right diagonal 
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == marker:
        winner = True 
    #checking right to left diagonal 
    elif board[0][3] == board[1][2] == board[2][1] == board[3][0] == marker:
        winner = True 
   
    print("Updating the state of the board.....")
    
    # add 1 sec delay 
    time.sleep(1)
    os.system("clear") # "cls"
    
    
    if winner:
        break 
    
    if counter == 16:
        break 
    
    turn = not turn 

print("Board: ")
for row in range(rows):
    for col in range(cols):
        if col == 3:
            print(board[row][col],end="")
        else:
            print(board[row][col],end=" | ")
    print()
    if row != 3:
        print("-------------")
if winner: 
    print(f"{currentplayer} is the Winner!")
else:
    print("It's a Tie.")
