"""
Created on Dec 20, 2016

@author: Arthur
"""
from random import *
from datetime import *
from texttable import *

from ex11_insertion_sort import insertion_sort, binary_insertion_sort
from ex12_merge_sort import merge_sort
from ex13_tim_sort import tim_sort_rpython
from ex14_tim_sort import tim_sort_vladris
from ex15_quick_sort import quick_sort_but_slow, quick_sort


def already_sorted_data(data_size):
    result = list(range(0, data_size))
    return result


def sorted_in_reverse_data(data_size):
    result = list(range(data_size, 0, -1))
    return result


def random_data(data_size):
    result = list(range(0, data_size))
    shuffle(result)
    return result


def test_sorts():
    array = list(range(100, 0, -1))
    insertion_sort(array)
    assert array == list(range(1, 101))

    array.reverse()
    array = binary_insertion_sort(array)
    assert array == list(range(1, 101))

    array.reverse()
    merge_sort(array)
    assert array == list(range(1, 101))

    array.reverse()
    quick_sort_but_slow(array)
    assert array == list(range(1, 101))

    array.reverse()
    tim_sort_rpython(array)
    assert array == list(range(1, 101))

    array.reverse()
    tim_sort_vladris(array)
    assert array == list(range(1, 101))


test_sorts()

'''
    Utility function to convert a timedelta into a number of milliseconds
'''


def millis_interval(start, end):
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return int(millis)


'''
    And here we build our experiment

        data_generators - Change the functions that build the data set to be sorted
        sort_functions  - What functions will do the actual sort
        data_sizes      - What are the data sizes to be sorted
'''


def sort_test():
    """
    Generator functions for best case, average case and worst case
    """
    data_generators = [already_sorted_data, random_data, sorted_in_reverse_data]

    '''
    Sorting functions to employ
    '''
    sort_functions = [insertion_sort, binary_insertion_sort, merge_sort, quick_sort_but_slow, quick_sort,
                      tim_sort_rpython, tim_sort_vladris, sorted]

    '''
    Data sizes that will be sorted
    '''
    data_sizes = [64, 128, 256, 512, 1024, 2048, 4096, 8192]

    '''
    Do the sort and build the result table dynamically
    '''
    for generator in data_generators:
        print("Current data: " + generator.__name__)
        t = Texttable()
        t.add_row(['Functions/size'] + data_sizes)
        for sort_function in sort_functions:
            row = [sort_function.__name__]
            for size in data_sizes:
                data = generator(size)
                t1 = datetime.now()
                sort_function(data)
                t2 = datetime.now()
                row = row + [millis_interval(t1, t2)]
            t.add_row(row)
        print(t.draw())


sort_test()
