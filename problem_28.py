"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def square(side_length):
    """returns the diagonals of a square with the input side length as described in the problem"""
    diagonals = [1]
    step = 2
    while diagonals[-1] + step <= side_length ** 2 + 1:
        diagonals += [diagonals[-1] + integer * step for integer in range(1, 5)]
        step += 2
    return diagonals


if __name__ == "__main__":
    print(sum(square(1001)))
