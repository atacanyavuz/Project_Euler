"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from Helper.Timer import Timer
from Helper.Logger import Logger
from Solutions.Helper import Euler_Helper as EH

QUESTION_NUM = 5


def solve():
    timer = Timer()
    timer.set_start_time()
    number = 1
    for i in range(1, 20):
        if EH.is_prime(i):
            for j in range(1, 5):
                if i ** (j + 1) > 20:
                    break
            number *= i ** j
    return number, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
