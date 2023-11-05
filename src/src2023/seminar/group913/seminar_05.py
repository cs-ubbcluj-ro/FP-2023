"""
    Greedy + Dynamic programming
"""

"""
    Dynamic programming
        1. Principle of optimality
        2. Overlapping subproblems
        3. Memoization
"""

# we place already computed values in the cache
# we add the base cases to the cache (fib(0) = 0, fib(1) = 1)
cache = {0: 0, 1: 1}


def fib(n: int) -> int:
    """
    2. Overlapping subproblems - to calculate fib(n) we need to first calculate
        fib(n-2), fib(n-1)
    3. Memoization - place already calculated values in the cache
    """

    # if n < 2:
    #     return n
    if n in cache:
        # if the value is in the cache we return it
        return cache[n]
    # add the value to the cache then return it
    cache[n] = fib(n - 2) + fib(n - 1)
    return cache[n]
    # return fib(n - 2) + fib(n - 1)


# print(fib(10))

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


def maximum_subarray_dp(data: list) -> int:
    current_sum = data[0]
    max_sum = data[0]

    for i in range(1, len(data)):
        # if current_sum + data[i] > data[i]:
        #     current_sum = current_sum + data[i]
        # else:
        #     current_sum = data[i]

        # this is the same as the if statement above
        current_sum = max(current_sum + data[i], data[i])

        # do we need to update the max_sum?
        max_sum = max(max_sum, current_sum)
    return max_sum


# print(maximum_subarray_dp([-2, -5, 6, -2, -3, 1, 5, -6]))

"""
2. Knapsack problem. Given the weights and values of N items, put them in a 
    knapsack having capacity W so that you
    maximize the value of the stored items. Items can be broken up
"""

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a 
knapsack having capacity W so that you
   maximize the value of the stored items. 
   Items cannot be broken up (0-1 property)
   
   Using dynamic programming:
   time complexity:
    T(n,W) = n * W (n - number of objects, W - size of knapsack)
   space complexity:
    T(n,W) = W (W - size of knapsack, constant relatvie to the number of objects)     
"""


def knapsack_naive_impl(W: int, weights: list, values: list, index: int) -> int:
    # T(n) = 2 * T(n-1) + 1 => O(2ˆn), where 'n' is the number of objects
    if index < 0:
        return 0

    # we are considering object at index
    value_include = 0
    # does the object at index fit in the knapsack
    if W - weights[index] >= 0:
        value_include = values[index] + knapsack_naive_impl(W - weights[index], weights, values, index - 1)
    value_exclude = knapsack_naive_impl(W, weights, values, index - 1)

    return max(value_exclude, value_include)


def knapsack_naive(W: int, weights: list, values: list) -> int:
    return knapsack_naive_impl(W, weights, values, len(weights) - 1)


W = 14
weights = [2, 5, 3, 9, 1]
values = [8, 4, 6, 9, 2]

# weights = [1, 2, 3, 5, 9]
# values = [2, 8, 6, 4, 9]

print(knapsack_naive(W, weights, values))

# counterexample for using the greedy method when objects cannot be broken up
# W = 20
# values =  [14,  9, 7]
# weights = [14, 10, 8]


"""
4. Count in how many ways we can provide change to a given sum of money (N), 
    when provided infinite    supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give 
   change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

# N = 10, coins = [1,5,10]
# 10 = 10 * 1
# 10 = 1 * 5 + 5 * 1
# 10 = 2 * 5
# 10 = 1 * 10 => 4 ways of making change


"""
5. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
