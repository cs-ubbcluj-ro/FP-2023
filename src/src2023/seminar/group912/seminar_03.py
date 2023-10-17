"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""
from random import randint

"""
    n - size of the program's input data
        factorial, fibonacci      -> n is the term's index
        merge sort, binary search -> n is the length of the list

    T(n) - the number of operations the program makes for input size n
    
    what T(n) measures is resource consumption
        -> memory taken up by the algorithm (extra-space complexity)
        -> time required to complete (time complexity)
        
    how do we express classes of complexity?
        O(n) -> high bound ( O(n^2) is also O(n^3), O(n^4) ...)
        Omega(n) -> low bound ( O(n^2) is also O(n), O(log(n)) ...)
        Theta(n) both low and high bounds
    
    what about the structure of the input data
        BC(A) - minimal resources for input size "n"
        AC(A) - !!!???!!!
        WC(A) - most resources for input size "n"

    ex. liniar search in a list 
        - element is in the list
        - probability is equal for all positions in the list

        AC(A):
            T(n) = (1 + 2 + 3 + ... + n)/n = n(n+1)/(2n) = (n + 1) / 2
            T(n) is O(n)
"""


# T(n) = 10 * n * 1 = 10n => O(n)
def f_1(n: int):
    for i in range(10):  # 10 iterations -> does not depend on n
        for j in range(n):  # 0 .. n - 1 => n iterations of the loop
            print("Hello World")  # 1


# T(n) = 10*n => O(n)
def f_2(n: int):
    for i in range(n, n + 10):  # 10 iterations -> does not depend on n
        for j in range(n):  # 0 .. (n - 1)
            print("Hello World")


# T(n) = n(n-1)/2 => O(n^2)
def f_3(n: int):
    for i in range(1, n):  # n - 1 iterations
        for j in range(i, n):  # i .. n - 1
            print("Hello World")


"""
explanation (each number is an iteration of the inner loop)
1 2 3 ... n-2 n-1 -> n-1
  2 3 ... n-2 n-1 -> n-2
    3 ... n-2 n-1 -> n-3
              ...
              n-1 -> 1
"""


# T(n) = n^2
def f_4(n: int):
    for i in range(n):  # n
        for j in range(2 * i + 1):  # 0 .. 2n - 1
            print("Hello World")


# T(n) = n^4 => O(n^4)
def f_5(n: int):
    for i in range(n ** 2):  # 0 .. n^2 - 1
        for j in range(i):  # 0 .. n^2 - 2
            print("Hello World")


"""
for f5
    if n = 1000, the runtime is 1s
    if n = 3000, the runtime is ??

    between 1000 and 3000 we triple the size of the input, but complexity
    is O(n^4) so runtime increases by 3^4 => approx. 81s.
"""


# T(n) = n * log2(n)
def f_6(n: int):
    for i in range(n):  # 0 .. n -> n iterations
        t = 1
        while t < n:  # log2(n) -- log base 2 of n
            print("Hello World")
            t *= 2  # we multiply by 2, so that's the base of the log


"""
def f_6(n: int):
    for i in range(n): 
        t = 1
        while t < i: 
            print("Hello World")
            t *= 2
            
T(n) = log2(1) + log2(2) + log2(3) + ... + log2(n-1)    
T(n) = log2( (n-1)! ) -- we could approximate by replacing all indices with n
"""

"""
1. Time complexity in both "n" and "m"
"""


# T(n, m) = n + m, so O(n + m)
def f_7(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, m):  # m iterations
        print("Hello World")


# O(n)
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


"""
time complexity
    n = len(data)
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + 1, n >=2 --> assume [:] is constant time
    
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    T(n/8) = 2 * T(n/16) + 1
    
    at one point, the term T(n/...) becomes T(1)
    a value k exists, so that we reach the base case after k divisions
    in that case, 2^k = n
    
    T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 
    4 * T(n/4) + 2 + 1 = 4 * [2 * T(n/8) + 1] + 2 + 1 = 
    8 * T(n/8) + 4 + 2 + 1 = 16 * T(n/16) + 8 + 4 + 2 + 1 
    
    T(n) = 16 * T(n/16) + 8 + 4 + 2 + 1, we know 2^k = n
    T(n) =  2^k * T(1) + 2^(k-1) + 2^(k-2) + ... + 2 + 1
    T(n) = n + [(2^k - 1) / (2 - 1)] = n + n/2 => O(n)

extra-space complexity
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + n, n >=2
    -- repeat the process above for this recurrence -- 
"""


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])


def f_13(n: int):
    s = 0
    for i in range(1, n ** 2):  # n^2 - 1 iterations
        j = i  # i depends on n, so j itself depends on the value of n
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10  # log10(i) divisions
    return s


"""
f_13

T(n) = log10(1) + log10(2) + log10(3) + ... + log10(n^2-1)
T(n) = log10( (n^2-1)! ) 
    what if we replace all log terms with n^2?
    
T(n) = (n^2 - 1) * log10(n^2) = 2 * n^2 & log10(n) - 2 * log10(n)
    -- take the term with the fastest growth
    -- ignore constant multiplicative factors (2 * ...)
    => O(n^2 * log10(n))
"""

"""
time complexity

    T(n) = 1, n < 2 
    T(n) = 4 * T(n/2) + 1, n >= 2
    
    T(n) = 4 * T(n/2) + 1
    T(n/2) = 4 * T(n/4) + 1
    T(n/4) = 4 * T(n/8) + 1
    T(n/8) = 4 * T(n/16) + 1

    T(n) = 4 * T(n/2) + 1 = 4 * [4 * T(n/4) + 1] + 1 = 16 * T(n/4) + 4 + 1
    = 16 * [4 * T(n/8) + 1] + 4 + 1 = 64 * T(n/8) + 16 + 4 + 1
    
    T(n) = 64 * T(n/8) + 16 + 4 + 1
    -- 2^k = n, we did n iterations --

    T(n) = 4^k * T(1) + 4^(k-1) + 4^(k-2) + ... + 4 + 1
    T(n) = n^2 + (4^k - 1)/3 = n^2 + n^2/3 => O(n^2)
"""


def f_14(n, i: int):
    if n > 1:
        i *= 2
        m = n // 2
        f_14(m, i - 2)  # m takes the place of n in the recursive calls
        f_14(m, i - 1)
        f_14(m, i + 2)
        f_14(m, i + 1)
    else:
        print(i)


"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""


# O(n^2)
# returns the number of appearances of the most frequent element in the list
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


def f_15_better(data: list):
    cache = {}
    max_so_far = 1

    for el in data:
        # looping through the list is O(n)
        if el in cache:
            # el in cache should be O(1) -- Data Structures course
            # if element is in the dict increase its occurence freq. by 1
            cache[el] += 1
            max_so_far = max(max_so_far, cache[el])
        else:
            # we see this element for the first time
            cache[el] = 1
            # max_so_far = max(max_so_far, cache[el])

    # return max(cache.values())  # liniar depending on the number of
    # unique elements in the data list

    return max_so_far


def test_f_15():
    for index in range(1000):
        # generate one random list
        data = []
        for i in range(randint(1, 20)):
            data.append(randint(1, 5))

        print(data)
        # assert raises AssertionError if the condition is False
        # no effect if condition is True
        assert f_15(data) == f_15_better(data)

    assert f_15([]) == f_15_better([]), (f_15([]), f_15_better([]))


# test_f_15()

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
