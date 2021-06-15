"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
COINS = [1, 2, 5, 10, 100, 200]


def permutations(integer: int) -> int:
    """returns the number of possible permutations of coins to make an integer value"""
    total_permutations = 0
    for coin in COINS:
        if coin > integer:
            break
        total_permutations += permutations(integer - coin)
    return total_permutations if integer else 1


print(permutations(5))
