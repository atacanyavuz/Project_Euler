def is_palindrome(x):
    return str(x) == "".join(reversed(str(x)))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
