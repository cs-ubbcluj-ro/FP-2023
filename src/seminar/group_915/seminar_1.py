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


oh_my_word = input("Word to count vowels for: ")
print("There are " + str(count_vowles(oh_my_word)) + " in word " + oh_my_word)
