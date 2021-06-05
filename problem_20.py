"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
import functools


@functools.cache
def factorial(integer):
    """returns the factorial of an integer"""
    return integer * factorial(integer - 1) if integer else 1


def main():
    """returns th sum of the digits of 100 factorial"""
    number = str(factorial(100))
    return sum(int(digit) for digit in number)


print(main())
