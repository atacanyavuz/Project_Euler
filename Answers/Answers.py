import json
import os.path


class Answers:
    def __init__(self, path):
        with open(path) as answersFile:
            answers_data = answersFile.read()

        self.answers = json.loads(answers_data)

    def get_answer(self, question_number):
        return self.answers[str(question_number)]

