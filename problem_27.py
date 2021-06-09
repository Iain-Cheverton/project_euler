"""https://projecteuler.net/problem=27"""
import prime_tools


def consecutive_primes(linear, constant):
    """returns the number of consecutive primes formed by the sequence:
    n ** 2 + linear * n + constant starting from n = 0"""
    primes = 0
    while len(prime_tools.get_factors(primes ** 2 + linear * primes + constant)) == 2:
        primes += 1
    return primes


def main():
    """returns the number of consecutive primes and the parameters that
    create it for the longest sequence within the range provided"""
    max_consecutive = (0, 0, 0)
    for linear_coefficient in range(-999, 1000):
        for constant_term in range(-1000, 1001):
            series_length = consecutive_primes(linear_coefficient, constant_term)
            if series_length > max_consecutive[0]:
                max_consecutive = (series_length, linear_coefficient, constant_term)
    return max_consecutive[1] * max_consecutive[2]


if __name__ == "__main__":
    print(main())
