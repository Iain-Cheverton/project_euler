"""
Consider all integer combinations of a**b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5
If they are then placed in numerical order, with any repeats removed,
we get the following sequence of 15 distinct terms:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
How many distinct terms are in the sequence generated by a ** b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""


def main(max_int, max_power):
    """returns the set of unique terms in the sequence generated by a ** b for 1 < a < max_int and 1 < b < max_power"""
    return {integer ** power for integer in range(2, max_int) for power in range(2, max_power)}


if __name__ == "__main__":
    print(len(main(101, 101)))
