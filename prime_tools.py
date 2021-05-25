import math


def find_primes(bound):
    primes = [2]
    temp_primes = [2]
    for i in range(2, bound):
        root = math.sqrt(i)
        for prime in primes:
            if i % prime == 0:
                break
            if prime > root:
                temp_primes.append(i)
                break
        primes = temp_primes

    return primes


def prime_factors(integer):
    primes = find_primes(int(math.sqrt(integer)))
    factors = []
    for prime in primes:
        while integer % prime == 0:
            factors.append(prime)
            integer /= prime
        if integer == 1:
            return factors
