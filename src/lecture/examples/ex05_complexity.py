"""
Created on Dec 6, 2016

@author: Arthur
"""
import timeit
from texttable import Texttable

'''
    1. Here we have two implementation for the Fibonacci sequence
'''


def fibonacci_iterative(n):
    """
    Iterative implementation for computing n-th term of the Fibonacci sequence
    """
    if n == 0:
        return 0
    x = 0
    y = 1
    for i in range(1, n):
        z = x + y
        x = y
        y = z
    return y


def fibonacci_recursive(n):
    """
    Recursive implementation for computing n-th term of the Fibonacci sequence
    """
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


'''
    2. We test them to see they work correctly
'''


def test_fibonacci():
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(0, len(fib)):
        assert fibonacci_iterative(i) == fib[i], (i, fibonacci_iterative(i))
        assert fibonacci_recursive(i) == fib[i]


test_fibonacci()

'''
    NB!
    To run the function below, you must have installed the texttable component from:
    https://github.com/foutaise/texttable
'''


def build_result_table():
    table = Texttable()
    table.add_row(['Term', 'Iterative', 'Recursive'])
    for term in [10, 20, 30, 32, 34, 36]:
        # Iterative
        start_iter = timeit.default_timer()
        row = fibonacci_iterative(term)
        end_iter = timeit.default_timer()
        # Recursive
        start_rec = timeit.default_timer()
        row = fibonacci_recursive(term)
        end_rec = timeit.default_timer()

        table.add_row([term, end_iter - start_iter, end_rec - start_rec])
    return table


if __name__ == "__main__":
    print(build_result_table().draw())

'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +------+-----------+-----------+
    | Term | Iterative | Recursive |
    +------+-----------+-----------+
    | 10   | 0         | 0         |
    +------+-----------+-----------+
    | 20   | 0         | 3         |
    +------+-----------+-----------+
    | 30   | 0         | 357       |
    +------+-----------+-----------+
    | 32   | 0         | 937       |
    +------+-----------+-----------+
    | 34   | 0         | 2440      |
    +------+-----------+-----------+
    | 36   | 0         | 6437      |
    +------+-----------+-----------+
    
    NB!
    0 milliseconds is not really 0, it's just too short to measure accurately
'''
