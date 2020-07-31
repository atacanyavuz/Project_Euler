"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def prime(x):
    for i in range(2,int(x**(1/2))+1):
        if not x % i:
            return False

    return True

number = 1
for i in range(1,20):
    if prime(i):
        for j in range(1,5):
            if i**(j+1) > 20:
                break
        number *= i**j

print(number)
