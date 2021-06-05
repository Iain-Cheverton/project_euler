"""What is the value of the first triangle number to have over five hundred divisors?"""
import prime_tools


def main(min_factors):
    """This returns the first triangular number with over min_factors divisors"""
    for term_number in range(1, 1000000):
        total_factors = 1
        prime_factors = prime_tools.dict_factors(term_number * (term_number + 1) // 2)
        for prime in prime_factors:
            total_factors *= prime_factors[prime] + 1
        if total_factors > min_factors:
            return (term_number * (term_number + 1)) // 2
    return "pylint made me add this"


print(main(500))
