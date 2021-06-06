"""
Using names.txt a text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
with open("names.txt") as FILE:
    TEXT = FILE.read()
NAMES = sorted(name[1:-1] for name in TEXT.split(","))
VALUES = {char: value + 1 for value, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
POSITIONS = {name: position_value + 1 for position_value, name in enumerate(NAMES)}


def main():
    """adds the total values of each name in the list"""
    total = 0
    for name in NAMES:
        total += POSITIONS[name] * sum(VALUES[letter] for letter in name)
    return total


if __name__ == "__main__":
    print(main())
