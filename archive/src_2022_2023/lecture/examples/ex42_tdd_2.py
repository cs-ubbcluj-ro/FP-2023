"""
How to apply TDD - a simple example

Problem statement:
Every even number larger or equal to 4 can be expressed as the sum of two primes (Goldbach conjecture). For a given even
number, determine the two primes that express it.
"""

'''
0. Think 
- what function do you need? 
- what are its specifications?
'''

'''
1. Write the function specification
'''


def is_prime(n):
    """
    Tests whether the provided parameter is a prime number
    input: n - the number to be tested
    output: True if 'n' is prime
    """
    pass


def find_goldbach_primes(n):
    """
    Returns the two primes that sum to the given even 'n'
    input: n - an even natural number
    output: return the smallest of the two primes that sum to 'n'
    error: raises a ValueError if input is not an even natural number
    """
    pass


'''
2. Write a test for it
'''


def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(-100, 50):
        assert is_prime(i) == (i in primes)


def test_find_goldbach_primes(n):
    pairs = [(4, 2), (8, 3), (12, 5), (16, 5)]
    for p in pairs:
        assert p[1] == find_goldbach_primes(p[0])
    for i in range(-10, 2):
        try:
            find_goldbach_primes(i)
            assert False
        except ValueError:
            assert True
    for i in range(1, 100, 2):
        try:
            find_goldbach_primes(i)
            assert False
        except ValueError:
            assert True


'''
3. Run the test. It will fail because the isPrime(n) function does not yet do anything useful.
'''

'''
4. Write the isPrime(n) function so that the test passes
'''


def is_prime(n):
    """
    Tests whether the provided parameter is a prime number
    input: n - the number to be tested
    output: True if 'n' is prime
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def find_goldbach_primes(n):
    """
    Returns the two primes that sum to the given even 'n'
    input: n - an even natural number
    output: return the smallest of the two primes that sum to 'n'
    error: raises a ValueError if input is not an even natural number
    """
    if n < 2 or n % 2 == 1:
        raise ValueError("Goldbach conjecture requires an even parameter!")
    i = 2
    while i < n:
        if is_prime(i) and is_prime(n - i):
            return i


'''
5. Refactor the code. Make it easier to read, faster, ...
'''


def is_prime(n):
    """
    Tests whether the provided parameter is a prime number
    input: n - the number to be tested
    output: True if 'n' is prime
    """
    if n < 2:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
    return True


'''
6. Run the tests again! Make sure that they pass.
'''
