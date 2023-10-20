"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
Complexity analysis

Notations:
    - n = size of the input (number of elements that have to be processed - but we can also have n, m, ... if multiple inputs)
    - A = the algorithm
    - T(n) = number of steps (operations) the algorithm does
    
    - O(n) - upper bound - my algorithm cannot go worse than this
    - Omega(n) - low bound - my algorithm cannot go better than this
    - Theta(n) - both upper and lower bound - my algorithm always has the same complexity (BC=AC=WC)
    
Cases
    - BC(A): case in which we do least number of steps
    - AC(A): formula
    - WC(A): case in which we do most steps
    
Complexity in terms of:
    - time: number of operations taken to solve the problem
    - space
"""


# Terebent Roxana
# T(n) = 10*n,
# O(n) - upper bound
# Theta(n) - it always performs 10*n steps
#           (no cases in which it does less/more)
def f_1(n: int):
    for i in range(10):  # i=0..9
        for j in range(n):  # j=0..n
            print("Hello World")


# Voda Ioan
# T(n) = 10*n, O(n)/Theta(n)
def f_2(n: int):
    for i in range(n, n + 10):  # i=n+0, n+1 .. n+9
        # it goes in constant number of steps (10 steps)
        for j in range(n):
            # it depends to n - j = 0,1..n-1
            print("Hello World")


# Schiop Bogdan
# T(n) = n(n-1)/2 = O(n^2)
# explicit computations (will be) available (shortly) in separate file
def f_3(n: int):
    for i in range(1, n):  # i = 1 .. (n-1)
        for j in range(i, n):  # j = i, i+1..n-1
            print("Hello World")


# Serban Dragos
# O(n^2)
def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1):
            print("Hello World")


# Tiut Cristian
# T(n) = (n^2-1)*n^2 -> O(n^4)
def f_5(n: int):
    for i in range(n ** 2):
        for j in range(i):
            print("Hello World")


def f_run(n: int):
    val = 0
    for i in range(n ** 2):
        for j in range(i):
            val += 1
    return val


for i in range(13):
    print(i, f_run(i))


# O(n*log2(n))
def f_6(n: int):
    for i in range(n):  #0..n
        t = 1
        while t < n:  # how many times can we multiply by 2 until we get to n?
            print("Hello World") #A: as many times as n can be divided by 2 -> log2(n)
            t *= 2


"""
1. Time complexity in both "n" and "m"
"""


# Szarics Iulia
# O(n+m)
def f_7(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, m):  # m iterations
        print("Hello World")


# Tiganasu Alexandru
# T(n) = 2*n ->  O(n)
def f_8(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, n):  # n iterations
        print("Hello World")


# Ungur Andreea
# T(n) =n * (n+n) = 2n^2 -> O(n^2)
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")

#TO-DO
def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")


"""
Analyze the time and space complexity 
"""


# Time: O(n*logn) (base of log = 3)
# Extra space complexity: O(1)
def f_11(data: list):
    data_sum = 0
    for el in data:
        j = len(data)
        while j > 1:
            data_sum += el * j
            j = j // 3
    return data_sum


#Time complexity: O(n)
#Space complexity: ? (!!slicing)
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
