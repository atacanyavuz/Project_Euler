class Logger:
    @staticmethod
    def print_log(question_num, answer, calculation_time=-1):
        if calculation_time == -1:
            print("Question {} answer: {}".format(question_num, answer))
            return
        print("Question {} was calculated in {} seconds. Answer: {}".format(question_num, calculation_time, answer))