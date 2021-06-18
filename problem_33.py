"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def main():
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            if check_division(numerator, denominator):
                print(check_division(numerator, denominator))


def check_division(numerator, denominator):
    for digit in str(denominator):
        if (
            digit in str(numerator)
            and int(str(denominator).replace(digit, ""))
            and int(str(numerator).replace(digit, ""))
        ):
            new_denominator = int(str(denominator).replace(digit, ""))
            new_numerator = int(str(numerator).replace(digit, ""))
            if new_numerator and new_denominator:
                if numerator / denominator == new_numerator / new_denominator:
                    return numerator, denominator


print(main())
"""
