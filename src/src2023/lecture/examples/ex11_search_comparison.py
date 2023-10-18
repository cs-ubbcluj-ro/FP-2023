import timeit
from texttable import Texttable

from ex08_sequential_search import search_iter
from ex09_binary_search import binary_search_iter, binary_search_rec


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
            # (list_length // 2) is at the middle of the list
            algorithm(data, list_length // 2)
            t2 = timeit.default_timer()
            table_row.append(t2 - t1)
        table.add_row(table_row)
    return table


if __name__ == "__main__":
    list_lengths = [1_000_000, 2_000_000, 4_000_000, 8_000_000, 16_000_000]
    algorithms = [search_iter, binary_search_iter, binary_search_rec]
    print(build_result_table(algorithms, list_lengths).draw())
