"""
1. Determine the time complexity of the following algorithms as a function of n.
source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""


# n -- size of the program's input
# T(n) -- the number of operations the program makes
# Overall
# T(n) = 10 * n * 1 => O(n) is n
def f_1(n: int):
    for i in range(10):  # loops between 0 and 9, so does not depend on n
        for j in range(n):  # does depend on n => O(n) is n
            print("Hello World")  # constant time => T(n) = 1


# Overall
# T(n) = 10 * n * 1, so complexity is O(n)
def f_2(n: int):
    for i in range(n, n + 10):  # 10 iterations, regardless of n's value
        for j in range(n):  # does depend on n => O(n) is n
            print("Hello World")  # T(n) = 1 for the print statement


# Overall
# T(n) = (n - 1) * n * 1
# T(n) = n(n-1)//2
# f_3 is O(n^2) algorithm
def f_3(n: int):
    # n - 1 iterations
    for i in range(1, n):
        # 1 ... n - 1
        # 2 ... n - 1
        # 3 ... n - 1
        # ...
        # n- 1
        for j in range(i, n):
            print("Hello World")


# overall T(n) ~ n^2, so its an O(n^2) algorithm
def f_4(n: int):
    for i in range(n):  # T(n) = n
        for j in range(2 * i + 1):  # T(n) = 2 * n -1
            print("Hello World")


# overall T(n) ~ n^4, so its an O(n^4) algorithm
# let's say that for n = 1000, the algorithm needs 1 ms.
# what's the expected runtime for n = 2000?
# for n = 2000 we expect 2 ^ 4 = 16 ms runtime
def f_5(n: int):
    for i in range(n ** 2):  # T(n) = n^2
        for j in range(i):  # T(n) = n^2
            print("Hello World")


# T(n) = n * log(n), so O(n*log(n)) algorithm
def f_6(n: int):
    for i in range(n):
        t = 1
        while t < n:
            print("Hello World")
            t *= 2  # log(n) in base 2, as we multiply by 2


"""
1. Time complexity in both "n" and "m"
"""


# nr. operations T(n,m) = n + m
# so complexity is O(n+m)
def f_7(n, m: int):
    for i in range(0, n):  # T(n) = n
        print("Hello World")
    for j in range(0, m):  # T(n) = m
        print("Hello World")


# T(n) = 2 * n, so O(n) complexity
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# T(n) = n * (n + n) = 2n^2 => O(n^2) algorithm (also O(n^3), O(n^4))
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# O(n^2)
def f_10(n: int):
    for i in range(n):
        # n ... n - 1 ... 1
        # n ... 2
        # ...
        # n
        for j in range(n, i, -1):
            print("Hello World")


"""
Analyze the time and space complexity 
"""


# input size (n) is the length of the input list (n = len(data))
# T(n) n * log(n) => O(n*log(n))
# extra space is O(1) (same vars allocated every time)
def f_11(data: list):
    data_sum = 0
    for el in data:  # T(n) = n, n iterations
        j = len(data)  # j = n
        while j > 1:  # log base 3 of n
            data_sum += el * j
            j = j // 3  # DIV
    return data_sum


"""
extra time complexity
T(n) = 1, n <= 1
T(n) = 2 * T(n/2) + 1

T(n/2) = 2 * T(n/4) + 1
T(n/4) = 2 * T(n/8) + 1

T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 =
4 * [2 * T(n/8) + 1] + 2 + 1 = 

T(n) = 8 * T(n/8) + 4 + 2 + 1
how do we get to T(1) ??
let's say we have k, so that 2^k = n (k = log(n))

T(n) = 2^k * T(1) + 2^(k-1) + ... + 2^0
T(n) = n + 2^k - 1 = n + n - 1 => O(n)

extra space complexity
T(n) = 1, n <= 1
T(n) = 2 * T(n/2) + 2 * n/2 = 2 * T(n/2) + n 
extra space is O(n^2) ==> look at the time complexity calculation, and redo it
with an additional n in the telescopic sum :)
"""


def f_12(data: list):  # T(n), n = len(data)
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])  # 2 * T(n/2)


# this is an O(n^2 * log(n))
def f_13(n: int):
    s = 0
    for i in range(1, n ** 2):  # T(n) ~ n^2
        j = i
        while j != 0:  # T(n) ~ log(n^2) in base 10
            s = s + j - 10 * j // 10
            j //= 10
    return s


"""
time complexity
T(n) = 1, n <= 1
T(n) = 4 * T(n/2) + 1 
T(n/2) = 4 * T(n/4) + 1
T(n/4) = 4 * T(n/8) + 1

...

T(n) = 4 * T(n/2) + 1 = 4 * [4 * T(n/4) + 1] + 1 =
T(n) = 16 * [4 * T(n/8) + 1] + 4 + 1
T(n) = 64 * T(n/8) + 16 + 4 + 1
to get to T(1), let's pick k so that 2^k = n, so k = log(n)

T(n) = 4^k * T(1) + 4^(k-1) + 4^(k-2) + ... + 4^0
T(n) = 4^(k+1) - 1 ~ 4*4^k = (2^k)^2 = n^2 
"""


def f_14(n, i: int):  # T(n), n decides when the algorithms is done
    if n > 1:
        i *= 2
        m = n // 2
        f_14(m, i - 2)  # T(n//2)
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
What is the time complexity when the following algorithm is implemented via 
linear exponentiation. How can this be 
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
