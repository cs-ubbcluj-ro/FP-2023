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


def generate_list(n: int) -> list:
    """
    Generate a sorted list of integers
    :param n: List length
    :return: The ascending sorted list
    """
    pass


def binary_search(data: list, key: int, left: int, right: int) -> int:
    """
    Search for the key in the list
    :param data: Ascending sorted list to search the key in
    :param key: The int value to search
    :param left: low bound for binary search
    :param right: high bound for binary search
    :return: Index of key in list, -1 if key is not found
    """
    pass

def exponential_search(data:list,key:int) -> int:
    """
    Exponential search key in data
    :param data: List of ascending sorted numbers
    :param key: int value to search for
    :return: The position of key, or -1 if key not in list
    """
    pass


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
