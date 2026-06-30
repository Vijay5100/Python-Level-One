import random 
import os 
import time 

print("""Difficulty:
1. Easy - You will get 6 words
2. Medium - You will get 8 words 
3. Hard - You will get 10 words
""")
choice = int(input("Choose the Difficulty(1-3): "))
n = 0 
difficulty = None 
if choice == 3:
    n = 6 
    difficulty = "Hard"
elif choice == 2:
    n = 5
    difficulty = "Medium"
else:
    n = 4 
    difficulty = "Easy"
    
time.sleep(2) # adding delay 
os.system("clear")
    
numbers = [] 
# this will generate 4 random numbers and store it in a list 
for i in range(n):
    number = random.randint(1,100)
    numbers.append(number)

for number in numbers:
    print(number)
    time.sleep(1) # this will add 1 sec delay 
    os.system("clear")

print("Memory Tester: ")
print(f"Difficulty : {difficulty}")
guesses = list(map(int,input("Enter the sequence: ").split(",")))

counter = 0 
score_per_correct_guess = 100/n 

for i in range(len(guesses)):
    if numbers[i] == guesses[i]:# both the values and sequence
        counter += 1 
score = counter * score_per_correct_guess

print(f"You're Score is {score}")
        
