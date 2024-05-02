"""
12. Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers 
    up to a specified limit using the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.
"""

def era_crivello(limit:int) -> list[int]:
    prime_numbers:list = [i for i in range(limit)]

    for i in range(2, limit):
        if i in prime_numbers\
        and i*i <= limit:
            for xi in range(2, limit):
                if i*xi in prime_numbers\
                and i*xi <= limit:
                    prime_numbers.remove(i*xi)
                elif i*xi > limit:
                    break

    return prime_numbers

print(era_crivello(16147))