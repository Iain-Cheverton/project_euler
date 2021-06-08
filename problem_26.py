"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def cycle_length(divisor):
    """returns the length of the recurring cycle of 1 / divisor"""
    position = 1
    remainder_lookup = {1: 10}
    positions_lookup = {10: 1}
    while (remainder_lookup[position] % divisor) * 10 not in remainder_lookup.values():
        position += 1
        remainder_lookup[position] = (remainder_lookup[position - 1] % divisor) * 10
        positions_lookup[(remainder_lookup[position - 1] % divisor) * 10] = position
    if 0 not in remainder_lookup.values():
        return (
            len(remainder_lookup)
            - positions_lookup[(remainder_lookup[position] % divisor) * 10]
            + 1
        )
    return 0


def main():
    """finds the the integer under 1000 with the longest recurring cycle"""
    current_longest = (0, 0)
    for integer in range(2, 1000):
        length = cycle_length(integer)
        if length > current_longest[1]:
            current_longest = (integer, length)
    return current_longest[0]


print(main())
