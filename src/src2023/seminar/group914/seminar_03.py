"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
Computational complexity recap
    n -> size of the program's input
        factorial (n!) -> number we calculate factorial for
        fibonacci -> index of the term we want to compute
        merge sort -> length of the list we want to sort
        
    BC(n) -> how is input data organized (e.g., list already sorted)
    AC(n)
    WC(n) -> how is input data organized (e.g., list sorted in reverse)
         
    O(n) -> upper bound 
        if T(n) in O(n*log(n)) => T(n) in O(n^2), O(n^3), O(n^4)
    Omega(n) -> lower bound
    Theta(n) -> upper && lower bound
"""

"""
AC(n) for liniar search
1. find elem on pos 0 -> 1
2. find elem on pos 1 -> 2
....
n. find elem on pos n-1 -> n

assume P(I) is uniform distribution

T(n) = (1 + 2 + ... + n) / n = n(n-1) / (2 * n) in T(n)
"""


# T(n) = 10 * n in O(n)
def f_1(n: int):  # n represents size of the program's input
    for i in range(10):  # between 0 .. 9 -> 10 loops
        for j in range(n):  # n times
            print("Hello World")


# T(n) = 10 * n in O(n)
def f_2(n: int):
    for i in range(n, n + 10):  # 10 times ! does not depend on n !
        for j in range(n):  # n times
            print("Hello World")


# T(n) = n * n => O(n^2)
def f_3(n: int):
    for i in range(1, n):  # n - 1
        for j in range(i, n):  # n - i + 1
            print("Hello World")


# T(n) in O(n^2)
def f_4(n: int):
    for i in range(n):  # n
        for j in range(2 * i + 1):  # 1 .. (2n - 1)
            print("Hello World")


# T(n) = n^2 * n^2, so O(n^4)
# for n = 1000, function takes 1 ms to complete
# for n = 3000, we expect runtime of 81 ms
def f_5(n: int):
    for i in range(n ** 2):  # n^2
        for j in range(i):  # n^ 2
            print("Hello World")


# T(n) = n * log(n)
def f_6(n: int):
    for i in range(n):  # n
        t = 1
        while t < n:
            print("Hello World")
            t *= 2  # how many times do we multiply t => log(n)


"""
1. Time complexity in both "n" and "m"
"""


# T(n, m) = n + m, O(n + m)
def f_7(n, m: int):
    for i in range(0, n):  # n loops
        print("Hello World")
    for j in range(0, m):  # m loops
        print("Hello World")


# m does not contribute to complexity
# T(n) = 2n, O(n)
def f_8(n, m: int):
    for i in range(0, n):  # n
        print("Hello World")
    for j in range(0, n):  # n
        print("Hello World")


# T(n) = n * ( n + n ) = 2n^2 => O(n^2)
def f_9(n: int):
    for i in range(n):  # n loops
        for j in range(n):  # n loops
            print("Hello World")
        for k in range(n):  # n loops
            print("Hello World")


# T(n) is O(n^2)
def f_10(n: int):
    for i in range(n):  # n
        for j in range(n, i, -1):  # n .. (i + 1) => n
            print("Hello World")


"""
Analyze the time and space complexity 
"""

"""
time complexity T(n) = n * log3(n) => O(n * log(n))

extra-space complexity
    n - size of the program's input
    how much additional memory is required by the program?
        => we allocate the same 4 vars, regardless of len(data) 
    T(n) = 1, O(1)
"""


def f_11(data: list):  # len(data) = n
    data_sum = 0
    for el in data:  # n loops
        j = len(data)
        while j > 1:  # log base 3 of n
            data_sum += el * j
            j = j // 3
    return data_sum


"""
time complexity
    T(1) = 1
    T(n) = 2 * T(n/2) + 1
    
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    ...
    
    T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 =
    = 4 * [2 * T(n/8) + 1] + 2 + 1=
    = 8 * T(n/8) + 4 + 2 + 1 
    = 16 * T(n/16) + 8 + 4 + 2 + 1
    
    # let's take k, so that n = 2^k
    # T(2^k) = 2^k * T(1) + 2^(k-1) + 2^(k-2) + ... + 2 + 1
    # T(2^k) = 2^k + (2^k - 1)/(2 - 1) = 2n => O(n)
    
extra-space complexity
T(n) = 2 * T(n/2) + 2 * n/2
     = 2 * T(n/2) + n
     
     just like above, but all terms get multiplied by n => O(n^2)
"""


def f_12(data: list):  # n = len(data)
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


"""
    we need to look at n to determine complexity
    
    T(n) = 1, n < 2
    T(n) = 4 * T(n/2) + 1
    T(n/2) = 4 * T(n/4) + 1
    T(n/4) = 4 * T(n/8) + 1
    ...
    at after k iterations we get to T(1), 2^k = n
    T(n) = 4 * T(n/2) + 1 = 4 * [4 * T(n/4) + 1] + 1 =
    = 16 * T(n/4) + 4 + 1 = 16 * [4 * T(n/8) + 1] + 4 + 1 =
    = 4^3 * T(n/8) + 4^2 + 4^1 + 1
    
    T(2^k) = 2^(2k) * T(1) + (4^(k-1) - 1) / (4 - 1)
    T(2^k) = n^2 + n^2/6 => O(n^2) 
    
    
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


def f_15_better(data: list) -> int:
    cache = {}  # dict() - constructor for class dict
    max_elem = data[0]
    max_freq = 1
    cache[data[0]] = 1
    for el in data:
        if el in cache:
            # if el in dictionary we increase the number of times we've seen
            # it by 1
            cache[el] += 1
            if cache[el] > max_freq:
                max_freq = cache[el]
                max_elem = el
        else:
            # if not in cache then add it with 1 appearance
            cache[el] = 1
            # if cache[el] > max_freq:
            #     max_freq = cache[el]
            #     max_elem = el
    return max_elem


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


"""
slicing in Python 
    works for Sequece types -- str, list
"""
# list() is a sequence type
data = list(range(0, 10))
# str is also a sequence type
data = "abcdefghijkl"

print(data[2:4])  # '23' -> index 2 is included, index 4 is excluded
print(data[2:])  # until the end of the list
print(data[:4])  # from the beginning
print(data[:-1])
print(data[:5:3])
