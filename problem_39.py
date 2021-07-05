"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""


def main():
    """Returns the perimeter with the largest number of solutions for right angle triangles with integer side length"""
    current_max = (0, 0)
    for perimeter in range(1001):
        if solution_count(perimeter) > current_max[0]:
            current_max = (solution_count(perimeter), perimeter)
    return current_max[1]


def solution_count(perimeter):
    """Returns the number of solutions for right angle triangles with integer side length for a given perimeter"""
    count = 0
    for medium_side in range(perimeter // 2):
        for short_side in range(min(medium_side + 1, perimeter - 2 * medium_side)):
            if (perimeter - medium_side - short_side) * (
                perimeter - medium_side - short_side
            ) == medium_side * medium_side + short_side * short_side:
                count += 1
    return count


if __name__ == "__main__":
    print(main())
