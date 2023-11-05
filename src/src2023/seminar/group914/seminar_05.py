"""
    Greedy + Dynamic programming
"""

"""
Dynamic programming 101
    
    Principle of optimality
    Overlapping subproblems
    Memoization
    
    f(n) = f(n-2) + f(n-1)
"""

# store the first two values of the sequence
cache = {0: 0, 1: 1}


def fib(n: int) -> int:
    """
    Principle of optimality - fib(n-k) is the the solution for finding the n-k'th
                              term of the sequence
    Overlapping subproblems - to calculate n-th term we need all previous terms
    Memoization - building the dictionary of previous values
    """

    # T(n) = 2 * T(n-1) + 1 => O(2ˆn)
    # if n < 2:
    #     return n

    # brave new basic case :)
    if n in cache:
        return cache[n]

    # T(n) = n, as long as cache operations are O(1)
    cache[n] = fib(n - 2) + fib(n - 1)
    return cache[n]


# print(fib(10))

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


def maximum_sum(data: list) -> int:
    # T(n) = n
    """
    Principle of optimality
    Overlapping subproblems - we have the array's elements
    Memoization - current_sum
    """
    current_sum = data[0]
    max_sum = data[0]

    for i in range(1, len(data)):
        # !!??

        # this if is <=> to the one below :)
        # if current_sum + data[i] > data[i]:
        #     current_sum = current_sum + data[i]
        # else:
        #     current_sum = data[i]

        if current_sum > 0:
            current_sum += data[i]
        else:
            current_sum = data[i]

        max_sum = max(max_sum, current_sum)
    return max_sum


"""
2. Knapsack problem. Given the weights and values of N items, put them in a 
   knapsack having capacity W so that you
   maximize the value of the stored items. Items can be broken up
"""

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up (0-1 property)
"""


def knapsack_naive_impl(W: int, weights: list, values: list, index: int) -> int:
    # T(n) = 2 * T(n-1) + 1 => O(2ˆn), n - number of objects

    if index < 0:
        # out of objects
        return 0

    # value if we add object índex
    include_value = 0
    # we can add the object only if there's space left for it
    if W - weights[index] >= 0:
        include_value = values[index] + knapsack_naive_impl(W - weights[index], weights, values, index - 1)
    # value if we don't add object índex
    exclude_value = knapsack_naive_impl(W, weights, values, index - 1)

    return max(include_value, exclude_value)


def knapsack_naive(W: int, weights: list, values: list) -> int:
    return knapsack_naive_impl(W, weights, values, len(weights) - 1)


"""
    Principle of optimality
    Overlapping subproblems
    Memoization
    
    with dp:
    time complexity
        T(n,W) = W * n (size of knapsack * number of objects)
    space complexity
        T(n,W) = W (size of knapsack) (because we never look back more than 1 row 
        in the table, and that row can be overwritten)
"""

W = 11
values = [2, 3, 1, 5, 3, 2]
weights = [1, 2, 3, 3, 5, 6]

# counter-example for using greedy in the 0-1 scenario (items cannot be broken up)
# W = 6
# values =  [5, 3, 3]
# weights = [4, 3, 3]

print(knapsack_naive(W, weights, values))

"""
4. Count in how many ways we can provide change to a given sum of money (N), 
    when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give 
   change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
5. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
