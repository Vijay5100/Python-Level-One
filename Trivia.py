import random
print('Trivia Game')
questions = ["What is the bigges planet in our solar system?", 
"How many continents are there?", "What is the capital of Italy?",
    "What gas do humans need to breathe?",
    "What is the largest country in the world?"]

answers = ["jupiter", "7", "rome", "oxygen", "russia"]

score = 0

for i in range(5):
    print("Question:", questions[i])
    useranswer = input("Answer: ").lower()
    if useranswer.lower() == answers[randomindex]:
        print("Good Job! You earned 10 points.")
        score = score + 10
    else:
        print("Incorrect. You lost 5 points.")
        print("The correct answer was:", answers[randomindex])
        score = score - 5
    
print("Your final score is:", score)
