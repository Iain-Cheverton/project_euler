"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def multiple_sum(upper_bound):
    total = 0
    for i in range(upper_bound):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total


print(multiple_sum(1000))
