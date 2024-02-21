"""Project: Quiz Game
Start: February 18th, 2024
Last touched: February 20th, 2024
Author: Madeleine L.
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# If we have a question object what objects would it have?
# - Would have text and answer
# - Methods would be to take a guess and check it against an answer

# int_quiz = QuizBrain()
# int_quiz.start_quiz()

# create question bank as lecture asks

question_bank = []
for i in range(0, len(question_data)):
    text = question_data[i]["text"]
    answer = question_data[i]["answer"]
    question = Question(text, answer)
    question_bank.append(question)

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)

# quiz.get_question()
quiz.quiz_time()

# my_q = Question("2+3=5", True)
# print(my_q.text)
