"""
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
"""
import functools


@functools.cache
def collatz(starting_term):
    """returns the length of the collatz sequence from the starting term"""
    if starting_term % 2 == 0:
        return 1 + collatz(starting_term // 2)
    if starting_term - 1:
        return 1 + collatz(3 * starting_term + 1)
    return 1


def main():
    """
    returns the starting number and sequence length of the longest collatz
    sequence formed from a starting number under 1_000_000
    """
    longest_sequence = 1
    starting_number = 1
    for i in range(1, 1_000_000):
        sequence_length = collatz(i)
        if sequence_length > longest_sequence:
            longest_sequence = sequence_length
            starting_number = i
    return starting_number, sequence_length


print(main())
