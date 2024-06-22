def is_palindrome(x):
    return str(x) == "".join(reversed(str(x)))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def divisor_num(x):
    i = 2
    number_of_divisor = 1
    powers_of_prime_factors = [0]
    while x != 1:
        if not (x % i):
            x = x // i
            powers_of_prime_factors[-1] += 1
            continue
        if i == 2:
            i += 1
        else:
            i += 2
        if powers_of_prime_factors[-1] != 0:
            powers_of_prime_factors.append(0)

    for i in powers_of_prime_factors:
        number_of_divisor = number_of_divisor * (i + 1)
    return number_of_divisor


def triangle(x):
    return x * (x + 1) / 2
