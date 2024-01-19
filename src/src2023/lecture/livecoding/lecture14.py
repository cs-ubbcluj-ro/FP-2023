"""
       Compute the sum of even elements in the given list
       input:
           l - the list of numbers
       output:
           The sum of the even elements in the list

       Raises TypeError if parameter l is not a Python list
       Raises ValueError if the list does not contain even numbers
"""

"""
D & C
    - Divide
    - Conquer
    - Combine
    
    variants:
        1. divide problem space into halves
        2. chip & conquer (divide into 1, n-1)
        2. divide problem space into halves -> iteratively

n - input size of the algorithm
T(n) - number of operations carried out

T(n) = 4*T(n/2) + 1, n > 1
     = 1, n <= 1

"""


# https://refactoring.guru/design-patterns/iterator
class DataIter:
    def __init__(self, data: list):
        self.__data = data
        self.__poz = -1

    def __next__(self):
        self.__poz += 1
        if len(self.__data) <= self.__poz:
            raise StopIteration()
        return self.__data[self.__poz]


class MyDataStructure:
    def __init__(self):
        self.__data = []

    def add(self, e):
        self.__data.append(e)

    def __iter__(self):
        return DataIter(self.__data)
