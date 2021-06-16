"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


def main():
    """returns a set of products that form a 1 through 9 pandigital equation with a pair of their factors"""
    products = set()
    for smaller_factor in range(99):
        for larger_factor in range(9877):
            product = smaller_factor * larger_factor
            combined_digits = str(smaller_factor) + str(larger_factor) + str(product)
            if len(combined_digits) == 9:
                for digit in "123456789":
                    if digit not in combined_digits:
                        break
                else:
                    products.add(product)
    return products


if __name__ == "__main__":
    print(sum(main()))
