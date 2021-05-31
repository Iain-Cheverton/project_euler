"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start_time = time.perf_counter()


def main():
    """This function returns the largest palindrome that can be formed by multiplying 2, 3 digit numbers"""
    largest_palindrome = 1
    for int1 in range(100, 1000):
        for int2 in range(100, int1 + 1):
            product = int1 * int2
            if str(product) == str(product)[::-1] and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome


print(main(), time.perf_counter() - start_time)
