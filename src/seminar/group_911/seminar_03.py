"""
1. Determine the time complexity of the following algorithms as a function of n.
source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""


# Overall
# T(n) = 10 * n * 1 = 10 * n, so O(n) is n
# O(n) is also any function growing faster than "n"
# O(n) is also n*log(n), n^2, n^3 ,... , 2^n and so on
# what about a low bound for f_1 ?
# Theta(n) = n, and T(n) = n is both high-bound and low-bound
def f_1(n: int):
    # T(n) = 1, for loop does not depend on n's value, O(n) = 1
    for i in range(10):  # <=> range(0,10) -> from 0 to 9
        # for loop depends on n's value, T(n) = n, so complexity O(n)
        for j in range(n):  # <=> range(0,n) -> from 0 to n - 1
            # print does not depend on n's value, so complexity is O(1)
            # 1 is like f(n) = 1
            print("Hello World")


# Overall
# T(n) = 10 * n * 1, so O(n) = n, Theta(n) = n
def f_2(n: int):
    # does not actually depend on n's value
    for i in range(n, n + 10):  # loops between n .. n + 9 (10 values)
        # inner loop depends on n linearly, so its O(n)
        for j in range(n):
            # print takes constant time to run, so O(1)
            print("Hello World")


# T(n) = n * n * 1 => O(n) = n^2
def f_3(n: int):
    # T(n) = n for the outer loop (linear time)
    for i in range(1, n):
        # Inner loop depends on n, starts with for j in range(1, n)
        # inner loop calculation:
        # 1 + 2 + ... + n - 1
        #     2 + ... + n - 1
        # ...
        # ...           n - 1
        for j in range(i, n):
            print("Hello World")


# Overall
# T(n) = n * n * 1 => O(n) is n^2
def f_4(n: int):
    # outer loop is O(n), with T(n) = n * inner loop
    for i in range(n):
        # j depends on n, final iteration is between 0 and 2 * (n-1) + 1
        for j in range(2 * i + 1):
            print("Hello World")  # O(1) as usual :)


# T(n) = n^2 * n^2 * 1
# O(n) is n^4
#
# Question:
# let's say for n = 1000, it takes 1 ms
# how long do we expect it to run for n = 2000?
# answer: we doubled the size of the input => 2 ^ 4 times more => 16 ms.
# if n = 3000
# 3 ^ 4 => 81 ms.
def f_5(n: int):
    # T(n) = n^2 for outer loop
    for i in range(n ** 2):
        # T(n) = n^2 for inner loop
        for j in range(i):
            print("Hello World")  # O(1)


def f_6(n: int):
    for i in range(n):
        # How many times can we multiply by 2 in order to go from 1 to n?
        # Answer is log(n) times
        t = 1
        while t < n:
            print("Hello World")
            t *= 2  # log is base 2 as we multiply by 2


"""
1. Time complexity in both "n" and "m"
"""


# overall ??
# T(n,m) = n + m, so its O(n+m)
# another example -- when merging arrays of lengths n and m, O(n+m) = n + m
# as we look at each merged element exactly one time
def f_7(n, m: int):
    # T(n) = n, so for the loop O(n) = n
    for i in range(0, n):
        print("Hello World")
    # T(n) = m, so for the loop O(n) = m
    for j in range(0, m):
        print("Hello World")


# T(n) = n + n = 2*n
# O(n) = n
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# O(n) is n^2
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# O(n) is n^2
def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")


"""
Analyze the time and space complexity 
"""


# O(n) is n * log(n) (log is base 3)
# extra space complexity is O(1)
def f_11(data: list):
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3  # we get log base 3 of n (j always stars at n)
    return data_sum


"""
time complexity
T(n) = 1, if n <= 1
T(n) = 2 * T(n/2) + 1

T(n) = 2 * T(n/2) + 1
T(n/2) = 2 * T(n/4) + 1
T(n/4) = 2 * T(n/8) + 1

T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 =
4 * [2 * T(n/8) + 1] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1

T(n) = 8 * T(n/8) + 4 + 2 + 1 ... and so on
we know T(0) = T(1) = 1
let's say we have k natural number so that 2 ^ k = n, k = log(n)

T(n) = k * T(1) + sum of the powers of 2 (2^0 + 2^1 + ... + 2^(k-1))  
T(n) = k * 1 + 2^k - 1 = log(n) + n => O(n) is n

extra space complexity
T(1) = 1
T(n) = 2 * T(n/2)
"""


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])  # T(n/2) + T(n/2)


def f_13(n: int):
    s = 0
    for i in range(1, n ** 2):
        j = i
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10
    return s


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
