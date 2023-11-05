"""
    Greedy + Dynamic programming
"""

"""
    Dynamic programming 101
    what is dynamic programming - a method to optimize the time/space
    complexity of certain algorithms
    
        When can we think to apply it?
        1. Overlapping subproblems
        2. Principle of optimality holds!!??
        3. Apply memoization
"""


def fib_rec(n: int) -> int:
    if n < 2:
        return n
    return fib_rec(n - 2) + fib_rec(n - 1)


# we store already calculated values in the cache
# we know that fib(0) = 0, fib(1) = 1
cache = {0: 0, 1: 1}


def fib_rec_opt(n: int) -> int:
    """
    1. Overlapping subproblems -- to calculate fib(n), we need to calculate
    fib(n-2) and fib(n-1)

    3. Apply memoization -- we store calculated values in the cache
    """
    if n in cache:
        # hopefully O(1)
        return cache[n]

    cache[n] = fib_rec_opt(n - 2) + fib_rec_opt(n - 1)
    return cache[n]


# print(fib_rec(10), fib_rec_opt(10))

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


def max_subarray(data: list) -> int:
    current_sum = data[0]
    max_sum = data[0]

    for i in range(1, len(data)):
        # if current_sum + data[i] > data[i]:
        #     current_sum += data[i]
        # else:
        #     current_sum = data[i]

        # <=> to the if else we have above
        current_sum = max(current_sum + data[i], data[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


# print(max_subarray([-2, -5, 6, -2, -3, 1, 5, -6]))
# print(max_subarray([-2, -5, -6, -2, -3, -1, -5, -6]))

"""
2. Knapsack problem. Given the weights and values of N items, put them in 
a knapsack having capacity W so that you
   maximize the value of the stored items. Items can be broken up
"""

# W = 20
# weights = [1, 3, 4, 5, 8, 11]
# values = [2, 4, 5, 7, 10, 10]

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them 
in a knapsack having capacity W so that you
   maximize the value of the stored items. 
   Items cannot be broken up (0-1 property)
"""


# W = 20
# weights = [7, 15]
# values = [10, 15]

def knapsack_naive_impl(W: int, weights: list, values: list, index: int) -> int:
    # T(n) = 2 * T(n-1) + 1 => O(2ˆn), n -- number of objects
    if index < 0:
        return 0

    # is it better to include or exclude the objects at index?
    include_value = 0
    if W - weights[index] >= 0:
        include_value = values[index] + knapsack_naive_impl(W - weights[index], weights, values, index - 1)
    exclude_value = knapsack_naive_impl(W, weights, values, index - 1)

    # is it better value to include or exclude the object
    return max(include_value, exclude_value)


def knapsack_naive(W: int, weights: list, values: list) -> int:
    return knapsack_naive_impl(W, weights, values, len(values) - 1)


W = 14
weights = [1, 3, 4, 5, 8]
values = [2, 4, 5, 7, 10]

"""
    With dynamic programming
    time complexity
        T(n,W) = n * W (number of objects * size of the knapsack)
    space complexity
        T(W) = W (size of the knapsack)
"""

print(knapsack_naive(W, weights, values))

"""
4. Count in how many ways we can provide change to a given sum of money (N), when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give change in 4 ways (10, 5 + 5, 5 + 1 + ... 
   and 1 + ... + 1)
""" \
 \
"""
5. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
