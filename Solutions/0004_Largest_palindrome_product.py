"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from Helper.Timer import Timer
from Helper.Logger import Logger
from Solutions.Helper import Euler_Helper as EH

QUESTION_NUM = 4


def solve():
    timer = Timer()
    timer.set_start_time()
    max_value = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            if EH.is_palindrome(a * b) and max_value < a * b:
                max_value = a * b
    return max_value, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
