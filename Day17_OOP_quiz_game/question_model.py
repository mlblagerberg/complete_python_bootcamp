from data import question_data


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def get_question(self):
        random_number = randint(0, len(question_data))
        self.text = question_data[random_number]["text"]
        self.answer = question_data[random_number]["answer"]
        return self.text, self.answer