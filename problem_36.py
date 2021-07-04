"""
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def main():
    """returns a list of all numbers under 1000000 that are palindromic in both base 10 and 2"""
    return list(filter(double_palindrome, range(1_000_000)))


def double_palindrome(integer: int):
    """True if the integer is palindromic in both 10 and 2 else false"""
    return str(integer) == str(integer)[::-1] and bin(integer)[2:] == bin(integer)[:1:-1]


if __name__ == "__main__":
    print(sum(main()))
