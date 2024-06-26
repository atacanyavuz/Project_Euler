"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
from Helper.Timer import Timer
from Helper.Logger import Logger

QUESTION_NUM = 14

even = lambda x: x / 2
odd = lambda x: (3 * x) + 1


def chain_num(x):
    chain = 0
    while x != 1:
        if x % 2 == 0:
            x = even(x)
            chain += 1
        else:
            x = odd(x)
            chain += 1
    return chain


def solve():
    timer = Timer()
    timer.set_start_time()

    max_chain = 0
    number = 0

    for i in range(1, 1000001):
        if max_chain < chain_num(i):
            max_chain = chain_num(i)
            number = i

    return number, timer.get_reset_calculation_time()


if __name__ == "__main__":
    result, time = solve()
    Logger.print_log(QUESTION_NUM, result, time)
