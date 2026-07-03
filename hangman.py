import time 
import os 
import random 

max_lives = 6

movie_words = ["Titanic","Frozen","Jaws","Avatar","Coco","Shrek","Rocky","Cars"]
movie_hints = ["iceberg","princess","shark","planet","music","ogre","boxing","racing"]
hangman_stages = [
"""
 +---+
 | |
   |
   |
   |
   |
=========
""",
"""
 +---+
 | |
 O |
   |
   |
   |
=========
""",
"""
+---+
| |
O |
| |
  |
  |
=========
""",
"""
 +---+
 | |
 O |
/| |
   |
   |
=========
""",

"""
 +---+
 | |
 O |
/|\\|
   |
   |
=========
""",
"""
 +---+
 | |
 O |
/|\\|
/  |
   |
=========
""",
"""
 +---+
 | |
 O |
/|\\|
/ \\|
   |
=========
"""
]

index = random.randint(0,len(movie_words)-1)
word = movie_words[index]
hint = movie_hints[index]
num_characters = len(word)
guess = ["_" for i in range(num_characters)]
count = 0 # index for the characters 
body = 0 
rounds_won = 0

while True:
    print("Hangman:")
    print(hangman_stages[body])
    if count == num_characters:
        print("Congragulation, You have won.")
        round_wons += 1
        break
    if body > max_lives + 1:
        break
    print(" ".join(guess))
    print(f"Hint: {hint.title()}")
    character = input(f"Guess the character-{count+1}: ")
    print("Checking...")
    time.sleep(2)
    if character.lower() == word[count].lower():
        guess[count] = character
        print("Result: Correct")
        count += 1 
    else:
        body += 1
        match body:
            case _ if body == max_lives + 1:
                print(f"Out of guesses! The word was: {word}")
                break
            case 1:
                print("head was drawn")
            case 2:
                print("body was drawn")
            case 3:
                print("left hand was drawn")
            case 4:
                print("right hand was drawn")
            case 5:
                print("left leg was drawn")
            case 6:
                print("right leg was drawn")
                print("Game Over!")
                print(f"The word was: {word}")
    time.sleep(2)
    os.system("clear")
print(f"You won {rounds_won} time(s) this session.")
