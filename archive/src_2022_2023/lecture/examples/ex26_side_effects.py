"""
Created on Sep 29, 2016

@author: http://www.python-course.eu/passing_arguments.php
"""

"""
    Example for function side effects. Run the code below calling each of
    the functions in turn. Examine the result
"""


def no_side_effect(lst):
    print(2, id(lst), lst)
    lst = [0, 1, 2, 3]
    print(3, id(lst), lst)


def side_effect(lst):
    print(5, id(lst), lst)
    lst.append(999)
    print(6, id(lst), lst)


my_list = [0, 1, 2]
print(1, id(my_list), my_list)
no_side_effect(my_list)
print(4, id(my_list), my_list)
side_effect(my_list)
print(7, id(my_list), my_list)
