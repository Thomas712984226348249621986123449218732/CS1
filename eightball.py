'''
Author: Thomas Butkiewicz
Date: 12/7/23
Description: This is a magic 8 ball that if you ask it a question it will give you an answer.
Bugs: None
Challenges: str.lower.
Sources: Me, Ms Marciano, Mr Abanto.
'''





import random

while True:
    question = str.lower(input("Enter stop to end. Ask a question, any question, and I will give you a truthful answer. "))

    if question == "stop":
        break
    elif "?" in question:
        print(random.choice(['Gaurenteed', 'Yes', 'No', 'Maybe', 'Try again later', ' A little bit', 'Never']))
    else:
        print("Not a question!")






