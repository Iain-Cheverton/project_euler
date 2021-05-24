"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(string):
    for i in range(int(len(string))):
        if string[i] != string[-(i + 1)]:
            return False
    return True


largest_palindrome = 1
for x in range(100, 1000):
    for y in range(100, x):
        product = x * y
        if palindrome(str(product)) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)
