from pprint import pprint
from typing import List

import numpy as np
import texttable
from colorama import Fore, Style


class Item:
    def __init__(self, weight, profit):
        self._weight = weight
        self._profit = profit

    @property
    def weight(self):
        return self._weight

    @property
    def profit(self):
        return self._profit

    def __str__(self):
        return 'Item: W = {}, Profit = {}'.format(self.weight, self.profit)


def print_dp_table_nicely(dp):
    table = texttable.Texttable()
    header = ['\\'] + [str(i) for i in range(len(dp[0]))]
    table.header(header)
    for i, row in enumerate(dp):
        row_to_add = [str(i)] + row
        table.add_row(row_to_add)
    print(table.draw())


def solve_knapsack(items: List[Item], max_possible_weight: int):
    dp = [[0 for x in range(max_possible_weight + 1)] for y in range(len(items) + 1)]

    for item_number in range(1, len(items) + 1):
        current_item_weight = items[item_number - 1].weight
        current_item_profit = items[item_number - 1].profit

        for current_weight in range(1, max_possible_weight + 1):
            if current_item_weight <= current_weight:
                # If we take current item, then we need to see if we can add any profit for remaining weight
                profit_if_we_take_current_item = current_item_profit + dp[item_number - 1][
                    current_weight - current_item_weight]

                # If we don't take current item, look at what profit we can obtain with
                # the other items
                profit_if_we_dont_take_current_item = dp[item_number - 1][current_weight]

                dp[item_number][current_weight] = max(profit_if_we_take_current_item,
                                                      profit_if_we_dont_take_current_item)
            else:
                dp[item_number][current_weight] = dp[item_number - 1][current_weight]
        print(Fore.BLUE + 'After considering item', items[item_number - 1], 'table looks like:' + Style.RESET_ALL)
        print_dp_table_nicely(dp)
    return dp


# You can print intermediary tables by calling print_dp_table_nicely from solve_knapsack at
# different points (e.g. when we finish with a row) - uncomment lines
items = [Item(3, 2), Item(4, 3), Item(6, 1), Item(5, 4)]
rucksack_weight = 8
result = solve_knapsack(items, rucksack_weight)
print('Max profit', result[-1][-1])
