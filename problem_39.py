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
        # By substitution using the identities a^2 + b^2 = c^2 and a + b + c = perimeter,
        # the second non-hypotenuse side can be calculated to be:
        # (2 * perimeter * side - perimeter * perimeter) / (2 * (side - perimeter))
        # If there is an integer solution to this expression then the hypotenuse is also integer since it can be written
        # as c = perimeter - a - b where a,b perimeter are all integer.
        # Therefore we have an integer solution and can increase the count.
        count += ((2 * perimeter * side - perimeter * perimeter) / (2 * (side - perimeter))).is_integer()
        # Each solution is counted twice, when the variable side takes the two different side lengths of the solution
        # There are no un-duplicated solutions since this means both sides are equal,
        # and then the hypotenuse is an integer multiple of sqrt(2) so non integer
    return count // 2


if __name__ == "__main__":
    print(main())
