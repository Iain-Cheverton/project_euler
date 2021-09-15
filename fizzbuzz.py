"""
A variety of solutions to the standard fizzbuzz interview question
"""


def fizzbuzz_1(start, end):
    """Most obvious just make it work solution"""
    for i_1 in range(start, end):
        if not i_1 % 3:
            if not i_1 % 5:
                print("fizzbuzz")
            else:
                print("fizz")
        elif not i_1 % 5:
            print("buzz")
        else:
            print(i_1)


def fizzbuzz_5(start, end):
    """Most obvious just make it work solution"""
    for i_1 in range(start, end):
        if i_1 % 3 and i_1 % 5:
            print(i_1)
        elif i_1 % 3:
            print("buzz")
        elif i_1 % 5:
            print("fizz")
        else:
            print("fizzbuzz")


def fizzbuzz_2(start, end):
    """cleaner shorter and more expandable / reusable"""
    for i_2 in range(start, end):
        output = ""
        output += "fizz" if not i_2 % 3 else ""
        output += "buzz" if not i_2 % 5 else ""
        print(output if output else str(i_2))


def fizzbuzz_3(start, end):
    """slightly shorter again"""
    for i_3 in range(start, end):
        fizz = "Fizz" if not i_3 % 3 else ""
        buzz = "Buzz" if not i_3 % 5 else ""
        print(f"{fizz}{buzz}" or i_3)


def fizzbuzz_4(start, end):
    """even shorter but less usable"""
    print(*map(lambda i_4: "Fizz" * (not i_4 % 3) + "Buzz" * (not i_4 % 5) or i_4, range(start, end)), sep="\n")


def fizzbuzz_6(start, end):
    """even shorter but less usable"""
    print(*("Fizz" * (not i_4 % 3) + "Buzz" * (not i_4 % 5) or i_4 for i_4 in range(start, end)), sep="\n")


def fizzbuzz_7(start, end):
    """even shorter but less usable"""
    print(*(((i_4, "fizz"), ("buzz", "fizzbuzz"))[not i_4 % 5][not i_4 % 3] for i_4 in range(start, end)), sep="\n")


if __name__ == "__main__":
    fizzbuzz_7(1, 101)
