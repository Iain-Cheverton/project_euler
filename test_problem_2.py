import problem_2


def test_fibonacci():
    assert problem_2.fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
