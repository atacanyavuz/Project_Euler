import os
import importlib.util
from Answers.Answers import Answers
from Helper.Logger import Logger

solve_functions = dict()
answers = Answers("../Answers/answers.json")


def test_answers():
    number_of_true_answers = 0
    for question_num in sorted(solve_functions.keys()):
        result, time = solve_functions[question_num]()
        answer = answers.get_answer(question_num)
        if answer == result:
            print("[+]", end="\t")
            number_of_true_answers += 1
        else:
            print("[-]", end="\t")
        Logger.print_log(question_num, result, time)
    print("{} out of {} questions are correct.". format(number_of_true_answers, len(solve_functions)))


def find_solve_function(file_path):
    try:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, 'solve') and callable(module.solve) and hasattr(module, "QUESTION_NUM"):
            solve_functions[module.QUESTION_NUM] = module.solve
        else:
            print(f"{file_path}: 'solve' function and QUESTION_NUM not found.")
    except Exception as e:
        print(f"{file_path}: Error - {str(e)}")


def find_solve_functions_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                find_solve_function(file_path)


if __name__ == "__main__":
    find_solve_functions_in_folder("../Solutions")
    test_answers()
