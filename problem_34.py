"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math


def main():
    """returns all the curious numbers"""
    curious_numbers = []
    # 9! * 7 is a suitable limit since 9999999 > 9! * 7
    for integer in range(3, math.factorial(9) * 7):
        if sum_of_factorials(integer) == integer:
            curious_numbers.append(integer)
    return curious_numbers


def sum_of_factorials(integer: int) -> int:
    """returns the sum of the factorials of each of the digits of an integer"""
    return sum([math.factorial(int(digit)) for digit in str(integer)])


if __name__ == "__main__":
    print(sum(main()))
