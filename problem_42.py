"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a
16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
from problem_22 import VALUES

TRIANGULARS = {n * (n + 1) // 2 for n in range(1000)}
with open("words.txt") as FILE:
    WORDS = [name[1:-1] for name in FILE.read().split(",")]


def triangle(word: str) -> bool:
    """True if the sum of the alphabetical positional values of each letter in the word add to a triangular number"""
    return sum(VALUES[letter] for letter in word) in TRIANGULARS


def main() -> int:
    """Returns the number of triangle words in words.txt"""
    triangle_count = 0

    for word in WORDS:
        triangle_count += triangle(word)
    return triangle_count


if __name__ == "__main__":
    print(main())
