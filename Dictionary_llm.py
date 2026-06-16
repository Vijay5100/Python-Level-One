print("Dictionary LLM:")

######### Questions ########
question1 = "What does resilient mean?"
question2 = "What does curious mean?"
question3 = "What does ancient mean?"
question4 = "What does fragile mean?"
question5 = "What does enormous mean?"
question6 = "What does cautious mean?"
question7 = "What does generous mean?"
question8 = "What does scarce mean?"
question9 = "What does predict mean?"
question10 = "What does observe mean?"

######### Answers ########
answer1 = "being able to recover quickly from difficulty."
answer2 = "wanting to learn or know something."
answer3 = "from a long time ago."
answer4 = "Easily broken or damaged."
answer5 = "super large."
answer6 = "careful to avoid danger."
answer7 = "being able to give to others easily"
answer8 = "difficult to get because there is not much available."
answer9 = "to make a guess about what will happen in the future."
answer10 = "to examine something carefully."

while True:
    prompt = input("Prompt:")
    if prompt.lower().replace(" ","") in question1.lower().replace(" ",""):
        print(answer1)
    elif prompt.lower().replace(" ","") in question2.lower().replace(" ",""):
        print(answer2)
    elif prompt.lower().replace(" ","") in question3.lower().replace(" ",""):
        print(answer3)
    elif prompt.lower().replace(" ","") in question4.lower().replace(" ",""):
        print(answer4)
    elif prompt.lower().replace(" ","") in question5.lower().replace(" ",""):
        print(answer5)
    elif prompt.lower().replace(" ","") in question6.lower().replace(" ",""):
        print(answer6)
    elif prompt.lower().replace(" ","") in question7.lower().replace(" ",""):
        print(answer7)
    elif prompt.lower().replace(" ","") in question8.lower().replace(" ",""):
        print(answer8)
    elif prompt.lower().replace(" ","") in question9.lower().replace(" ",""):
        print(answer9)
    elif prompt.lower().replace(" ","") in question10.lower().replace(" ",""):
        print(answer10)
    else:
        print("Sorry I couldn't Answer")
