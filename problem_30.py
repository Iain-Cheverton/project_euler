"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
# 9 ** 5 * 6 = 354294 < 999999 so this is a suitable limit


def sum_of_powers(power):
    """all the numbers where if their digits are raised to the power given sum to make that number"""
    valid_sums = []
    for integer in range(10, 9 ** power * (power + 1)):  # the upper bound  was derived analytically and is overly large
        if sum([int(digit) ** power for digit in str(integer)]) == integer:
            valid_sums.append(integer)
    return valid_sums


if __name__ == "__main__":
    print(sum_of_powers(5))
