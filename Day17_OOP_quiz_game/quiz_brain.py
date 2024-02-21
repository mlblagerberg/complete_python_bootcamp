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

    def get_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        return text, answer

    def quiz_time(self):
        # check start
        if self.question_number == 0:
            start = input("Would you like to play quiz game? 'Y' or 'N' ")
        else:
            start = input(f"Would you like another question? 'Y' or 'N' ")
        if start == 'Y':
            question = self.get_question()
            question_text = question[0]
            question_answer = question[1]
            user_answer = input(f"Q{self.question_number}: {question_text} (True/False)? ")
            self.next_question()
            if user_answer == question_answer:
                self.score += 1
                # print(question_answer)
                print(f"You're right! Your score is {self.score}.")
                self.quiz_time()
            else:
                # print(question_answer)
                print(f"You were wrong. Your score is {self.score}.")
                self.quiz_time()
        else:
            print("Goodbye!")




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