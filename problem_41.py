"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import itertools
from typing import List

import prime_tools

IS_PRIME = prime_tools.is_prime_array(10_000_000)


def pandigitals(start: int, end: int) -> List:
    """Returns a list of all the n digit pandigitals"""
    pandigital_list = []
    for pandigital in itertools.permutations("".join(str(x) for x in range(start, end))):
        pandigital_list.append(int("".join(pandigital)))
    return pandigital_list


def main() -> int:
    """Returns the largest n-digit pandigital prime"""
    current_largest = 0
    # since the digits 12345678 add up to 36 and 123456789 adds to 45 all 8 and 9 digit pandigitals are divisible by 3
    for pandigital in pandigitals(1, 8):
        if IS_PRIME[pandigital]:
            current_largest = pandigital
    return current_largest


if __name__ == "__main__":
    print(main())
