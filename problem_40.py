"""
An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910(1)112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1_000 × d10_000 × d100_000 × d1_000_000
"""


def concatenate_integers(bound):
    """concatenates all the non-negative integers up to a bound"""
    return "".join(str(x) for x in range(bound))


def main():
    """multiplies all the required digits of the irrational number"""
    fraction = concatenate_integers(500_000)
    return (
        int(fraction[1])
        * int(fraction[10])
        * int(fraction[100])
        * int(fraction[1_000])
        * int(fraction[10_000])
        * int(fraction[100_000])
        * int(fraction[1_000_000])
    )


if __name__ == "__main__":
    print(main())
