"""
    Determine the time complexity of the following algorithms as a function of n.
    source: https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
"""

"""
    n - size of the program's input (can be n,m,p if multiple inputs) 

    ex:
        factorial, fibonacci -> n is a number (index in a list etc.)
        merge sort -> n is the length of a list (or another data structure)
        
    T(n) -- number of operations made by the algorithm
    
    O(n) -- upper bound (algorithm will not perform worse than this)
    Omega(n) -- low bound (algorithm will not perform better than this)
    Theta(n) -- both upper and low bounds
    
    BC(A) -- case in which the least number of operations are required
    AC(A) -- !!!???
    WC(A) -- case in which the most number of operations are required 
  
AC(A) in the case of liniar search
    - we assume search in a list of length n
    - we assume the element is in the list
    - we assume the same probability of being in any valid position (uniform probability)
    
    T(n) = (1 + 2 + .. + n) / n = n(n+1)/(2*n) = (n+1)/2 => O(n)  

complexity
    - time (number of operations taken to solve the problem)
    - space (memory, number of bytes taken to solve the problem)
"""


# T(n) = 10 * n * 1 =10 * n => O(n)
def f_1(n: int):
    for i in range(10):  # 0 .. 9 -> does not depend on n
        for j in range(n):  # 0 .. (n-1) -> n times
            print("Hello World")  # O(1) constant complexity


# T(n) = 10 * n, O(n)
def f_2(n: int):
    for i in range(n, n + 10):  # n .. n+9 -> does not depend on n
        for j in range(n):  # n times
            print("Hello World")  # O(1)


def f_3(n: int):
    for i in range(1, n):  # 1 .. (n-1)
        for j in range(i, n):  #
            print("Hello World")


"""
1 2 3 4 ... n - 1 = n - 1
  2 3 4 ... n - 1 = n - 2
    3 4 ... n - 1 = n - 3
              ...
            n - 1 = 1    

T(n) = n(n-1)/2 => O(n^2)     
"""


# T(n) = n^2, O(n^2)
def f_4(n: int):
    for i in range(n):  # n iterations
        for j in range(2 * i + 1):  # 0 .. 2 * i => n
            print("Hello World")


# T(n) = n^4, O(n^4)
def f_5(n: int):
    for i in range(n ** 2):  # 0 .. n^2 - 1
        for j in range(i):  # 0 .. n^2 - 2
            print("Hello World")


"""
0                      = 1
0 1                    = 2
0 1 2                  = 3 
...                    ...
0 1 2 ... (n^2) - 2    = n^2 - 1

T(n) = n^2 * (n^2 + 1) / 2, O(n^4)

still about f_5, O(n^4)

if n = 1000, runtime is 1 ms
if n = 3000, runtime is estimated at 81 ms 


"""


def f_run(n: int):
    val = 0
    for i in range(n ** 2):  # 0 .. n^2 - 1
        for j in range(i):  # 0 .. n^2 - 2
            val += 1
    return val


for i in range(13):
    print(i, f_run(i))


# T(n) = n * log2(n) => O(n*log2(n))
def f_6(n: int):
    for i in range(n):  # n iterations
        t = 1
        while t < n:  # log2(n) -- log base 2 of n
            print("Hello World")
            t *= 2


"""
1. Time complexity in both "n" and "m"
"""


# T(n,m) = n + m
def f_7(n, m: int):
    for i in range(0, n):  # n iterations
        print("Hello World")
    for j in range(0, m):  # m iterations
        print("Hello World")


# T(n) 2 * n, O(n)
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
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + 1, n >= 2
    
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    T(n/8) = 2 * T(n/16) + 1
    
    k is the number of times we divide the list into halves, 2^k = n
    T(n) = 2 * T(n/2) + 1 = 2 * [2 * T(n/4) + 1] + 1 = 4 * T(n/4) + 2 + 1 =
    4 * [2 * T(n/8) + 1] + 2 + 1 = 8 * T(n/8) + 4 + 2 + 1
    
    T(n)   = 16 * T(n/16) + 8 + 4 + 2 + 1
    T(2^k) = 2^k * T(1) + 2^(k-1) + 2^(k-2) + ... + 2 + 1
           = n * 1 + (n - 1)/(2-1) approx n => O(n)

extra-space complexity
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + n, n >= 2
    
    TODO -- repeat the same process as in the case of time complexity
"""


def f_12(data: list):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_12(data[:m]) + f_12(data[m:])


# data = list(range(10))
# slice = data[:5]
# slice.append(99)
#
# print(id(data))
# print(id(slice))

# data = list(range(10))
# print(id(data))
# print(id(data[:5]))
# print(id(data[5:]))
# print(id(data))

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
