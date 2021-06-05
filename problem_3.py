"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time

import prime_tools

start_time = time.perf_counter()
print(prime_tools.prime_factors(600851475143))
print(time.perf_counter() - start_time)
