from random import choice
""" make a list of questios """

questions = [
    "Why is the car red",
    "Why the rain falls",
    "Why your hair is black",
    "Why the food is hot",
    "Why the dog is barking"
    ]


""" pick a random choice from the list to ask the question """
question = choice(questions)
answer = input(question.lower())

while answer != "just because":
    question = choice(questions)
    answer = input(question.strip().lower())

print("Oh ... OK")
