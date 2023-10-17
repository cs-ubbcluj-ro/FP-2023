"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
    n - program's input size (relevant to calculate complexity)
    ex.
    factorial, fibonacci -> index of number to factor, or term in Fib sequence
    quick sort -> n is the size of the list
    
    T(n) - number of operations made by the program for input size n
    
    computational complexity bounds
        O(n) -> high bound ( O(n^2) is also O(n^3) and O(n^4) and so on)
        Omega(n) -> low bound ( Omega(n^2) is also Omega(n^log(n)) and Omega(n) and so on)
        Theta(n) means both low and high bounds    
        
    BC(n) - best case, algorithm makes fewest operations possible
    AC(n) - average case !!!???
    WC(n) - worst case, algorithm makes the maximum number of operations possible

    AC(n) example - liniar search, we know the element is in the list
    we assume uniform probability ditribution => it means that the element we are 
    searching for have the same probability of being at each of the list's indices
    
    T(n) = (1 + 2 + 3 + ... + n) / n = (n + 1) / 2 => O(n) 

"""


# T(n) = 10 * n * 1 => O(n)
def f_1(n: int):
    for i in range(10):  # 0 .. 9  -> does not depend on n
        for j in range(n):  # 0 .. (n - 1)
            print("Hello World")  # O(1) - runs in constant time


# T(n) = 10 * n * 1 => O(n)
def f_2(n: int):
    for i in range(n, n + 10):  # n .. (n + 9) -> does not depend on n
        for j in range(n):  # n
            print("Hello World")  # constant time


# T(n) = n * n * 1 => O(n^2)
def f_3(n: int):
    for i in range(1, n):  # 1 .. (n - 1)
        for j in range(i, n):  # i .. (n - 1)
            print("Hello World")  # O(1)


"""
f3
1 2 3 ... n - 1
  2 3 ... n - 1
    3 ... n - 1
            ...
          n - 1
"""


# T(n) = n * 2n * 1 => O(n^2)
def f_4(n: int):
    for i in range(n):  # 0 .. (n - 1)
        for j in range(2 * i + 1):  # 0 .. (2n - 1) -- [2 * (n-1)] + 1 = 2n - 1
            print("Hello World")  # O(1)


# T(n) = n^2 * n^2 * 1 => O(n^4)
"""
for f5
for n = 1000, f5 takes 1 ms to complete
for n = 3000, how long does ti take?
it's (3000 / 1000)^ 4 ms => 81 ms
"""


def f_5(n: int):
    for i in range(n ** 2):  # 0 .. n^2
        for j in range(i):  # 0 .. n^2
            print("Hello World")  # O(1)


# T(n) = n * log2(n)
def f_6(n: int):
    for i in range(n):  # n iterations
        t = 1
        while t < n:  # log2(n) -- log base 2 of n
            print("Hello World")
            t *= 2


"""
def f_6(n: int):
    for i in range(n):  # n iterations
        t = 1
        while t < i:  # log2(n) -- log base 2 of n
            print("Hello World")
            t *= 2
            
T(n) = log2(1) + log2(2) + ... + log2(n-1)
T(n) = log2( (n-1)! ) we don't know how much this is but we can approx high bound
by replacing all terms with (n-1)
T(n) = log2( (n-1)^(n-1) ) = (n-1) * log2(n-1)
"""

"""
1. Time complexity in both "n" and "m"
"""


# T(n,m) = n + m, so O(n + m) (still liniar complexity)
def f_7(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, m):  # m iterations
        print("Hello World")


# T(n) = n + n, O(n)
def f_8(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, n):  # n iterations
        print("Hello World")


def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# T(n) = n *
def f_10(n: int):
    for i in range(n):  # n iterations
        for j in range(n, i, -1):  # n .. (i+1) => n - i
            print("Hello World")  # O(1)


"""
n n-1 n-2 ... 3 2 1 - n - 1
n n-1 n-2 ... 3 2   - n - 2
n n-1 n-2 ... 3     - n - 3
...
n                   - 1

T(n) = n* n(n-1) / (2*n) => O(n^2)
"""

# data = list(range(10))
# print(len(data))

"""
Analyze the time and space complexity 
"""

"""
time complexity
    T(n) = n * log3(n)
    
extra space complexity
    T(n) = 1 => O(1) extra space complexity
"""


def f_11(data: list):  # n = len(data)
    data_sum = 0
    for el in data:  # n iterations
        j = len(data)
        while j > 1:  # log3(n) -- we divide j by 3 at each step
            data_sum += el * j
            j = j // 3  # integer division
    return data_sum


"""
time complexity
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + 1
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    ... we get to T(1) on the right hand side
    
    a number k exists so that 2^k = n ( or k = log2(n) )
    T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 =
    4 * [2 * T(n/8) + 1] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1

    T(n)   = 16 * T(n/16) + 8 + 4 + 2 + 1
    T(2^k) =   k * T(1) + 2^(k-1) + 2^(k-2) + ... + 2 + 1
      T(n) = log2(n) * 1 + (n - 1)/(2-1) => O(n)  

extra space complexity
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + n
    repeat the calculations at the previous step
    T(n) = n^2 => O(n^2) 
    
"""


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])  # assume list allocation is O(1)


# sequence types are list and str
# data = list(range(10))
# data = "abcdefghijk"
# print(data)
# print(data[2:4])
# print(data[:4])
# print(data[2:])
# print(data[2:-1])
# print(data[2:-2])
# print(data[2:-2:2])


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
# TODO
    - use a dict() in order to store elements and the number of their appearances
    - iterate the list
        - new element -> add to dict with number of appearances 1
        - we've already seen this element -> increase number of appearances by 1
    - return the element with highest no of appearances
"""

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
