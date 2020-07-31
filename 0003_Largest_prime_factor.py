"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
prime_factor = 3
while True:
    if not number % prime_factor:
        number = number / prime_factor
        continue
    if prime_factor > number:
        break
    prime_factor += 2

print(prime_factor)

