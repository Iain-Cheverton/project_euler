"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
import prime_tools


def main():
    """adds up all the amicable numbers under 10000"""
    return sum(number for number in range(1, 10000) if amicable_pair(number))


def amicable_pair(number):
    """if the number has an amicable pair return it else return 0"""
    paired_number = sum(prime_tools.get_factors(number)[:-1])
    if sum(prime_tools.get_factors(paired_number)[:-1]) == number and number != paired_number:
        return paired_number
    return 0


if __name__ == "__main__":
    print(main())
