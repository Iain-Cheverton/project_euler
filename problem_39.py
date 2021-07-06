"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""


def main():
    """Returns the perimeter with the largest number of solutions for right angle triangles with integer side length"""
    current_max = (0, 0)
    for perimeter in range(2, 1001, 2):
        if solution_count(perimeter) > current_max[0]:
            current_max = solution_count(perimeter), perimeter
    return current_max


def solution_count(perimeter):
    """Returns the number of solutions for right angle triangles with integer side length for a given perimeter"""
    count = 0
    for side in range(1, perimeter // 2):
        # the second non-hypotenuse side can be calculated to be:
        # (2 * perimeter * side - perimeter * perimeter) / (2 * (side - perimeter))
        # by substitution using the identities a^2 + b^2 = c^2 and a + b + c = perimeter
        # if there is an integer solution to this expression then
        count += ((2 * perimeter * side - perimeter * perimeter) / (2 * (side - perimeter))).is_integer()
    return count


if __name__ == "__main__":
    print(main())
