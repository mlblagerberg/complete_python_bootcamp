import question_data
from random import randint


class Question:

    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.correct_answer = q_answer

    # def get_question(self):
    #     random_number = randint(0, len(question_computers))
    #     self.question = question_computers[random_number]["question"]
    #     self.correct_answer = question_computers[random_number]["correct_answer"]
    #     return self.question, self.correct_answer
