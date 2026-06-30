import random

story_1 = """
One morning, He found a mysterious -(1)- outside his large house.
The -(1)- started glowing with a bright -(2)- light.
He picked it up and suddenly appeared in -(3)-.
In -(3)-, he -(4)- to the creature.
"""

story_2 = """
She decided to visit the -(1)- during the weekend.
While walking around, she saw a large -(2)-.
It was eating a -(3)- beside an oak tree.
She took a picture of the -(3)- and went back to her -(4)-.
"""

story_3 = """
One day, He built a small robot named -(1)-.
The robot could -(2)- faster than most humans.
He asked the robot to bring a -(3)- from the kitchen.
Instead, -(1)- brought the entire -(4)-.
"""

stories = [story_1, story_2, story_3]

selected_story = random.choice(stories)

print("Mad Libs")

count = 1

while True:
    print(selected_story)
    fill = input(f'Fill the Blank-{count}:')
    if fill.strip() == "":
        print("Please enter a word since blank answers are not allowed")
        continue
    selected_story = selected_story.replace(f"-({count})-", fill.strip())
    count += 1
    if count == 5:
        break
    
print("Your Finished Story:")
print(selected_story)
