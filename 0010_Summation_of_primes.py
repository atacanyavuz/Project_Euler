"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def prime(x):
    for i in range(2,int(x**(1/2))+1):
        if not x % i:
            return False

    return True

total = 0
for i in range(3,2000000,2):
    if (prime(i)):
        total += i

total += 2

print(total)


