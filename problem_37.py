"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time

import prime_tools

IS_PRIME = prime_tools.is_prime_array(1_000_000)


def main():
    """returns all the truncatable primes larger than 10"""
    truncated_primes = []
    # the first 4 primes are removed since the question explicitly excludes them
    for integer in range(10, 1_000_000):
        if IS_PRIME[integer] and lt_prime(integer) and rt_prime(integer):
            truncated_primes.append(integer)
    return truncated_primes


def lt_prime(prime):
    """True if the prime is left truncatable"""
    string = str(prime)
    while string[1:]:
        string = string[1:]
        if string[0]:
            if not IS_PRIME[int(string)]:
                return False
    return True


def rt_prime(prime):
    """True if the prime is right truncatable"""
    string = str(prime)
    while string[:-1]:
        string = string[:-1]
        if string[0]:
            if not IS_PRIME[int(string)]:
                return False
    return True


if __name__ == "__main__":
    start = time.perf_counter()
    print(sum(main()), time.perf_counter() - start)
# Runtime before optimisation = 72.9893086, after switching to is_prime_array = 0.0922085
# I rewrote it using recursion and memoize but this ran slower: 0.11913520000000002 so I reverted this
