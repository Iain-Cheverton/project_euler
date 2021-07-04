"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import math
import typing


def main() -> typing.Tuple[int, int]:
    """returns the product of the numerators and denominators of the four desired fractions"""
    total_numerator = 1
    total_denominator = 1
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            if check_division(numerator, denominator):
                total_numerator *= numerator
                total_denominator *= denominator
    return total_numerator, total_denominator


def check_division(numerator: int, denominator: int) -> bool:
    """returns a new numerator and denominator for a fraction,
    if it can be simplified by 'cancelling' a digit from each"""
    for digit in str(denominator):
        if digit in str(numerator) and str(denominator).replace(digit, "") and str(numerator).replace(digit, ""):
            new_denominator = int(str(denominator).replace(digit, ""))
            new_numerator = int(str(numerator).replace(digit, ""))
            if new_numerator and new_denominator:
                if numerator / denominator == new_numerator / new_denominator and int(str(denominator)[-1]):
                    return True
    return False


if __name__ == "__main__":
    unsimplified_fraction = main()
    hcf = math.gcd(unsimplified_fraction[0], unsimplified_fraction[1])
    print(f"{unsimplified_fraction[0] // hcf} / {unsimplified_fraction[1] // hcf}")
