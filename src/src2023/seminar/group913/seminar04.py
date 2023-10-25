"""
    Problem Solving Methods -- Divide & Conquer and Backtracking
"""
from random import randint

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
    
    How does exponential search work?
    - we are searching for element <x> in a sorted list
    - take elements in form of 2 ^ i (2^1, 2^2, 2^3, ...) 
    - compare searched element (x) with el. at 2^i until 
                -> end of list
                -> data[2^i] > x => binary search between x[2^(i-1)] and x[2^i] 
"""


def generate_list(n: int) -> list:
    """
    Generate a random, increasing list
    :param n: List length
    :return: The list
    """
    v = []
    for i in range(0, n):
        v.append(randint(0, 100))

    v.sort()
    return v


def binary_search(data: list, key: int, left: int, right: int) -> int:
    """
    Implement binary search between bound left and right
    :param data: Searched list
    :param key: Key we are searching for
    :return: Position where key was found, -1 if key not in list
    """
    while left <= right:
        mid = int(left + (right - left) // 2)

        if data[mid] == key:
            return mid
        elif data[mid] < key:
            left = mid + 1
        elif data[mid] > key:
            right = mid - 1

    return -1


def expo_search(data: list, key: int) -> int:
    """
    Exponential search in given list
    :param data: The list we are searching
    :param key: The search key
    :return: Position where key was found, -1 if key not in list
    """
    if data[0] > key or data[-1] < key:
        return -1

    i = 1
    while i < len(data) and data[i] < key:
        i *= 2

    return binary_search(data, key, i // 2, min(i, len(data) - 1))


# Short test with 10 element list
# data = generate_list(10)
# print(data)
# Search for the last element in the list
# print(expo_search(data, data[-1]))

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
# Dumitrascu Constantin-Alexandri
# Naive implementation

import random


def max_subarray_naive_version(arr) -> (int, int, int):
    """
    T(n) = n ^ 2
    :param arr:
    :return:
    """
    n = len(arr)
    max_sum = -101
    start_index = 0
    end_index = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j

    return max_sum, start_index, end_index


# print(max_subarray_naive_version([-1, -2, -3]))


def generate_random_list(n):
    data = []
    for i in range(n):
        data.append(random.randint(-100, 100))
    return data


# data = generate_random_list(12)
# print("Randomly generated list:", data)
# result, start, end = max_subarray_naive_version(data)
# print("Max subarray sum is:", result)
# print("Indices of the maximum subarray:", start + 1, "to", end + 1)


def maximum_sum_subarray(data: list) -> int:
    """
    Returns the maximum sum of a subarray from the initial array

    T(n) = n => O(n)
    (uses dynamic programming)

    :data: the initial array
    :return: the maximum sum of a subarray from the initial array
    """
    if len(data) == 0:
        return None

    maximum_sum = data[0]
    current_sum = data[0]

    for i in range(1, len(data)):
        if current_sum < 0:
            current_sum = 0

        # current_sum += data[i]

        current_sum = max(data[i], current_sum + data[i])
        # if current_sum + data[i] > 0:
        #     current_sum = current_sum + data[i]
        # else:
        #     current_sum = data[i]

        # if current_sum > maximum_sum:
        #     maximum_sum = current_sum
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


# print(maximum_sum_subarray([-2, -5, 6, -2, -3, 1, 5, -6]))  # = 7
# print(maximum_sum_subarray([-1, -2, -3]))


def max_subarray_dc(data: list, left: int, right: int) -> int:
    """
    Calculate the maximum subarray sum using divide & conquer
    :param data: The list
    :param left: Left bound for divide & conquer
    :param right: Right bound for divide & conquer
    :return: The value of the maximum subarray sum
    """

    # ... ??
    m = (left + right) // 2
    return max(max_subarray_dc(data, left, m), max_subarray_dc(data, m, right),
               max_cross_sum(data, left, right))


def max_cross_sum(data: list, left: int, right: int) -> int:
    """
    Return the value of the maximum subarray sum that includes the midpoint of
    the list
    :param data:
    :return:
    """
    pass


# Deaconu Victor
# Divide & conquer implementation

def max_subarray_sum(data, left, right):
    """
    n = len(data)
    T(n) = 2 * T(n/2) + n
    T(1) = 1, :)
    :param data:
    :param left:
    :param right:
    :return:
    """
    if left == right:
        return data[left]

    mid = (left + right) // 2

    left_sum = float('-inf')
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += data[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, right + 1):
        sum += data[i]
        if sum > right_sum:
            right_sum = sum

    cross_sum = left_sum + right_sum

    return max(max_subarray_sum(data, left, mid),
               max_subarray_sum(data, mid + 1, right),
               cross_sum)


# data = [-2, -5, 6, -2, -3, 1, 5, -6]
# print(max_subarray_sum(data, 0, len(data) - 1))

"""
    Backtracking
        - depth-first search
    
    What do we need to be able to do?
        1. How to represent the search space (array X)
        2. When is the vector X consistent (consistent function)
        3. When do we have a solution (solution function)     
          1 2 3 4
    X = [ 1 3 2 4 ]
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
6. Change the code for generating the permutation above to work for the n-Queen 
   problem
   
   for the position here:
   https://medium.com/swlh/how-many-solutions-does-the-n-queens-problem-have-e8da5d45a34c
   
   we have the following vector X (starting fomr top row):
   X = [ 4 1 3 6 2 7 5 0 ] (vector indices represent rows, values represent the
   position of the queen in the given row)
   
   checking consistency:
    - columns: array X must not contain duplicates
    - diagonal: difference between array indices cannot be equal to difference
                between array values
    - solution: vector is filled (we've placed all n queens)
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column

    1. How do we represent array X?
        A B C 
        C A B
        B C A 
        
    A is 0, B is 1, C is 2
    
    X = [ 0 1 2 2 0 1 1 2 0 ]
    
    2. consistent
        - current row should not have duplicates
        - current column should not have duplicates ( X[::-3]
    3. solution
        - filled in all squares ( len(X) == n*n )

7. Generate all the N x N Latin squares for a given number N. 

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
