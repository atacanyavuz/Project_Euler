"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 6


def solve():
    timer = Timer()
    timer.set_start_time()

    total_sum_of_square = 0
    total_square_of_sum = 0

    for i in range(1, 101):
        total_sum_of_square += i ** 2
        total_square_of_sum += i

    total_square_of_sum = total_square_of_sum ** 2
    answer = total_square_of_sum - total_sum_of_square
    return answer, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
