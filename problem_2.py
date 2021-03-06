"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fibonacci(bound):
    """returns a list of the Fibonacci sequence up to a bound"""
    fibonacci_list = [1, 1]
    while fibonacci_list[-1] + fibonacci_list[-2] < bound:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list


def even_fibonacci(bound):
    """returns a list of the even valued terms of the Fibonacci sequence up to a bound"""
    fibonacci_list = fibonacci(bound)
    return [term for term in fibonacci_list if not term % 2]


if __name__ == "__main__":
    print(sum(even_fibonacci(4_000_000)))
