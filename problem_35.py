"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
import prime_tools


def main(bound):
    """returns a set of all circular primes below a bound"""
    circular_primes = set()
    is_prime = prime_tools.is_prime_array(bound)
    for integer in range(bound):
        if is_prime[integer]:
            rotation = str(integer)
            while is_prime[int(rotation)]:
                rotation = rotation[1:] + rotation[0]
                if int(rotation) == integer:
                    circular_primes.add(integer)
                    break
    return circular_primes


if __name__ == "__main__":
    print(len(main(1_000_000)))
