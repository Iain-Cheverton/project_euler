"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
import prime_tools

print(prime_tools.find_primes(1_000_000)[10_000])
