"""
Created on Dec 6, 2016

@author: Arthur
"""

from texttable import Texttable
import timeit

from lecture.examples.ex05_complexity import fibonacci_recursive, fibonacci_iterative

'''
    4. To speed up the recursive implementation, we use memoization to store interim results
'''
results = {0: 0, 1: 1}


def fibonacci_memoization(n):
    if n not in results:
        results[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return results[n]


dataList = []

'''
    NB!
    To run the function below, you must have installed the texttable component from:
    https://github.com/foutaise/texttable
'''


def build_result_table():
    table = Texttable()
    table.add_row(['Term', 'Iterative', 'Recursive', 'Memoization'])
    for term in [10, 20, 30, 32, 34, 36]:
        # Iterative
        start_iter = timeit.default_timer()
        row = fibonacci_iterative(term)
        end_iter = timeit.default_timer()
        # Recursive
        start_rec = timeit.default_timer()
        row = fibonacci_recursive(term)
        end_rec = timeit.default_timer()
        # Recursive with memoization
        start_mem = timeit.default_timer()
        row = fibonacci_memoization(term)
        end_mem = timeit.default_timer()

        table.add_row([term, end_iter - start_iter, end_rec - start_rec, end_mem - start_mem])
    return table


if __name__ == "__main__":
    print(build_result_table().draw())

'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +------+-----------+-----------+-------------+
    | Term | Iterative | Recursive | Memoization |
    +------+-----------+-----------+-------------+
    | 10   | 0         | 0         | 0           |
    +------+-----------+-----------+-------------+
    | 20   | 0         | 3         | 0           |
    +------+-----------+-----------+-------------+
    | 30   | 0         | 345       | 0           |
    +------+-----------+-----------+-------------+
    | 32   | 0         | 912       | 0           |
    +------+-----------+-----------+-------------+
    | 34   | 0         | 2381      | 0           |
    +------+-----------+-----------+-------------+
    | 36   | 0         | 6215      | 0           |
    +------+-----------+-----------+-------------+

    NB!
    0 milliseconds is not really 0, it's just too short to measure accurately
'''
