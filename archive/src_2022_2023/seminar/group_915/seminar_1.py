"""
FP seminar 1 problems & solutions
"""

"""
Problem statements to choose from:
    https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
"""

"""
Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, 
only a, e, i, o, and u will be counted as vowels — not y.
"""


def count_vowles(word):
    count = 0
    vowels = "aeiou"

    for char in word:
        if char in vowels:
            count += 1

    return count


# oh_my_word = input("Word to count vowels for: ")
# print("There are " + str(count_vowles(oh_my_word)) + " in word " + oh_my_word)

"""
Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, 
the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits 
long.
"""


def convert_base_2(number):
    """
    Convert given number to base 2
    :param number: Number to convert
    :return: List of the number's digits in base 2 representation (e.g., 6 -> [1, 1, 0])
    """
    digit_list = []

    while number != 0:
        # digit_list.append(number % 2)
        digit_list.insert(0, number % 2)
        number //= 2  # <=> number = number // 2
    return digit_list


# my_number = int(input("Enter the number to convert to base 2"))
# digit_list = convert_base_2(my_number)
#
# as_string = ""
# for el in digit_list:
#     as_string += str(el)
#
# print("Value " + str(my_number) + " in base 2: " + as_string)

"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2
substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the
same place in both strings.
    stringMatch('xxcaazz', 'xxbaaz') → 3
    stringMatch('abc','abc) → 2
        stringMatch('abc', 'axc') → 0
"""


def string_match(str_one, str_two):
    count = 0
    for i in range(0, min(len(str_one), len(str_two)) - 1):  # range(0,5) -> 0, 1, 2, 3, 4
        # Python iterables (strings, lists) can be indexed and sliced
        if str_one[i:i + 2] == str_two[i:i + 2]:
            count += 1
    return count


print(string_match("xxcaazzabcdefg", "xxbaaz"))
