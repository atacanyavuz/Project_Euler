"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 9


def solve():
    timer = Timer()
    timer.set_start_time()
    for i in range(1, 334):
        for j in range(1, 667 - i):
            if ((i ** 2 + j ** 2) ** (1 / 2) == int((i ** 2 + j ** 2) ** (1 / 2))):
                c = int((i ** 2 + j ** 2) ** (1 / 2))
                if (i + j + c == 1000):
                    return int(i * j * c), timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
