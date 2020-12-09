from random import choice

questions = ["Why bread tastes like bread?","Who am i?","Is cheese made out of letuce?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()


print("Okay")
