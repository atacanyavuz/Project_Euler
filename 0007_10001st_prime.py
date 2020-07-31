"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def prime(x):
    for i in range(2,int(x**(1/2))+1):
        if not x % i:
            return False

    return True


counter = 1
number = 3
while True:
    if prime(number):
        counter += 1
    if counter == 10001:
        break
    number += 2

print(number)
