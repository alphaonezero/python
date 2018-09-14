from random import choice
questions = [
    "Why isn't Hillary Clinton in jail?: ",
    "Why is the sky blue?: ",
    "Where do babies come from?: "
    ]
answer = input(choice(questions)).lower().strip()

while answer != "just because":
    answer = input("Why?: ")

print("Oh... Ok.")
