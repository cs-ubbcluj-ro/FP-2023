"""
Created on Jan 11, 2017

@author: Arthur
"""


def longest_increasing_subsequence(A):
    """
    Maximum length of subsequence recorded so far, as well as its end index
    """
    max_length = 1
    best_end = 0

    indices_array = [1]
    previous_indices = [-1]

    for i in range(1, len(A)):
        '''
        The maximum length of the increasing subsequence ending at index i
        '''
        indices_array.append(1)
        previous_indices.append(-1)

        '''
        The maximum length is increased by 1 if 'j' exists, so that:
            A[j] < A[i] and the length of the subsequence would increase
        '''
        for j in range(i - 1, -1, -1):
            if (indices_array[j] + 1 > indices_array[i]) and (A[j] < A[i]):
                indices_array[i] = indices_array[j] + 1
                previous_indices[i] = j

        '''
        Record the end index in the same go
        '''
        if indices_array[i] > max_length:
            best_end = i
            max_length = indices_array[i]

    '''
    Build the solution using the previous_indices list
    '''
    solution = [A[best_end]]
    while previous_indices[best_end] != -1:
        solution.append(A[previous_indices[best_end]])
        best_end = previous_indices[best_end]

    solution.reverse()
    return solution


A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(A))
