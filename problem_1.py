"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def main(upper_bound):
    """returns the sum of the numbers that divide by 3 or 5 below 1000"""
    return sum(i for i in range(upper_bound) if not (i % 3 and i % 5))


if __name__ == "__main__":
    print(main(1000))
