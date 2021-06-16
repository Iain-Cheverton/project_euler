"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def main():
    """returns the number of different ways can £2 be made using the possible coins"""
    possible_permutations = 0
    for x_1 in range(201):
        for x_2 in range((200 - x_1) // 2 + 1):
            for x_5 in range((200 - x_1 - x_2 * 2) // 5 + 1):
                for x_10 in range((200 - x_1 - x_2 * 2 - x_5 * 5) // 10 + 1):
                    for x_20 in range((200 - x_1 - x_2 * 2 - x_5 * 5 - x_10 * 10) // 20 + 1):
                        possible_permutations += last_bit(x_1, x_2, x_5, x_10, x_20)
    return possible_permutations


def last_bit(x_1, x_2, x_5, x_10, x_20):
    """returns all the possible permutations for given numbers of the smaller coins"""
    section_permutations = 0
    for x_50 in range(5):
        for x_100 in range(3):
            for x_200 in range(2):
                if x_1 + x_2 * 2 + x_5 * 5 + x_10 * 10 + x_20 * 20 + x_50 * 50 + x_100 * 100 + x_200 * 200 == 200:
                    section_permutations += 1
    return section_permutations


print(main())
