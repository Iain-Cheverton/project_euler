"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import itertools

import prime_tools

IS_PRIME = prime_tools.is_prime_array(10_000_000)


def main() -> int:
    """Returns the largest n-digit pandigital prime"""
    current_largest = 0
    # since the digits 12345678 add up to 36 and 123456789 adds to 45 all 8 and 9 digit pandigitals are divisible by 3
    for pandigital in itertools.permutations("1234567"):
        pan_int = int("".join(pandigital))
        if IS_PRIME[pan_int]:
            current_largest = pan_int
    return current_largest


if __name__ == "__main__":
    print(main())
