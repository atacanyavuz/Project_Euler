"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from Helper.Timer import Timer
from Helper.Logger import Logger
from Solutions.Helper import Euler_Helper as EH

QUESTION_NUM = 7


def solve():
    timer = Timer()
    timer.set_start_time()
    counter = 1
    number = 3
    while True:
        if EH.is_prime(number):
            counter += 1
        if counter == 10001:
            break
        number += 2
    return number, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
