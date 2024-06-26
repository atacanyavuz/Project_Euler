"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from math import factorial

from Helper.Logger import Logger
from Helper.Timer import Timer

QUESTION_NUM = 20


def solve():
    timer = Timer()
    timer.set_start_time()
    x = factorial(100)
    total = 0

    while x != 0:
        total = total + x % 10
        x = x // 10
    return total, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
