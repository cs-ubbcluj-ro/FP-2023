"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""


def f_1(n: int):
    for i in range(10):
        for j in range(n):
            print("Hello World")


def f_2(n: int):
    for i in range(n, n + 10):
        for j in range(n):
            print("Hello World")


def f_3(n: int):
    for i in range(1, n):
        for j in range(i, n):
            print("Hello World")


def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")


def f_5(n: int):
    for i in range(n ** 2):
        for j in range(i):
            print("Hello World")


def f_6(n: int):
    for i in range(n):
        t = 1
        while t < n:
            print("Hello World")
            t *= 2


"""
1. Time complexity in both "n" and "m"
"""


def f_7(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, m):
        print("Hello World")


def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")


"""
Analyze the time and space complexity 
"""


def f_11(data: list):
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])


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
