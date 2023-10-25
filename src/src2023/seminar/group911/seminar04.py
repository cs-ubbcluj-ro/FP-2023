"""
    Problem Solving Methods -- Divide & Conquer and Backtracking
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive). Return None for
    an empty list
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""

# Alupei Alexandru
import random


def generate_list(n: int) -> list:
    """
    Generate a list of integers
    :param n: list length
    :return: The ascending sorted list
    """

    return sorted([random.randint(0, 100) for i in range(0, n)])


def binary_search(data: list, key: int, left: int, right: int) -> int:
    """
    Search for the key in the sorted list
    :param data: List to search the key in
    :param key: The int value to search
    :param left: low bound for binary search
    :param right: high bound for binary search
    :return: Index of key in list, -1 if key is not found
    """
    if right >= left:
        m = (right + left) // 2
        if key < data[m]:
            return binary_search(data, key, left, m - 1)
        elif key > data[m]:
            return binary_search(data, key, m + 1, right)
        else:
            return m
    else:
        return -1


def exponential_search(data: list, key: int) -> int:
    """
    Exponential search key in list
    :param data: List of ascending sorted numbers
    :param key: Int value to search for
    :return: The position of key or -1 if key is not found
    """
    if len(data) == 0:
        return -1
    if data[0] > key:
        return -1
    if data[-1] < key:
        return -1

    if data[0] == key:
        return 0
    i = 1
    while i < len(data) and data[i] < key:
        i = i * 2
    return binary_search(data, key, i // 2, min(i, len(data) - 1))


# data = generate_list(20)
# print(data)
# print(exponential_search(data, data[10]))

"""
3. Calculate the r-th root of a given number x with a given 
    precision p
"""


# x = 2
# r = 10
# p = 0.001
# # res = ?
# print((x ** 0.1) ** 10)

# 2 - 0.001 <= res ^ 10 <= 2 + 0.001

# Banyai Endre
def root_r(x: int, r: int, p: float) -> float:
    """
    Return the r-th root of number x with precision p
    :param x: Number to find the r-th root for
    :param r: Value of root
    :param p: Precision
    :return: the r-th root
    """
    # x = 3
    # r = 2
    # TODO Handle case when 0 < x <= 1
    min_num = 0
    max_num = max(1, x)
    mid = (min_num + max_num) / 2
    power_r = mid ** r
    while abs(power_r - x) > p:
        # print(mid)
        if x >= 1:
            if power_r < x:
                min_num = mid
            else:
                max_num = mid
        mid = (min_num + max_num) / 2
        power_r = mid ** r
    return mid


# print(root_r(2, 10, 1))
# print(root_r(2, 10, 0.1))
# print(root_r(2, 10, 0.0001))

"""
4. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking
    
    We have a template that we need to customize.
        1. How is the search space represented (values in array X)
        2. When is array X consistent (consistent function)
            -> True iff we can reach a solution strictly by adding values
        3. When do we have a solution
            -> depends on the problem
            
    Permutations of 4
    X is a sequence of values in [1, 4]
    X = [ 1 2 3 4 ] - solution
    X = [ 1 2 4 3 ] - solution
    X = [ 1 3 2 4 ] - solution
            
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


bkt_rec([], 4)

"""
6. Change the code for generating the permutation above to work for the n-Queen problem

    https://medium.com/swlh/how-many-solutions-does-the-n-queens-problem-have-e8da5d45a34c
    X = [ 1 7 4 6 8 2 5 3 ]
    - if the values of X are unique => queens don't attack on row
    - difference between array indices and corresponding array values cannot be equal
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column

    A B C
    C A B
    B C A
    
    X = [ A B C C A B B C A ]
    
    when is array X consistent?
        -> values on current row must be unique (%3 !?)
        -> X[len(X)-1::-3] --> slice going down, 3 values at a time
    solution
        -> len(X) == 9 (nˆ2 generally)
     
7. Generate all the N x N Latin squares for a given number N. 

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
