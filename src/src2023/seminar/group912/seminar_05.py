"""
    Greedy + Dynamic programming

    Dynamic programming
    -> it's a specific way to optimize finding a solution to a problem

    1. Principle of optimality
    2. Overlapping subproblems
    3. Memoization
"""


def fib_naive(n: int) -> int:
    if n < 2:
        return n
    return fib_naive(n - 2) + fib_naive(n - 1)


# Memoization -- in the cache
cache = {0: 0, 1: 1}  # base case in the cache


def fib_dp(n: int) -> int:
    if n in cache:
        return cache[n]  # hopefully cache[n] is O(1)
    cache[n] = fib_dp(n - 2) + fib_dp(n - 1)  # Overlapping subproblems
    return cache[n]


# print(fib_naive(10), fib_dp(10))

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


def max_subarray_dp(data: list) -> int:
    max_sum = data[0]
    current_sum = data[0]

    for i in range(1, len(data)):
        # if current_sum + data[i] >= data[i]:
        #     current_sum += data[i]
        # else:
        #     current_sum = data[i]

        # <=> to the if above
        current_sum = max(data[i], data[i] + current_sum)
        # current_sum stores the largest sum ending at index i

        # if current_sum > max_sum, then update max_sum
        max_sum = max(max_sum, current_sum)
    return max_sum


# print(max_subarray_dp([-2, -5, 6, -2, -3, 1, 5, -6]))
# print(max_subarray_dp([-2, -5, -6, -2, -3, -1, -5, -6]))

"""
2. Knapsack problem. Given the weights and values of N items, put them in a knapsack having 
   capacity W so that you maximize the value of the stored items. Items can be broken up
"""

W = 13
objects = [(5, 10), (2, 12), (1, 2), (6, 7), (6, 9)]  # tuples of (weight, value)
# (5, 10), (2, 12), (6, 9)
"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up (0-1 property)
   
   with dynamic programming:
   time complexity:
   T(n,W) = n * W, where n -- number of objects, W -- size of knapsack
   
   space complexity:
   T(W) = W 
   
"""


# counter-example for the greedy method
# W = 10
# objects = [(10, 10), (2, 4)]
# objects = [(9, 10), (1, 1), (5, 5), (5, 5)]

def knapsack_01_impl(W: int, objects: list, index: int) -> int:
    # T(n) = 2 * T(n-1) + 1 => O(2ˆn), where n is the number of objects
    if index < 0:
        return 0

    include_value = 0
    if W - objects[index][0] >= 0:
        include_value = objects[index][1] + knapsack_01_impl(W - objects[index][0], objects, index - 1)
    exclude_value = knapsack_01_impl(W, objects, index - 1)
    return max(include_value, exclude_value)


def knapsack_01(W: int, objects: list) -> int:
    return knapsack_01_impl(W, objects, len(objects) - 1)  # start with the last object


print(knapsack_01(W, objects))

"""
4. Count in how many ways we can provide change to a given sum of money (N), when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give change in 4 ways (10, 5 + 5, 5 + 1 + ... 
   and 1 + ... + 1)
"""

"""
5. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
   
   n - rows
   m - columns
   T(n,m) = m * 3 * T(n-1) + 1 => O(3ˆn) * m?
"""
