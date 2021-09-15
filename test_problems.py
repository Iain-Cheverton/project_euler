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
import problem_33
import problem_34
import problem_35
import problem_36
import problem_37
import problem_38
import problem_39
import problem_40
import problem_41
import problem_42
import problem_43


def test_problem_1():
    """this tests problem_1 using the example given by project euler"""
    assert problem_1.main(10) == 23
    assert problem_1.main(20) == 78


def test_problem_2():
    """this tests that the function fibonacci in problem_2 is equal to the sequence provided"""
    assert problem_2.fibonacci(100) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


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
    assert prime_tools.lcm([1, 2, 4, 9]) == 36
    assert prime_tools.next_prime(9) == 11


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
    """the diagonals of a 5 by 5 square should be [1, 3, 5, 7, 9, 13, 17, 21, 25]"""
    assert problem_28.square(5) == [1, 3, 5, 7, 9, 13, 17, 21, 25]


def test_problem_29():
    """the distinct terms should match those provided in the example"""
    assert problem_29.main(6, 6) == {
        4,
        8,
        9,
        16,
        25,
        27,
        32,
        64,
        81,
        125,
        243,
        256,
        625,
        1024,
        3125,
    }


def test_problem_30():
    """the powers of 4 should match those given in the question"""
    assert problem_30.sums_of_power(4) == [1634, 8208, 9474]


def test_problem_32():
    """the provided example should be in the set"""
    assert 7254 in problem_32.main()


def test_problem_33():
    """the case provided should not return False"""
    assert problem_33.check_division(49, 98)
    assert not problem_33.check_division(49, 97)
    assert problem_33.main() == (387296, 38729600)


def test_sum_of_factorials():
    """145 should equal the sum of its digit's factorials"""
    assert problem_34.sum_of_factorials(145) == 145


def test_problem_35():
    """the circular primes below 100 should match the ones given"""
    assert problem_35.main(100) == {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97}
    assert 197 in problem_35.main(1000)


def test_problem_36():
    """585 should be palindromic in both base 10 and 2"""
    assert problem_36.double_palindrome(585)
    assert not problem_36.double_palindrome(8)
    assert not problem_36.double_palindrome(17)
    assert not problem_36.double_palindrome(18)


def test_problem_37():
    """3797 should be both a left truncatable prime and a right truncatable prime,
    also testing both positives and negatives for both"""
    assert problem_37.lt_prime(3797)
    assert problem_37.rt_prime(3797)
    assert not problem_37.rt_prime(13)
    assert problem_37.lt_prime(13)
    assert problem_37.rt_prime(31)
    assert not problem_37.lt_prime(31)


def test_problem_38():
    """The given example should be in the set of concatenated products"""
    pandigital_set = problem_38.main()
    assert 192384576 in pandigital_set
    # this is the correct answer as calculated by the program and checked on project euler
    assert max(pandigital_set) == 932718654


def test_problem_39():
    """120 should have 3 solutions"""
    assert problem_39.solution_count(120) == 3


def test_problem_40():
    """the given fraction should match the generated one"""
    assert problem_40.concatenate_integers(22) == "0123456789101112131415161718192021"


def test_problem_41():
    """The given example should be prime and pandigital"""
    assert prime_tools.is_prime_array(2143)[-1]
    assert 2143 in problem_41.pandigitals(1, 5)


def test_problem_42():
    """SKY should be in the set of words and should be triangular"""
    assert "SKY" in problem_42.WORDS
    assert problem_42.triangle("SKY")


def test_problem_43():
    """the given example should fulfil the property"""
    assert problem_43.property_check(1406357289)
