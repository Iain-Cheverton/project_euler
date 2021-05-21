import pytest


def multiple_sum(upper_bound):
    total = 0
    for i in range(upper_bound):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total


if multiple_sum(10) != 23:
    print("sum is not working correctly")
    exit()


print(multiple_sum(1000))