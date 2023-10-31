"""
    Problem Solving Methods -- Divide & Conquer and Backtracking

    How does divide and conquer work?

    Divide & Conquer
    Divide: divide problem in sub-problems which are similar to the original (disjoint sub-problems)
    Conquer: solve the smallest problems
    Combine: combine the result obtained for the smaller problems (to solve the original one)


    What D&C algorithms do we already know?

    Merge sort
    Divide: divide the list into halves
    Conquer: array of length 1 is sorted
    Combine: merge the sorted lists

    Binary search, Quick sort
"""
import math

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, 
    recursive vs non-recursive). Return None for
    an empty list

    a. [S] Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. [S] Divide in halves, recursive
"""


# Soptelea Sebastian
# Solution for 1.c. Divide in halves, recursive
def find_min(lst: list, left: int, right: int):
    if left == right:
        return lst[left]
    else:
        mid = (left + right) // 2
        min_left = find_min(lst, left, mid)
        min_right = find_min(lst, mid + 1, right)
        return min(min_left, min_right)


# Solution for 1.a. Chip and conquer, recursive
# Split the list into 1 element ("chip") + rest of the list

def find_min_chip(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min_chip(lst[1:]))


def test_find_min_halves():
    # in a test, we should strive to include a series
    # of cases that are representative of the general ones
    # i.e.
    # min somewhere in list (not start or end index)
    # min on position 0, position length(list) - 1
    # lists with even, odd number of elements
    # list with 1 element, no element (Q: is this case addressed by our program?)
    # can you think of any other cases?

    testlist = [1, 4, -5, 10, -9, 2]
    assert find_min(testlist, 0, len(testlist) - 1) == -9

    testlist = [1, 4, 10]
    assert find_min(testlist, 0, len(testlist) - 1) == 1

    testlist = [-2]
    assert find_min(testlist, 0, len(testlist) - 1) == -2

    testlist = [11, 4, 2]
    assert find_min(testlist, 0, len(testlist) - 1) == 2

    testlist = [1, 4, -5, -6, 5, 8]
    assert find_min(testlist, 0, len(testlist) - 1) == -6

    testlist = [1, 4, -5, -1, 2]
    assert find_min(testlist, 0, len(testlist) - 1) == -5

    # testlist = []
    # assert find_min(testlist, 0, len(testlist) - 1) is None


def test_find_min_chip():
    # repeat the tests for the chip and conquer implementation

    testlist = [1, 4, -5, 10, -9, 2]
    assert find_min_chip(testlist) == -9

    testlist = [1, 4, 10]
    assert find_min_chip(testlist) == 1

    testlist = [-2]
    assert find_min_chip(testlist) == -2

    testlist = [11, 4, 2]
    assert find_min_chip(testlist) == 2

    testlist = [1, 4, -5, -6, 5, 8]
    assert find_min_chip(testlist) == -6

    testlist = [1, 4, -5, -1, 2]
    assert find_min_chip(testlist) == -5

    # testlist = []
    # assert find_min_chip(testlist, 0, len(testlist) - 1) is None


# assert ... : assert something that we expect to be true
# if it works: nothing shown
# if it fails (what we expected to be true is not - the program doesn't
# return the result we expect) -> AssertionError

test_find_min_halves()
test_find_min_chip()

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
    
    
    [A] 
    
    What is exponential search?
    
"""

"""
3. Calculate the r-th root of a given number x with a given precision p

"""

"""
4. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation
    c*. Dynamic programming
    
    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
    
    
"""

"""
Divide and conquer approach
    - split list in halves, compute max subarray sum for each half
    - return max of these sums 
    
    Problem:
    
    [-2, -5, 6, -2, -3, 1, 5, -6]
    ->
    [-2, -5, 6, -2] and [-3, 1, 5, -6]
    ->
    ([-2, -5] and [6, -2]) and ([-3, 1] and [5, -6])
    ->
    ...
    
    We never check the subarray which actually has the max sum:
    [6, -2, -3, 1, 5]
    
    This is a subarray that crosses the midpoint in our split =>
    need to find a way to also take this into account
    
    Solution: compute a "crossing sum" = find the max sum 
        that can be obtained for a subarray that crosses the midpoint
        
        We can compute this by simply going from the midpoint to the left,
        finding the max sum we can gather from the left (left_sum), and repeat the process
        for the right (right_sum)
        
        The max crossing sum is then the sum of the collected left_sum and right_sum
        
    -----
    
    Return max of (left_half_max_sum, right_half_max_sum, max_crossing_sum) at each point
    
        **Note: here, left_half_max_sum, right_half_max_sum refer to the max sums obtained
            from the left and right halves (in code, leftmax and rightmax)
"""


def max_sum_dc(list: list, left: int, right: int):
    if left == right:
        return list[left]

    m = (left + right) // 2

    leftmax = max_sum_dc(list, left, m)
    rightmax = max_sum_dc(list, m + 1, right)

    crt_sum = 0
    left_sum = -math.inf
    for i in range(m, left - 1, -1):
        crt_sum += list[i]
        if crt_sum > left_sum:
            left_sum = crt_sum

    crt_sum = 0
    right_sum = -math.inf
    for i in range(m + 1, right + 1):
        crt_sum += list[i]
        if crt_sum > right_sum:
            right_sum = crt_sum

    max_crossing_sum = left_sum + right_sum
    return max(leftmax, rightmax, max_crossing_sum)


# Toma Stefan
# ...
"""
Use a more efficient way to solve the max subarray sum problem

Idea:
For a list such as:

[-2, -5, 6, -2, -3, 1, 5, -6]

go through it, and at each point compute a current_sum
as follows:
 --try adding the current element to the current_sum
 --if by adding the current element we obtain a negative number,
    then restart current_sum and continue to next element
    
    Why?
    
    If, at any point, the current sum is < 0, it means that no matter
    what we add to it in the following steps, it would generate a smaller
    sum than that of 0+following elements
    
    
--check if the current_sum is greater than the max sum obtained up until 
    that point, if yes, set max to current sum
    
E.g. 
[-2, -5, 6, -2, -3, 1, 5, -6]

Start with
    current_sum = -2
    max_sum = - 2

    Go through list
    i = 1
    current_sum = -2 + list[1] = -2 + -5 = -7 < 0
    current_sum = 0 (starting from scratch with a new subarray is more helpful than 
                       taking the current sum up until this point, -7)
    
    i = 2
    current_sum = 0 + list[2] = 0 + 6 > 0
    current_sum > max_sum => max_sum = current_sum = 6
    
    i = 3
    current_sum = 6 + list[3] = 6 + -2 = 4 
    current_sum < max_sum (but we continue with current_sum = 4 and add to it
            because adding 4 to a sum we obtain from the following elements helps us get
            a bigger sum)
    
    ...

Problem:

If we have an array such as [-5, -4, -3, -2, -1], where max_sum is -1, 
we won't get the correct result

"""


def max_sum(lst: list):
    n = len(lst)
    print(lst)
    max_sum = lst[0]
    current_sum = 0

    for i in range(n):
        # print('Current sum at position', i,' is', current_sum)
        if current_sum + lst[i] < 0:
            current_sum = 0
        else:
            current_sum = current_sum + lst[i]
            max_sum = max(current_sum, max_sum)

    return max_sum


"""
[A] Dynamic programming approach
(we'll discuss in Seminar 5):

  --for each i, compute a maximum sum until the position i
  --check if this sum is greater than the current max sum
  """


def max_sum_dp2(lst: list):
    print(lst)
    max_ending_here = lst[0]
    max_sum = lst[0]

    for i in range(1, len(lst)):
        max_ending_here = max(lst[i], max_ending_here + lst[i])
        # print('Current maximum sum, at position', i, 'is', max_ending_here)

        if max_ending_here > max_sum:
            max_sum = max_ending_here

    return max_sum


def test_max_sum_dc():
    # Test case with all positive numbers in the list
    arr1 = [1, 2, 3, 4, 5]
    assert max_sum_dc(arr1, 0, len(arr1) - 1) == 15

    # Test case with mixed positive and negative numbers
    arr2 = [-2, -5, 6, -2, -3, 1, 5, -6]
    assert max_sum_dc(arr2, 0, len(arr2) - 1) == 7

    # Test case with all negative numbers
    arr3 = [-1, -2, -3, -4, -5]
    assert max_sum_dc(arr3, 0, len(arr3) - 1) == -1

    # # Test case 4: Empty list
    # arr4 = []
    # assert max_sum_dc(arr4,  0, len(arr4) - 1) == 0

    # Test case with a list with 1 element
    arr5 = [7]
    assert max_sum_dc(arr5, 0, len(arr5) - 1) == 7

    # Test case with a large negative number in the middle
    arr6 = [1, 2, -10, 3, 4]
    assert max_sum_dc(arr6, 0, len(arr6) - 1) == 7


def test_max_sum():
    # Test case with all positive numbers in the list
    arr1 = [1, 2, 3, 4, 5]
    assert max_sum(arr1) == 15

    # Test case with mixed positive and negative numbers
    arr2 = [-2, -5, 6, -2, -3, 1, 5, -6]
    assert max_sum(arr2) == 7

    arr9 = [-1, 4]
    assert (max_sum(arr9) == 4)

    # Test case with all negative numbers
    arr3 = [-1, -2, -3, -4, -5]
    assert max_sum(arr3) == -1

    # arr8 = [-5, -4, -3, -2, -1]
    # assert max_sum_dp1(arr8) ==-1

    # Test case with all negative numbers
    arr7 = [2, -2, -3, -4, -5]
    assert max_sum(arr7) == 2

    # # Test case 4: Empty list
    # arr4 = []
    # assert max_sum_dc(arr4,  0, len(arr4) - 1) == 0

    # Test case with a list with 1 element
    arr5 = [7]
    assert max_sum(arr5) == 7

    # Test case with a large negative number in the middle
    arr6 = [1, 2, -10, 3, 4]
    assert max_sum(arr6) == 7


def test_max_sum_dp():
    # Test case with all positive numbers in the list
    arr1 = [1, 2, 3, 4, 5]
    assert max_sum_dp2(arr1) == 15

    # Test case with mixed positive and negative numbers
    arr2 = [-2, -5, 6, -2, -3, 1, 5, -6]
    assert max_sum_dp2(arr2) == 7

    # Test case with all negative numbers
    arr3 = [-1, -2, -3, -4, -5]
    assert max_sum_dp2(arr3) == -1

    # # Test case 4: Empty list
    # arr4 = []
    # assert max_sum_dc(arr4,  0, len(arr4) - 1) == 0

    # Test case with a list with 1 element
    arr5 = [7]
    assert max_sum_dp2(arr5) == 7

    # Test case with a large negative number in the middle
    arr6 = [1, 2, -10, 3, 4]
    assert max_sum_dp2(arr6) == 7

    arr8 = [-5, -4, -3, -2, -1]
    assert max_sum_dp2(arr8) == -1


test_max_sum_dc()
test_max_sum()
test_max_sum_dp()

"""
    Backtracking
    
    For backtracking, we need to:
    
        - figure out how to represent the candidate solution(s)  
            e.g. for permutations of n, we take a list of size n, each element in list can take values from 0,.., n-1 (or 1,..,n)
                 X = [x0, x2, .., xn-1] where xi takes values from {0,1,2,..,n-1}
        - determine what a consistent solution looks like
            - a candidate solution Xc = [x0,..,xk] is consistent if we can extend it so that we obtain a solution to the problem
            - e.g. the partial solution [0] is consistent in terms of permutations (no duplicates) -> can build further to obtain solution
                                        [0, 1, 2] is consistent in terms of permutations (no duplicates) -> can build further to obtain solution
                                        [0, 1, 1] is not consistent -> cannot extend it to obtain valid permutation
        - determine when we found a solution:
                e.g. when we have candidate solution Xc = [x0,..,xk] consistent and k=n-1 

    Formally, for permutations:
    
    Candidate solution: X = [x0, x1,. .. , xk] , xi ∈ {0,1,..,N− 1}
    Consistent function: X = [x0, x1,. .. , xk] is consistent if  xi ≠ xj for ∀ i ≠ j
    Solution function: X = [x0, x1,. .. , xk] is a solution if is consistent and k= n − 1
    
    
"""

"""
5. Recursive implementation for permutations
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """

    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, 2):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
6. Change the code for generating the permutation above to work for the n-Queen 
   problem
   
   n-Queen problem: nxn board, place n queens in such a way that they don't attack each other
                    attack = they are on same line, column or diagonal
    
   How to represent the candidate solution?
   
   Board: 
   
   n=8
   
   L_0: - - - - - Q - -
   L_1: - - - - - - - Q
   L_2: - - - - - - Q - 
   L_3: - - - - Q - - -
   L_4: - Q - - - - - -    
   L_5: Q - - - - - - - 
   L_6: - - Q - - - - - 
   l_7: - - - Q - - - -
   
   Candidate solution: X = [5, 7, 6, 4, 1, 0, 2, 3] 
        -at index 0 we store the column for the queen on line L_index
   Consistency:
        -queens don't attack each other
            -check that we don't have two queens on the same line: taken care of by the representation
            -check that we don't have two queens on the same column: no duplicate values in candidate solutions
            -check that we don't have queens on a diagonal: for two queens, the difference between their respective 
                    line indices should not be the same as the difference between their column indices
   Solution:
        -we have placed all n queens on the board (and the full solution is consistent)        
    
    
    Formally:
    
    Candidate solution: X = [x0, x1,. .. , xk] , xi ∈ (0,1,. .,n-1)
                        (i , xi) ∀ i ∈ (0,1,. . ,k) is position of a queen on the board
    Consistency function:
        X = [x0, x1,. .. , xk] consistent if queens do not attack each other
        xi ≠ xj for ∀ i ≠ j (no two queens on same column)
        ∣i − j∣ ≠ ∣xi − xj∣ ∀ i≠ j (diagonal check)
    
    Solution function:
        X = [x0, x1,. .. , xk] is solution if consistent and k = n-1
    
"""

"""
7. Generate all the N x N Latin squares for a given number N.

Latin square: n × n array filled with n different symbols, each occurring exactly 
        once in each row and exactly once in each column

        A	B	C
        C	A	B
        B	C	A

Repeat the same process as for the previous two problems:
    --figure out how to represent solution
    --what the consistency function should check
    --what the solution function should look like & then customize the provided backtracking template

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
