"""Project: Tkinter Trivia App
Start: May 21st, 2024
Last touched: May 22nd, 2024
Author: Madeleine L.
"""

# Resources:
# https://opentdb.com/
# https://www.w3schools.com/html/html_entities.asp

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")