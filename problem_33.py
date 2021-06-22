"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


def main():
    """returns the product of the numerators and denominators of the four desired fractions """
    total_numerator = 1
    total_denominator = 1
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            fraction = check_division(numerator, denominator)
            if fraction:
                total_numerator *= fraction[0]
                total_denominator *= fraction[1]
    return total_numerator, total_denominator


def check_division(numerator, denominator):
    """returns a new numerator and denominator for a fraction,
     if it can be simplified by 'cancelling' a digit from each"""
    for digit in str(denominator):
        if (
            digit in str(numerator)
            and str(denominator).replace(digit, "")
            and str(numerator).replace(digit, "")
        ):
            new_denominator = int(str(denominator).replace(digit, ""))
            new_numerator = int(str(numerator).replace(digit, ""))
            if new_numerator and new_denominator:
                if numerator / denominator == new_numerator / new_denominator and int(str(denominator)[-1]):
                    return new_numerator, new_denominator
    return False


if __name__ == '__main__':
    to_print = main()
    print(to_print[0] // to_print[0], to_print[1] // to_print[0])

