"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import prime_tools

PRIMES = prime_tools.find_primes(1000000)


def main():
    truncated_primes = []
    for prime in PRIMES:
        if ltr_prime(prime) and rtl_prime(prime):
            truncated_primes.append(prime)
    return truncated_primes[4:]


def ltr_prime(prime):
    string = str(prime)
    while string[1:]:
        string = string[1:]
        if string[0]:
            if int(string) not in PRIMES:
                break
    else:
        return True
    return False


def rtl_prime(prime):
    string = str(prime)
    while string[:-1]:
        string = string[:-1]
        if string[0]:
            if int(string) not in PRIMES:
                break
    else:
        return True
    return False


if __name__ == '__main__':
    print(sum(main()))
