"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def lowest_common_multiple(bound):
    for multiple in range(1, 10 ** 10):
        for divisor in range(1, bound + 1):
            if multiple % divisor != 0:
                break
        else:
            return multiple


print(lowest_common_multiple(20))

# This takes too long, faster to solve manually with a calculator
