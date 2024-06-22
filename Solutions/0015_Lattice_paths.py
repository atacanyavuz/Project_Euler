"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 15


def solve():
    timer = Timer()
    timer.set_start_time()
    result = int(factorial(40) / (factorial(20) * factorial(20)))
    return result, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
