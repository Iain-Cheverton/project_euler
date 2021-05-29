"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import time
import math
import prime_tools

start_time = time.perf_counter()
integer = 600851475143
primes = prime_tools.find_primes(int(math.sqrt(integer)))
factors = []
for prime in primes:
    while integer % prime == 0:
        factors.append(prime)
        integer /= prime
    if integer == 1:
        print(factors)
        print(time.perf_counter() - start_time)
        exit()
