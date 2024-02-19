"""Project: Quiz Game
Start: February 18th, 2024
Last touched: February 18th, 2024
Author: Madeleine L.
"""

from data import question_data
from random import randint

# If we have a question object what objects would it have?
# - Would have text and answer
# - Methods would be to take a guess and check it against an answer


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def get_question(self):
        random_number = randint(0, len(question_data))
        self.text = question_data[random_number]["text"]
        self.answer = question_data[random_number]["answer"]
        return self.text, self.answer

class Quiz:

    def __init__(self):
        self.question = question_data

    def start_quiz(self):
        start = input("Would you like to play quiz game? 'Y' or 'N' ")
        if start == 'Y':
            question_bank = Question("text", "answer")
            quiz_question = question_bank.get_question()
            user_answer = input(quiz_question[0])
            question_answer = quiz_question[1]
            return print(user_answer), print(question_answer)


        else:
            print("Goodbye!")


int_quiz = Quiz()
int_quiz.start_quiz()


# print(question_data[1]["text"])

# my_q = Question("2+3=5", True)
# print(my_q.text)
