"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
with open("names.txt") as FILE:
    TEXT = FILE.read()
NAMES = sorted(TEXT.split(","))
VALUES = {
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[position]: position + 1 for position in range(26)
}


def main():
    """adds the total values of each name in the list"""
    position = 0
    total = 0
    for name in NAMES:
        position += 1
        total += position * sum(VALUES[letter] for letter in name[1:-1])
    return total


if __name__ == "__main__":
    print(main(), NAMES[937], sum(VALUES[letter] for letter in NAMES[937][1:-1]))
