"""This contains pytest tests for the code in this directory"""
import itertools

import prime_tools
import problem_1
import problem_2
import problem_12
import problem_21
import problem_22
import problem_26
import problem_27
import problem_28
import problem_29
import problem_30
import problem_32


def test_fibonacci():
    """this tests that the function fibonacci in problem_2 is equal to the sequence provided"""
    assert problem_2.fibonacci(100) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_problem_1():
    """this tests problem_1 using the example given by project euler"""
    assert problem_1.main(10) == 23


def test_find_primes():
    """this tests the function find_primes against a list of the primes under 10"""
    assert prime_tools.find_primes(10) == [2, 3, 5, 7]
    assert prime_tools.find_primes(2) == [2]


def test_prime_factors():
    """this tests the function prime_factors against a list of the factors of 13195 provided by project euler"""
    assert prime_tools.prime_factors(13195) == [5, 7, 13, 29]


def test_problem_12():
    """this tests problem 12 using the example given by project euler"""
    assert problem_12.main(5) == 28


def test_prime_tools():
    """the prime after 1 should be 2"""
    assert prime_tools.next_prime(1) == 2
    assert prime_tools.prime_factors(2) == [2]


def test_problem_21():
    """220 and 284 should be an amicable pair"""
    assert problem_21.amicable_pair(220) == 284


def test_problem_22():
    """the 938th name should be COLIN and should have the value provided in the question"""
    assert problem_22.NAMES[937] == "COLIN"
    assert sum(problem_22.VALUES[letter] for letter in problem_22.NAMES[937]) == 53


def test_problem_23():
    """permutations should be in lexicographic order if the initial string was also in lexicographic order"""
    test_list = ["".join(term) for term in list(itertools.permutations("1234"))]
    assert test_list == sorted(test_list)


def test_cycle_length():
    """the length of the recurring cycles should match those provided"""
    assert problem_26.cycle_length(7) == 6
    assert problem_26.cycle_length(6) == 1
    assert problem_26.cycle_length(3) == 1


def test_consecutive_primes():
    """the number of consecutive primes from the provided equations should match the number given in the problem"""
    assert problem_27.consecutive_primes(-79, 1601) == 80
    assert problem_27.consecutive_primes(1, 41) == 40


def test_problem_28():
    """the sum of the diagonals of a 5 by 5 square should be 101"""
    assert sum(problem_28.square(5)) == 101


def test_problem_29():
    """the distinct terms should match those provided in the example"""
    assert problem_29.main(6, 6) == {4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125}


def test_problem_30():
    """the powers of 4 should match those given in the question"""
    assert problem_30.sum_of_powers(4) == [1634, 8208, 9474]


def test_problem_32():
    """the provided example should be in the set"""
    assert 7254 in problem_32.main()
