import problem_1
import problem_2
import problem_12
import problem_16
import prime_tools


def test_fibonacci():
    assert problem_2.fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_problem_1():
    assert problem_1.main(10) == 23


def test_find_primes():
    assert prime_tools.find_primes(10) == [2, 3, 5, 7]


def test_prime_factors():
    assert prime_tools.prime_factors(13195) == [5, 7, 13, 29]


def test_problem_12():
    assert problem_12.main(5) == 28
