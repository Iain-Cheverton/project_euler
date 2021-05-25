"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start_time = time.perf_counter()

largest_palindrome = 1
for x in range(100, 1000):
    for y in range(100, x + 1):
        product = x * y
        if str(product) == str(product)[::-1] and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome, time.perf_counter() - start_time)
