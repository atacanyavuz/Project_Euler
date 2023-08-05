"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from math import factorial


def find_permutation(k):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []

    for i in range(10, 0, -1):
        index = (k - 1) // factorial(i - 1)
        digit = digits[index]
        result.append(digit)
        digits.remove(digit)
        k = k - index * factorial(i - 1)
    return result


result = find_permutation(1000000)
result_number = int(''.join(str(digit) for digit in result))
print(result_number)
