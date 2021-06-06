"""Contains various tools involving prime numbers that are reused throughout"""
import math


def find_primes(bound):
    """This creates a list of all primes up to a bound"""
    primes = [2]
    temp_primes = [2]
    for i in range(2, bound + 1):
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
    """This creates a list of all the prime factors of an integer"""
    factors = []
    divisor = 1
    while integer > 1:
        divisor += 1
        while integer % divisor == 0:
            factors.append(divisor)
            integer /= divisor
    return factors


def dict_factors(integer):
    """returns a dictionary containing the prime factors of an integer and the maximum number of times they divide it"""
    factors = dict()
    for i in range(2, integer + 1):
        while integer % i == 0:
            integer //= i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            if integer == 1:
                return factors
    return factors


def lcm(factor_list):
    """This function takes a list of factors in ascending order"""
    total_factors = {}
    for factor in factor_list:
        factor_dict = dict_factors(factor)
        for prime, power in factor_dict.items():
            total_factors[prime] = max(
                total_factors[prime] if prime in total_factors else 0, power
            )
    product = 1
    for prime, power in total_factors.items():
        product *= prime ** power
    return product


def get_factors(integer):
    """This returns a list of all the factors of an integer"""
    factor_list = []
    for divisor in range(1, integer // 2 + 1):
        if integer % divisor == 0:
            factor_list.append(divisor)
    factor_list.append(integer)
    return factor_list


def next_prime(integer: int) -> int:
    """returns the smallest prime greater than an integer"""
    if integer < 2:
        return 2
    potential_prime = integer
    primes = find_primes(integer)
    while True:
        potential_prime += 1
        for divisor in primes:
            if potential_prime % divisor == 0:
                break
        else:
            return potential_prime
