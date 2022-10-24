"""
Divide & Conquer

1. Divide - the problem into smaller subproblems (not overlapping)
2. Conquer - solve the "small" problems directly (no d&c)
3. Combine - "small" problem results into the solution of the original one

Binary search
1. Divide => decide in which half of the array to continue
2. Conquer => find the element/run out of list (left >= right)
3. Combine => nothing to do here

Merge Sort
1. Divide => split the array into two halves
2. Conquer => single-element arrays are already sorted
3. Combine => merge arrays until we get to the large, sorted one

Quick Sort
1. Divide => select a pivot, partition the array around it
2. Conquer => continue for the subarrays left and right of pivot
3. Combine => nothing to do here
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""
import random


def _find_min_impl(array: list, index: int):
    """
    Return the smallest element in the array.
    :param index:
    :param array:
    :return: Smallest element in array. None if array is empty.
    """
    if len(array) - 1 == index:
        return array[index]
    return min(array[index], _find_min_impl(array, index + 1))


def find_min(array: list):
    if len(array) == 0:
        return None
    return _find_min_impl(array, 0)


def test_find_min():
    # length of random list
    n = random.randint(0, 50)
    data = []
    for i in range(n):
        data.append(random.randint(1, 10))

    # insert the known minimal element in a random, but known position
    index = random.randint(0, len(data) - 1)
    data.insert(index, -1)

    print(data)
    result = find_min(data)
    assert result == -1, (result, index)


test_find_min()

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""

"""
3. Calculate the r-th root of a given number x with a given precision p
"""

"""
4. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking
"""

"""
5. Recursive implementation for permutations
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
6. Change the code for generating the permutation above to work for the n-Queen problem
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column

7. Generate all the N x N Latin squares for a given number N. 

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
