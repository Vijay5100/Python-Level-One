import random 
import os 
import time 

print("""Difficulty:
1. Easy - You will get 4 words 
2. Medium - You will get 6 words 
3. Hard - You will get 8 words
""")

word = [
    "dog",
    "cat",
    "car",
    "truck",
    "apple",
    "banana",
    "number",
    "idea",
    "lightning",
    "dark"
]

choice = int(input("Choose the Difficulty(1-3): "))
n = 0 
difficulty = None 
if choice == 3:
    n = 8 
    difficulty = "Hard"
elif choice == 2:
    n = 6
    difficulty = "Medium"
else:
    n = 4
    difficulty = "Easy"
    
time.sleep(2) # adding delay 
os.system("clear")
    
words = [] 
# this will generate 4 random numbers and store it in a list 
for i in range(n):
    number = random.randint(0,9)
    words.append(word[number])

for word in words:
    print(word)
    time.sleep(1) # this will add 1 sec delay 
    os.system("clear")

print("Memory Tester: ")
print(f"Difficulty : {difficulty}")
guesses = (input("Enter the sequence of Words: ").split(","))

counter = 0 
score_per_correct_guess = 100/n 

for i in range(len(guesses)):
    if words[i] == guesses[i]:# both the values and sequence
        counter += 1 
score = counter * score_per_correct_guess

print(f"You're Score is {score}")
        
