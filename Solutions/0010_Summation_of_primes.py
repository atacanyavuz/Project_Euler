"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
from Helper.Timer import Timer
from Helper.Logger import Logger
from Solutions.Helper import Euler_Helper as EH

QUESTION_NUM = 10


def prime(x):
    for i in range(2, int(x ** (1 / 2)) + 1):
        if not x % i:
            return False
    return True


def solve():
    timer = Timer()
    timer.set_start_time()
    total = 0
    for i in range(3, 2000000, 2):
        if EH.is_prime(i):
            total += i
    total += 2
    return total, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
