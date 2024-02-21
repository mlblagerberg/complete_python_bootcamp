# from data import question_data
# from question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        self.question_number += 1
        return self.question_number
        # self.question_number += 1
        # if self.question_number > len(self.question_list):
        #     return False, self.question_number
        # else:
        #     return True, self.question_number

    def get_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        user_answer = input(f"Q{self.question_number + 1}: {text} (True/False)? ")
        return user_answer.lower(), answer.lower()

    def quiz_prompt(self):
        if self.question_number == 0:
            play = input("Would you like to play quiz game? 'Y' or 'N' ")
        elif self.question_number >= len(self.question_list):
            play = "N"
        else:
            play = input(f"Would you like another question? 'Y' or 'N' ")
        return play.upper()

    def check_answer(self, answers):
        if answers[0] == answers[1]:
            self.score += 1
            print(f"You're right! \nThe correct answer was {answers[1]}.\nYour score is "
                  f"{self.score}/{self.question_number}.")
        else:
            print(f"You were wrong. \nThe correct answer was {answers[1]}.\nYour score is "
                  f"{self.score}/{self.question_number}.")

    def quiz_time(self):
        # check start
        play = self.quiz_prompt()
        if play == 'Y' and self.question_number < len(self.question_list):
            answers = self.get_question()
            # Increase question value
            self.next_question()
            self.check_answer(answers)
            self.quiz_time()
        else:
            print(f"Your final score is {self.score}/{self.question_number}. Thanks for playing! \nGoodbye!")




#######################################################
# Below is from working on it before the lesson prompts.
    # def __init__(self):
    #     self.question = question_data

    # def start_quiz(self):
    #     start = input("Would you like to play quiz game? 'Y' or 'N' ")
    #     if start == 'Y':
    #         question_bank = Question("text", "answer")
    #         quiz_question = question_bank.get_question()
    #         user_answer = input(quiz_question[0])
    #         question_answer = quiz_question[1]
    #         return print(user_answer), print(question_answer)
    #     else:
    #         print("Goodbye!")