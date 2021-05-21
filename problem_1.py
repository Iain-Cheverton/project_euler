def multiple_sum(upper_bound):
    total = 0
    for i in range(upper_bound):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total


print(multiple_sum(1000))
