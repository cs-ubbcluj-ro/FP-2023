"""
1. Determine the time complexity of the following algorithms as a function of n.
source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
n -> algorithm's input size
T(n) -> number of operations the algorithm makes for input size "n"
O(n) - high bound on time/space complexity
"""


# T(n) = 10 * n * 1 => O(n)
def f_1(n: int):
    # outer loop runs in constant time => O(1) (without inner loop)
    for i in range(10):
        # inner loop is O(n) it has linear complexity
        for j in range(n):
            # we consider print to be O(1) => constant time
            print("Hello World")


# T(n) = 10 * n * 1 => O(n)
def f_2(n: int):
    # outer loop does not actually depend on size of n
    for i in range(n, n + 10):
        # inner loop is linear complexity
        for j in range(n):
            print("Hello World")


# let's calculate T(n)
# T(n) = (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 => O(n^2)
# replace i with 1 => T(n) = (n-1)^2 => O(n^2)
def f_3(n: int):
    # both loops depend on n
    for i in range(1, n):  # i = 1, 2, 3, ..., n-1
        for j in range(i, n):
            print("Hello World")


"""
T(n) = 1 + 3 + 5 + ... + (2 * n - 1) => O(n^2)
"""


def f_4(n: int):
    for i in range(n):  # 0 ... (n-1) => n iterations
        for j in range(2 * i + 1):  # 2 * (n-1) + 1 = 2 * n - 1
            print("Hello World")


"""
T(n) = (1 + 2 + ... + (i-1)), with i = 0, n^2 -1
last loop: i = n^2 - 1, inner loop runs: n^2 - 1 times
time complexity is O(n^4)

when n = 10, runtime is 1ms; what's the runtime for n = 20?
n = 10 => 10^4 = 10.000 operations
n = 20 => 20^4 = 160.000 operations => 16 times more runtime
"""


# (0) + (0 + 1) + (0 + 1 + 2) + ... + (0 + 1 + 2 + ... + n^2-2)
def f_5(n: int):
    for i in range(n ** 2):  # i = 2
        for j in range(i):  # 0, 1
            print("Hello World")


# O(n * log(n)) -> log base is mul_factor
def f_6(n: int, mul_factor: int = 2):
    counter = 0
    for i in range(n):
        t = 1
        # how many muls before t > n?
        while t < n:
            # print("Hello World")
            counter += 1
            t *= mul_factor  # powers of 5 => exponentiation
    return counter


for factor in [2, 5]:
    print("mul factor is " + str(factor))
    for i in [4, 8, 16, 32, 64, 128]:
        print(str(i) + " -- " + str(f_6(i, factor)))

"""
1. Time complexity in both "n" and "m"
"""


# Time complexity O(n + m)
def f_7(n, m: int):
    # time complexity is O(n)
    for i in range(0, n):
        print("Hello World")
    # time complexity is O(m)
    for j in range(0, m):
        print("Hello World")


# Time complexity O(n)
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# T(n) = n * (n + n) = 2 * n^2 => O(n^2)
def f_9(n: int):
    for i in range(n):  # linear complexity for this loop
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# T(n) = n + n - 1 + ... + 1 => O(n^2)
def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):  # from n to i + 1 (inclusive)
            print("Hello World")


"""
Analyze the time and space complexity 
"""

"""
time complexity: O(n * log_3(n)), n is len(data)
space complexity: O(1) (does not depend on value of "n") 
"""


def f_11(data: list):
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


"""
Time Complexity:
T(n) = 1, n <= 1
T(n) = 1 + T(n/2) + T(n/2) = 2 * T(n/2) + 1

T(n)   = 2 * T(n/2) + 1
T(n/2) = 2 * T(n/4) + 1
T(n/4) = 2 * T(n/8) + 1

T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 =
T(n) = 4 * [2 * T(n/8) + 1] + 2 + 1
T(n) = 8 * T(n/8) + 4 + 2 + 1 (*)
when does T(n/8) become T(1) ?
we assume 2^k=n => k = log_2(n) 
we rewrite (*) in terms of k

T(n) = n * T(1) + 2^(k-1) + ... + 2 + 1
     = n + 2^k - 1 = 2*n - 1 => O(n) 
     
Space complexity:
T(n) = 1, n <= 1
T(n) = 2 * T(n/2) + n
(we redo the calculations for time complexity) => O(n^2) space complexity
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
    for i in range(1, n ** 2):
        # we can approximate that i == n every time
        j = i
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10  # we can divide log_10(j) times
    return s


"""
time complexity
T(n) = 1, n <= 1
T(n) = 4 * T(n/2) + 1

T(n/2) = 4 * T(n/4) + 1
T(n/4) = 4 * T(n/8) + 1

T(n) = 4 * T(n/2) + 1 = 4 * [4 * T(n/4) + 1] + 1 = 16 * T(n/4) + 4 + 1 =
16 * [4 * T(n/8) + 1] + 4 + 1

T(n) = 64 * T(n/8) + 16 + 4 + 1 (**)
when does T(n/8) become T(1) ?
we assume 2^k=n => k = log_2(n) 
we rewrite (**) in terms of k

T(n) = (2^k)^2 * T(1) + 4^(k-1) + ... + 4^0
T(n) = n^2 + n^2 - 1 => O(n^2)
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

1. Determine the time complexity
2. Determine what the function does
3. How to rewrite with better complexity?
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


# O(n * log(n)) time complexity
# O(n) worst space complexity, for lists with unique values
def f_15_better(data: list):
    max_freq = -1
    freq_dict = {}
    for el in data:
        if el not in freq_dict:  # element lookup in Python dict
            freq_dict[el] = 1  # O(log(n))?
        else:
            freq_dict[el] += 1
        max_freq = max(max_freq, freq_dict[el])
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
