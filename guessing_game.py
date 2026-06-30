'''
Guess the Number

1. Randomly generante a number 
2. Enter a number 
if the guess > actual_number "Greater"
if the guess < actual_number "Smaller"
Repeat until the guess == actual_number 
'''
import random

number = random.randint(1,100) # will generate random number between 1 to 100 
counter = 0 
while True:
    guess = int(input("Guess the number (1-100): "))
    counter += 1 
    if guess > number:
        print("Greater, Try a smaller Number")
    elif guess < number: 
        print("Smaller, Try a bigger Number")
    else:
        print("You're guess is correct")
        print(f"You have taken {counter} attempts.")
        break 
