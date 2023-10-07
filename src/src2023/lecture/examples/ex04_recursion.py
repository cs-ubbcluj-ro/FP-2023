"""
Created on Dec 6, 2016

@author: Arthur
"""

'''
    1. Compute the factorial for a given positive integer
'''


def factorial(n):
    """
    Determine the factorial for the given positive integer
    input:
        n - input parameter
    output:
        n!
    """

    '''
    This is  the best case, no recursion
    '''
    if n == 0:
        return 1

    '''
    Recursive step progresses toward the simple case
    '''
    return n * factorial(n - 1)


def test_factorial():
    for n in range(0, 10):
        fact1 = factorial(n)

        fact2 = 1
        for i in range(1, n + 1):
            fact2 *= i

    assert fact1 == fact2


'''
    2. Compute the sum of a list of numbers
'''


def sum_list(lst):
    """
    Calculate the sum of the elements in the list
    input:
        lst - the list
    output:
        The sum of the elements
    """

    '''
    This is  the best case, no recursion
    '''
    if len(lst) == 0:
        return 0

    '''
    Recursive step progresses toward the simple case
    '''
    return lst[0] + sum_list(lst[1:])


def test_sum_list():
    assert sum_list([]) == 0
    assert sum_list([0]) == 0
    assert sum_list([1, 2, 6]) == 9
    assert sum_list([-1, 4, -100, 50]) == -47
    assert sum_list([1, 2, 3, 4, 5, 6]) == 21


'''
    3. Compute the n-th term of the Fibonacci sequence
'''


def fibo(n):
    """
    Computes the n-th term of the Fibonacci sequence
    input:
        n - the index of the desired term
    output:
        The value of the desired term
    """

    '''
    This is  the best case, no recursion
    '''
    if n == 0 or n == 1:
        return 1

    '''
    Recursive step progresses toward the simple case
    '''
    return fibo(n - 2) + fibo(n - 1)


"""
    3a. Compute the n-th term of the Fibonacci sequence
    (tail call recursion - enabled, but not supported in Python, see:
        https://dev.to/rohit/demystifying-tail-call-optimization-5bf3
        https://tratt.net/laurie/blog/2004/tail_call_optimization.html
        http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)
"""


def fib_tail_call(i, current_val=1, next_val=1):
    if i == 0:
        return current_val
    else:
        return fib_tail_call(i - 1, next_val, current_val + next_val)


def test_fibo():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for index in range(0, len(fib)):
        assert fibo(index) == fib[index]
        assert fib_tail_call(index) == fib[index]


'''
    4. Determine whether a given string is a palindrome
'''


def palindrome(s):
    """
    Determine if the given string is a palindrome
    input:
        s - the string
    output:
        True if s is palindrome, False otherwise
    """

    '''
    This is  the best case, no recursion
    '''
    if len(s) < 2:
        return True

    '''
    Recursive step progresses toward the simple case
    '''
    return s[0] == s[-1] and palindrome(s[1:-1])


def test_palindrome():
    assert palindrome("") is True
    assert palindrome("a") is True
    assert palindrome("axa") is True
    assert palindrome("axdf") is False
    assert palindrome("axdfdxa") is True
    assert palindrome("abcddcba") is True
    assert palindrome("abcddca") is False


if __name__ == "__main__":
    test_factorial()
    test_sum_list()
    test_fibo()
    test_palindrome()
