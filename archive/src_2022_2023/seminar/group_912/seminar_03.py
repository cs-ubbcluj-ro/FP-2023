"""
1. Determine the time complexity of the following algorithms as a function of n.
source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
n -> size of the algorithm's input
T(n) -> number of operations made by program
T(n) = 1 -> constant time (a single operation) 
O notation -> O(1) is also O(n) is also O(n^2) ... 
"""


# T(n) = 10 * n * 1 => O(n)
def f_1(n: int):
    # does not depend on n
    for i in range(10):
        # depends on n linearly -> O(n)
        for j in range(n):
            # assume print is constant time -> T(1)
            print("Hello World")


# T(n) = 10 * n * 1 => O(n)
def f_2(n: int):
    # does not actually depend on n
    for i in range(n, n + 10):
        # depends on n linearly -> O(n)
        for j in range(n):
            # assume print is constant time -> T(1)
            print("Hello World")


# T(n) = (n-1) * n (simplified)
# T(n) = (n-1) + (n-2) + ... + 1 => O(n^2)
def f_3(n: int):
    # depends on n linearly
    for i in range(1, n):
        # depends on n linearly
        for j in range(i, n):
            print("Hello World")


def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")


# time complexity O(n^4)

# 1 + 2 + ... + (n^2-2) = ((n^2 - 2)*(n^2-1))/2
# (n^2 - 1) * (n^2 - 1)
# complexity is O(n^4)
# if for n = 10, runtime is 1ms, what's the runtime for n = 20 ?
def f_5(n: int):
    # i ranges between 0 and n^2 => first loop is O(n^2)
    for i in range(n ** 2):
        # j depends on i which loops to n^2 => second loop is O(n^2)
        # for j in range(i):  # probably faster, as i starts with lower values
        for j in range(1, n ** 2):
            print("Hello World")


# O(n * log(n))
def f_6(n: int):
    # outer loop is O(n)
    for i in range(n):
        t = 1
        # how many times can we multiply by 2 until we reach n?
        # inner loop is O(log(n))
        while t < n:
            print("Hello World")
            t *= 2


"""
1. Time complexity in both "n" and "m"
"""


# complexity is O(n + m)
# e.g., merging an array with n elements with an array having m elements
def f_7(n, m: int):
    # O(n)
    for i in range(0, n):
        print("Hello World")
    # O(m)
    for j in range(0, m):
        print("Hello World")


# time complexity is O(n)
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# O(n^2)
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# O(n^2)
def f_10(n: int):
    for i in range(n):
        # depends on n => O(n) for inner loop
        for j in range(n, i, -1):
            print("Hello World")


"""
Analyze the time and space complexity 
"""


# n = len(data)
# time complexity is O(n * log_3(n))
# space complexity is O(1)
def f_11(data: list):
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


"""
1. Time comlexity
    T(n) = 1, n <= 1
    T(n) = 2 * T(n /2) + 1
    
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1 
    
T(n) = 2 * T(n /2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 
= 4 * [2 * T(n/8) + 1] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1
    
T(n) = 8 * T(n/8) + 4 + 2 + 1
assume 2^k = n, k = log_2(n)

T(n) = n * T(1) + 2^(k-1) + ... + 2^0 = n + 2^k - 1 = n => O(n)

2. Space complexity
    T(n) = 1, n <= 1
    T(n) = 2 * T(n /2) + n
    T(n/2) = 2 * T(n/4) + n/2
    T(n/4) = 2 * T(n/8) + n/4

T(n) = 2 * T(n /2) + n = 2 * [2 * T(n/4) + n/2] + n = ...
like previously, only with n instead of 1 as final term
"""


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])


# O(n^2 * log_10(n))
def f_13(n: int):
    s = 0
    for i in range(1, n ** 2):  # n^2 loop
        j = i
        while j != 0:  # log_10(i) < log_10(n^2), if n large
            s = s + j - 10 * j // 10
            j //= 10
    return s


"""
T(n) = 1, n <= 1
T(n) = 4 * T(n/2) + 1, n > 1

T(n/2) = 4 * T(n/4) + 1
T(n/4) = 4 * T(n/8) + 1

T(n) = 4 * [4 * T(n/4) + 1] + 1 = 16 * T(n/4) + 4 + 1 =
     = 16 * [4 * T(n/8) + 1] + 4 + 1 =
2^k = n

T(n) = (2^k)^2 * T(1) + 4^(k-1) + ... + 4^0 = n^2 + => O(n^2) 
"""


def f_14(n, i: int):
    if n > 1:
        i *= 2
        m = n // 2
        f_14(m, i - 2)
        f_14(m, i - 1)
        f_14(m, i + 2)
        f_14(m, i + 1)
    else:
        print(i)


"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity

1. What's the time complexity?
2. What does it do?
3. Find a better O(n) to do it in...
"""


def f_15(data: list):
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data):
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


# TODO Time complexity
def f_15_better(data: list):
    freq_dict = {}

    max_freq = 1
    for el in list:
        if el not in freq_dict:
            freq_dict[el] = 1
        else:
            freq_dict[el] += 1
            max_freq = max(freq_dict[el], max_freq)
    return max_freq


"""
What is the time complexity when the following algorithm is implemented via linear exponentiation. How can this be 
optimized and how will that improve the complexity?
"""


def f_16(x, n: int):
    """
    The algorithms returns x ** n
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass


"""
Implement and discuss the complexity of merge sort
"""


def merge_sort(data: list):
    # TODO Implement me
    pass
