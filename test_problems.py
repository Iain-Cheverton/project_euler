"""This contains pytest tests for the code in this directory"""
import prime_tools
import problem_1
import problem_2
import problem_12


def test_fibonacci():
    """this tests the function fibonacci in problem_2"""
    assert problem_2.fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_problem_1():
    """this tests problem_1 using the example given by project euler"""
    assert problem_1.main(10) == 23


def test_find_primes():
    """this tests the function find_primes against a list of the primes under 10"""
    assert prime_tools.find_primes(10) == [2, 3, 5, 7]


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
