"""If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage."""
LOOKUP = {
    0: None,
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
}


def main():
    """returns the total number of letters in all numbers between 1 and 1000 (inclusive)"""
    total_letters = 0
    for integer in range(1, 1000):
        num = str(integer)
        if 0 < integer < 100:
            total_letters += tens_units(integer)
        elif num.endswith("00"):
            total_letters += len(LOOKUP[int(num[0])]) + len(LOOKUP[100])
        else:
            total_letters += len(LOOKUP[int(num[0])]) + len(LOOKUP[100]) + len("and") + tens_units(int(num[-2:]))
    total_letters += len("onethousand")
    return total_letters


def tens_units(integer):
    """returns the total number of letters for a number between 1 and 99"""
    letters = 0
    num = str(integer)
    if integer < 21:
        letters += len(LOOKUP[integer])
    if 20 < integer < 100:
        if num[1] == "0":
            letters += len(LOOKUP[integer])
        else:
            letters += len(LOOKUP[int(num[0] + "0")]) + len(LOOKUP[int(num[1])])
    return letters


print(main())
