import math
import sympy


def primes(n):
    """ Returns a list of all prime numbers less than n """
    return list(sympy.sieve.primerange(2, n))


def is_prime(m):
    """Returns a boolean indicating whether m is a prime number"""
    if m <= 1:
        return False
    if m == 2:
        return m
    if m > 2 and m % 2 == 0:
        return False
    divisor = math.floor(math.sqrt(m))
    for num in range(3, 1 + divisor, 2):
        if m % num == 0:
            return False
    return m
