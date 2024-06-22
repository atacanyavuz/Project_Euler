"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 16


def solve():
    timer = Timer()
    timer.set_start_time()
    x = 2 ** 1000
    total = 0

    while x != 0:
        total = total + (x % 10)
        x = x // 10

    return total, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
