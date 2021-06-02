"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million"""
import prime_tools

print(sum(prime_tools.find_primes(2_000_000)))
