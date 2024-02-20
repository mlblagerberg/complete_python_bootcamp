from data import question_data
from question_model import Question


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