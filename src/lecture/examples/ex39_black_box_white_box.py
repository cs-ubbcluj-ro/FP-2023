"""
Created on Nov 14, 2016

@author: Arthur
"""

"""
    A function that we want tested
"""


def is_prime(nr):
    """
    Verify if a number is prime
    return True if nr is prime, False otherwise
    raise ValueError if nr <= 0
    """
    if nr <= 0:
        raise ValueError("nr needs to be positive")
    if nr == 1:
        return False
    if nr <= 3:
        return True
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


"""
    Black-box testing assumes we only have its specification
"""


def test_is_prime_black_box():
    for i in range(-100, 1):
        try:
            is_prime(i)
            assert False
        except ValueError:
            pass

    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in range(2, 20):
        assert is_prime(i) == (i in primes), "this is the value where it fails: " + str(i)


"""
    White-box testing - we can see the source code, so we only write the required test cases
"""


def test_is_prime_white_box():
    try:
        is_prime(-5)
        assert False
    except ValueError:
        pass

    assert is_prime(1) is False, 1
    assert is_prime(2) is True, 2
    assert is_prime(3) is True, 3
    assert is_prime(6) is False, 4
    assert is_prime(7) is True, 7
    assert is_prime(8) is False, 8


"""
    Let's run the tests - they should work regardless
"""
if __name__ == "__main__":
    test_is_prime_black_box()
    test_is_prime_white_box()
