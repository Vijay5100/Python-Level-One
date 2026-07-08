from tabulate import tabulate 
import os 
import time 

questions = [] 
questions.append({
    "id": 1,
    "question": "What is the capital of France?",
    "answer": "paris",
    "points": 100
})

questions.append({
    "id": 2,
    "question": "How many days are in a week?",
    "answer": "7",
    "points": 100
})

questions.append({
    "id": 3,
    "question": "What is the largest ocean on Earth?",
    "answer": "pacific ocean",
    "points": 200
})

questions.append({
    "id": 4,
    "question": "Which planet the fourth away from the sun?",
    "answer": "mars",
    "points": 200
})

questions.append({
    "id": 5,
    "question": "Who painted the Mona Lisa?",
    "answer": "leonardo da vinci",
    "points": 300
})

questions.append({
    "id": 6,
    "question": "What is the element symbol for gold?",
    "answer": "AU",
    "points": 300
})

questions.append({
    "id": 7,
    "question": "What is the squate root of 144?",
    "answer": "12",
    "points": 400
})

questions.append({
    "id": 8,
    "question": "Which country has the most people in the world?",
    "answer": "India",
    "points": 400
})

questions.append({
    "id": 9,
    "question": "What is the longest river in the world?",
    "answer": "nile",
    "points": 500
})

questions.append({
    "id": 10,
    "question": "Who was the first person to discover america?",
    "answer": "Christopher Columbus",
    "points": 500
})

questions.append({
    "id": 11,
    "question": "What is the largest mammal in the world?",
    "answer": "blue whale",
    "points": 100
})

questions.append({
    "id": 12,
    "question": "How many continents are there?",
    "answer": "7",
    "points": 200
})

questions.append({
    "id": 13,
    "question": "What is the hardest natural substance on Earth?",
    "answer": "diamond",
    "points": 300
})
questions.append({"id": 14, "question": "This U.S. president is on the one dollar bill.", "answer": "George Washington", "points": 300})

questions.append({"id": 15, "question": "This gas is what plants take in during photosynthesis.", "answer": "Carbon dioxide", "points": 300})

questions.append({"id": 16, "question": "This 1648 treaty ended the Thirty Years War and helped establish state sovereignty in Europe.", "answer": "Treaty of Westphalia", "points": 400})

questions.append({"id": 17, "question": "In Frankenstein, this is the name of Victor Frankenstein's closest friend, who is later killed by the creature.", "answer": "Henry Clerval", "points": 400})

questions.append({"id": 18, "question": "This law states that gas pressure is inversely proportional to volume when temperature is constant.", "answer": "Boyle's Law", "points": 400})

questions.append({"id": 19, "question": "This landlocked South American country has two capitals which are Sucre and La Paz.", "answer": "Bolivia", "points": 400})

questions.append({"id": 20, "question": "This ancient Greek philosopher wrote nicomachean ethics and argued that virtue lies between extremes.", "answer": "Aristotle", "points": 400})

questions.append({"id": 21, "question": "This theorem says every nonconstant polynomial with complex coefficients has at least one complex root.", "answer": "Fundamental Theorem of Algebra", "points": 500})

questions.append({"id": 22, "question": "This 1794 rebellion against a federal tax was put down by George Washington's administration.", "answer": "Whiskey Rebellion", "points": 500})

questions.append({"id": 23, "question": "This boundary around a black hole marks the point beyond which not even light can escape.", "answer": "Event horizon", "points": 500})

questions.append({"id": 24, "question": "This Spanish painter created The Third of May 1808 which is a painting showing the horrors of war.", "answer": "Francisco Goya", "points": 500})

questions.append({"id": 25, "question": "This Greek Titan was punished by being forced to hold up the sky for eternity.", "answer": "Atlas", "points": 500})

questions.append({
    "id": 26,
    "question": "This is the smallest prime number.",
    "answer": "2",
    "points": 100
})

questions.append({
    "id": 27,
    "question": "This author wrote Romeo and Juliet.",
    "answer": "William Shakespeare",
    "points": 300
})

questions.append({
    "id": 28,
    "question": "This is the process where water changes from liquid to gas.",
    "answer": "evaporation",
    "points": 200
})

options = """Options: 
1. Choose a Question 
2. Answering Question
3. Game End 
4. View Current Scores
"""
# difficulty level -> display the question id's -> pick one id 
scores = [0,0,0,0,0]
difficulty_rows = [
    [1,"Type-1",100],    
    [2,"Type-2",200],    
    [3,"Type-3",300],    
    [4,"Type-4",400],    
    [5,"Type-5",500],    
]
difficulty_headers = ["Sr No.", "Difficulty Type","Points"]
number_of_teams = int(input("How many teams are playing? "))
while True: 
    print("Jeopardy:")
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1:
           print(tabulate(difficulty_rows,headers=difficulty_headers,tablefmt="grid"))
           choice = int(input("Enter your choice: "))
           category = difficulty_rows[choice-1][2]
           time.sleep(1)
           os.system("clear")
           rows = []
           for i in range(len(questions)):
               if questions[i]["points"] == category:
                   rows.append([questions[i]["id"],"Hidden",category])
           headers = ["Qns No.","Question","Points"]
           print(tabulate(rows,headers=headers,tablefmt="grid"))
           choice = input("Do you want to continue (y/n) ? ")
           if choice == "y":
               continue 
           
        case 2: 
            question_id = int(input("Question ID: "))
            team_no = int(input("Team Number: "))
            question = questions[question_id-1]
            print(f"Question: {question['question']}")
            answer = input("Answer: ")
            
            if answer.lower() == question["answer"].lower():
                print("Correct")
                scores[team_no - 1] += question["points"]
            else: 
                scores[team_no - 1] += -1 
                print("Wrong.")
        case 3:
            rows = [] 
            for i in range(len(scores)):
                rows.append([i+1,scores[i]])
            headers = ["Team No.","Score"]
            print(tabulate(rows,headers=headers,tablefmt="grid"))
            break
        case 4:
            rows = []
            for i in range(len(scores)):
                rows.append([i + 1, scores[i]])
            headers = ["Team No.", "Score"]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        case _: 
            print("Invalid choice, Try again.")
    time.sleep(1)
    os.system("clear")
