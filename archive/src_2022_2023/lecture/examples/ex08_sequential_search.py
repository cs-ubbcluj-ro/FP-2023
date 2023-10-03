"""
Examples for sequential searching
"""
import random
import timeit
from texttable import Texttable


def search_iter(data: list, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1


def search_rec(data: list, key, pos: int = 0):
    if 0 > pos or pos >= len(data):
        return -1
    if data[pos] == key:
        return key
    return search_rec(key, data, pos + 1)


def generate_list(length: int):
    """
    Generate a list of given length with elements [0, ... , n-1]
    :return: The newly generated list
    """
    return list(range(length))


'''
    NB!
    To run the function below, you must have installed the texttable component from:
    https://github.com/foutaise/texttable
'''


def build_result_table(algorithms: list, list_lengths: list):
    table = Texttable()
    table.add_row(['algorithm'] + list_lengths)

    for algorithm in algorithms:
        table_row = [algorithm.__name__]
        for list_length in list_lengths:
            data = generate_list(list_length)
            t1 = timeit.default_timer()
            # -1 is not in the list, so worst case complexity
            algorithm(data, -1)
            t2 = timeit.default_timer()
            table_row.append(t2 - t1)
        table.add_row(table_row)
    return table


if __name__ == "__main__":
    list_lengths = [1_000_000, 2_000_000, 4_000_000, 8_000_000, 16_000_000]
    # Adding search_rec here will crash with recursion depth exceeded error
    # TODO How do we add the binary search implementations here?
    algorithms = [search_iter]
    print(build_result_table(algorithms, list_lengths).draw())
