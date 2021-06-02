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
    primes = find_primes(integer + 1)
    factors = []
    for prime in primes:
        while integer % prime == 0:
            factors.append(prime)
            integer /= prime
        if integer == 1:
            return factors


def dict_factors(integer):
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
        for prime in factor_dict:
            if prime in total_factors:
                total_factors[prime] = max(total_factors[prime], factor_dict[prime])
            else:
                total_factors[prime] = factor_dict[prime]
    product = 1
    for prime in total_factors:
        product *= prime ** total_factors[prime]
    return product


def get_factors(integer):
    """This returns a list of all the factors of an integer"""
    factor_list = []
    for divisor in range(1, integer + 1):
        if integer % divisor == 0:
            factor_list.append(divisor)
    return factor_list
