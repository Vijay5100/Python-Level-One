"""
   1   2   3 
1 
2 
3


It prints the state of the board 

Board: 

    |   |
---------------
    |   |
---------------
    |   |

X's Turn / O's Turn 
Enter the row number: 2 
Enter the Col number: 2 
Board: 

    |   |
---------------
    | X |
---------------
    |   |
O's Turn 
Enter the row number: 
Enter the col number: 

"""
import os 
import time 
import random 

player1 = input("Enter Player 1's Name: ")
player2 = input("Enter Player 2's Name: ")

row1 = [" "," "," "] # 1 D list 
row2 = [" "," "," "]
row3 = [" "," "," "]

board = [row1,row2,row3]

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
    for row in range(3):
        for col in range(3):
            if col == 2:
                print(board[row][col],end="")
            else:
                print(board[row][col],end=" | ")
        print()
        if row != 2:
            print("----------")
    print(f"{currentplayer}'s Turn: ")
    row = int(input("Enter the row number: "))
    col = int(input("Enter the col number: "))
    # 2,2 -> 1,1 
    board[row-1][col-1] = marker
    counter += 1 
    
    # checking rows for a winner 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == marker:
            winner = True 
            break 
    
    # checking cols for winner 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == marker:
            winner = True 
            break 
   
    # checking left to right diagonal 
    if board[0][0] == board[1][1] == board[2][2] == marker:
        winner = True 
    #checking right to left diagonal 
    elif board[0][2] == board[1][1] == board[2][0] == marker:
        winner = True 
   
    print("Updating the state of the board.....")
    
    # add 1 sec delay 
    time.sleep(1)
    os.system("clear") # "cls"
    
    
    if winner:
        break 
    
    if counter == 9:
        break 
    
    turn = not turn 

print("Board: ")
for row in range(3):
    for col in range(3):
        if col == 2:
            print(board[row][col],end="")
        else:
            print(board[row][col],end=" | ")
    print()
    if row != 2:
        print("----------")
if winner: 
    print(f"{currentplayer} is the Winner!")
else:
    print("It's a Tie.")
