"""Contains various tools involving prime numbers that are reused throughout"""
import math


def is_prime_array(bound):
    """creates a list of True/False values where true corresponds to prime numbers"""
    is_prime = [True] * (bound + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(math.ceil(math.sqrt(bound))):
        if is_prime[i]:
            for multiple in range(i * 2, bound + 1, i):
                is_prime[multiple] = False
    return is_prime


def find_primes(bound):
    """This creates a list of all primes up to a bound"""
    is_prime_list = is_prime_array(bound)
    return [integer for integer in range(bound + 1) if is_prime_list[integer]]


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
            total_factors[prime] = max(total_factors[prime] if prime in total_factors else 0, power)
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
