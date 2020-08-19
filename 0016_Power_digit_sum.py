"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

x = 2 ** 1000
total = 0

while x != 0:
    total = total + (x%10)
    x = x // 10

print(total)


