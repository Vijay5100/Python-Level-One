import random 
import os 
import time 

stories = [
    """
One morning, he found a mysterious -(1)- outside the house.
He decided to take it to the -(2)-.
On the way, a -(3)- suddenly appeared.
He used a -(4)- to escape.
At the end of the journey, he discovered a hidden -(5)-.
""", 
    """
One afternoon, She discovered a strange -(1)- beside the road.
Curious, she carried it toward the -(2)-.
Before long, a -(3)- blocked her path.
She used a -(4)- to get past it.
Beyond the obstacle, She found a mysterious -(5)-.
""",
    """
During a storm, He uncovered an old -(1)- beneath a mug.
A hidden clue pointed toward the -(2)-.
On the way, a -(3)- began to follow him.
He escaped using a -(4)-.
At sunrise, the trail ended at a secret -(5)-.
""",
    """
Late one evening, she received a mysterious -(1)-.
The message led her to the -(2)-.
At the entrance, a -(3)- stood guard.
She overcame the danger with a -(4)-.
Inside, she discovered an ancient -(5)-.
""", 
    """
At dawn, I spotted a glowing -(1)- near the garden.
I followed its markings toward the -(2)-.
Along the path, a -(3)- jumped out from the shadows.
I defended myself with a -(4)-.
Finally, I uncovered a legendary -(5)-.
"""
]
options = [
    ["key", "map", "box", "letter"],          
    ["forest", "castle", "school", "cave"],   
    ["dragon", "robot", "tiger", "ghost"],    
    ["sword", "bicycle", "rope", "spell"],    
    ["treasure", "portal", "city", "spaceship"]  
]

story = random.choice(stories)
count = 0 
while count < 5:
    print(story)
    print("options:")
    for i in range(4):
        print(f"{i+1}. {options[count][i]}")
    
    index = int(input("Enter your choice (1-4): "))
    if index > 4:
        index = 1 

    story = story.replace(f"-({count+1})-",options[count][index-1])
    count += 1 
    time.sleep(1)
    os.system("clear")

print("Story: ")
print(story)
