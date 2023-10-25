"""
    Problem Solving Methods -- Divide & Conquer and Backtracking


    Divide & Conquer
    divide -> split up the problem into smaller problems similar to the original one
    conquer -> resolve the smallest problems
    combine -> combine the solution the smallest problems to solve the original one

    Merge Sort
    divide -> split the list into two halves
    conquer -> one-element lists are sorted :)
    combine -> merge the lists until we get to the initial size

    Quick Sort
    divide -> select pivot and arrange the elements around it correctly
    conquer -> one-element lists are sorted :)
    combine -> -
"""

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, 
    recursive vs non-recursive). Return None for
    an empty list

    ! All solutions consists of:
        - function that calculates the min
        - separat test function 

    a. Chip & conquer, recursive
        - divide the list into first element AND the remaining elements

    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""

"""
    a. Chip & conquer, recursive
"""


def min_value(data: list):
    """
    n = len(data)
    Time complexity: T(n) = 1 + T(n-1) = 2 + T(n-2) = ... => O(n)
    Space complexity: T(n) = T(n - 1) + (n - 1) => O(nˆ2)

    """
    if len(data) == 0:
        return None

    if len(data) == 1:
        return data[0]

    return min(data[0], min_value(data[1:]))


# print(min_value([-10, 1, 5, 2, 7, -1]))
# print(min_value([]))
# print(min_value([-1, -2]))

"""
    c. Divide in halves, recursive
"""
# Ilies Ariana
import random


# list = []
# n = int(input("enter number"))
# for i in range(n):
#     nr = random.randint(0, 100)
#     list.append(nr)


def _minv(v: list, s: int, d: int):
    if s == d:
        return v[s]
    else:
        m = (s + d) // 2
        x1 = _minv(v, s, m)
        x2 = _minv(v, m + 1, d)
        return min(x1, x2)


def min_value(v: list):
    return _minv(v, 0, len(v))


# print(min([-2, 3, 8, 4, 1, -1]))

# def test_fct():
#     nr = minv(list, 0, n - 1)
#     if nr == min(list):
#         return True
#     else:
#         return False


# print(test_fct())

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""

"""
3. Calculate the r-th root of a given number x with a given precision p

x = 2
r = 10
p = 0.0001
# result = ?

2 - 0.0001 <= result^10 <= 2 + 0.0001 

# 1 ^ 10 = 1
# 2 ^ 10 = 1024
print(1.5 ** 10)
    !! Care in the [0, 1] range !!
"""


# Luscan Alex
def root_r(x: int, r: int, p: float):
    left = float(0)
    right = float(x)
    # res = float(0)
    ok = 1
    while ok == 1:
        res = (left + right) / 2
        if 0 <= left <= 1 and 0 <= right <= 1:
            if res ** 10 <= x:
                right = res
            else:
                left = res
        else:
            if res ** 10 <= x:
                left = res
            else:
                right = res
        if x - p <= (res ** r) <= x + p:
            ok = 0
    return res


# print(root_r(2, 10, 0.0000001))
# print(2 ** 0.1)

# def solve():
#     x = int(input("Choose a value for x: "))
#     r = int(input("Choose a value for r: "))
#     p = float(input("Choose a value for p: "))
#     print(root_r(x, r, p))

# solve()

"""
4. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking
    
    Backtracking -- depth-first search
    we need to customize 2 functions in the generic algorithm:
        - consistent => True iff we can extend what we have up to a solution
        - solution => True iff we found a solution
        
    permutations of 4  
    X = [ 0 2 1 3 ]   
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
   
   example position https://medium.com/swlh/how-many-solutions-does-the-n-queens-problem-have-e8da5d45a34c
   X = [ 4 1 3 6 2 7 5 0 ]
   - each position in the vector represents one row on the chess-like board
   - the values in the vector are the indices at which queens can be found
   
   What checks do we need so queens don't attack on row, column, diagonal?
    row - since we assign one queen per row, no 2 queens can share a row
    column - vector X must have unique values
    diagonal - difference between row indices must be different than those between
                row values
    ! all checks into consistent function
    ! if len(X) == n            
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring 
exactly once in each row and exactly once in each column

Square is
    A B C
    C A B
    B C A

    X = [ A B C C A B B C A] # maybe A - 0, B - 1, ...
    - calculate the row of the placed element
    - what are the elements on the current column? 
        X[len(X)::-3] --> current column must be a mathematical set

7. Generate all the N x N Latin squares for a given number N. 

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
