"""
Created on Oct 21, 2018

@author: Arthur
"""

# FIXME Import statements should be at the top

'''
    Switch the order of the import statements below. What happens?
'''
# import src.lecture.examples.ex28_modules.rational.rational_dict as rational
# import src.lecture.examples.ex28_modules.rational.rational_list as rational
# print(rational.create_rational(1,3))

'''
    Code below works by directly referencing the create_rational function 
'''
from src.lecture.examples.ex28_modules.rational import rational_dict
from src.lecture.examples.ex28_modules.rational import rational_list

print('Rational number as dict')
print(rational_dict.create_rational(1, 3))
print('Rational number as list')
print(rational_list.create_rational(1, 3))

"""
    Switch the commented line below and check what happens
"""
from src.lecture.examples.ex28_modules.rational.rational_dict import create_rational, get_numerator, get_denominator


# from src.lecture.examples.ex28_modules.rational.rational_list import create_rational, get_numerator, get_denominator


def add(q1, q2):
    """
    Function to add rational numbers that works with both list and dict representations
    :param q1:
    :param q2:
    :return:
    """
    return create_rational(get_numerator(q1) * get_denominator(q2) + get_numerator(q2) * get_denominator(q1),
                           get_denominator(q1) * get_denominator(q2))


q1 = create_rational(1, 2)
q2 = create_rational(3, 4)
print(add(q1, q2))

"""
    Let's see what the dir(...) and help(...) functions do
    Switch between the commented lines and check the output 
"""
print('-' * 50)
print(dir(rational_dict))
print('-' * 50)
print(help(rational_dict))

# print('-' * 50)
# print(dir(rational_list))
# print('-' * 50)
# print(help(rational_list))
