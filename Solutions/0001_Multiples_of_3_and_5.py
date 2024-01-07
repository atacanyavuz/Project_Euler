"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 1


def solve():
    timer = Timer()
    timer.set_start_time()
    total = 0
    for i in range(1, 1000):
        if not (i % 3 and i % 5):
            total += i
    return total, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
