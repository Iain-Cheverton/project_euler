"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import functools
import time
from typing import Tuple

COINS = 1, 2, 5, 10, 20, 50, 100, 200


@functools.cache
def combination_count(total: int, coins: Tuple[int]) -> int:
    """Returns the number of ways to make total with the list of coins"""
    if total == 0:
        return 1
    combinations = 0
    if coins:
        highest_denomination_coin = coins[-1]
        for number_of_highest_denomination_coins in range(total // highest_denomination_coin + 1):
            combinations += combination_count(
                total - number_of_highest_denomination_coins * highest_denomination_coin, coins[:-1]
            )
    return combinations


# 24.2219546 runtime for original solution with loops
# 0.6690868 runtime after recursion
# 0.005155999999999994 runtime after caching


start = time.perf_counter()
print(combination_count(200, COINS), time.perf_counter() - start)
