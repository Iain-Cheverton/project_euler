"""
The description of this problem contains too many mathematical formulae to write in plain text but can be found at:
https://projecteuler.net/problem=27
"""
import time

import prime_tools

IS_PRIME = prime_tools.is_prime_array(20_000)


def consecutive_primes(linear, constant):
    """returns the number of consecutive primes formed by the sequence:
    n ** 2 + linear * n + constant starting from n = 0"""
    prime_count = 0
    while IS_PRIME[prime_count * prime_count + linear * prime_count + constant]:
        prime_count += 1
    return prime_count


def main():
    """returns the number of consecutive primes and the parameters that
    create it for the longest sequence within the range provided"""
    max_consecutive = (0, 0, 0)
    for linear_coefficient in range(-999, 1000):
        for constant_term in prime_tools.find_primes(1001):
            series_length = consecutive_primes(linear_coefficient, constant_term)
            if series_length > max_consecutive[0]:
                max_consecutive = (series_length, linear_coefficient, constant_term)
    return max_consecutive[1] * max_consecutive[2]


if __name__ == "__main__":
    start = time.perf_counter()
    print(main(), time.perf_counter() - start)
