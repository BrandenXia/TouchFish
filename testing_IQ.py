from tqdm import trange
from time import sleep
from random import randint, uniform


def question_and_react(question):
    input(question + "\n> ")
    print("Processing your answer, please wait a few seconds...")
    for i in trange(randint(80, 100)):
        sleep(uniform(0.01, 0.2))


print(
    """
\t************************
\t**  Calculate you IQ  **
\t************************
"""
)
question_and_react("How old are you?")
question_and_react("How tall are you?")
question_and_react("How heavy are you?")
question_and_react("Which food do you prefer, hamburger or noodles?")
question_and_react("How much money do you use per day?")
print("Finished!\nCongratulations! You IQ is " + str(randint(80, 200)) + "!\nTHe program will quit in 5 seconds...")
sleep(5)
