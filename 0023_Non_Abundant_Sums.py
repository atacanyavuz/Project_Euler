"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def sum_of_proper_divisors(x):
    total = 0
    for i in range(1, int(x / 2 + 1)):
        if x % i == 0:
            total = total + i
    return total


abundantNumbers = list()
NonAbundantSumsList = [0] * 28124
nonAbundantSum = 0

for i in range(12, 28124):
    if sum_of_proper_divisors(i) > i:
        abundantNumbers.append(i)

for i in range(len(abundantNumbers)):
    for j in range(len(abundantNumbers)):
        if abundantNumbers[i] + abundantNumbers[j] < 28124:
            NonAbundantSumsList[abundantNumbers[i] + abundantNumbers[j]] = 1

for i in range(len(NonAbundantSumsList)):
    if NonAbundantSumsList[i] == 0:
        nonAbundantSum += i

print(nonAbundantSum)
