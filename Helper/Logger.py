class Logger:
    @staticmethod
    def print_log(question_num, answer, calculation_time=-1):
        if calculation_time == -1:
            print("Question {} answer: {}".format(question_num, answer, 5))
            return
        print("Question {} was calculated in {} seconds.\tAnswer: {}".format(question_num, round(calculation_time, 5),
                                                                             answer))
