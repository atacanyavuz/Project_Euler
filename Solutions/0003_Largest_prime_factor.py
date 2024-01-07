"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 3


def solve():
    timer = Timer()
    timer.set_start_time()
    number = 600851475143
    prime_factor = 3
    while True:
        if not number % prime_factor:
            number = number / prime_factor
            continue
        if prime_factor > number:
            break
        prime_factor += 2

    return prime_factor, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
