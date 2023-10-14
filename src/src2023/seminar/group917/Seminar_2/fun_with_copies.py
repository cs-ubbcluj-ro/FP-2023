import copy


def copy_list(lst):
    lst_copy = []
    for element in lst:
        # assume element is of type list,
        # e.g. we represented task as list
        new_element = []
        for el2 in element:
            new_element.append(el2)
        lst_copy.append(new_element)
    return lst_copy


def sort_list(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True


list_of_numbers = [2, 10, 1, 8]
# print(id(list_of_numbers))
# my_list2 = list_of_numbers
# print(id(my_list2))
# my_list2.sort()
# print(list_of_numbers)

# list_copy = list_of_numbers[:]
# print(id(list_copy) != id(list_of_numbers))
# sort_list(list_copy)
# print(list_copy)
# print(list_of_numbers)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst_copy_assignment = lst
lst_copy_slicing = lst[:]
lst_copy_copyfn = lst.copy()
lst_copy_deepcopy = copy.deepcopy(lst)
lst_copy_ourfn = copy_list(lst)

print('Do copies made with assignment have different ids?', id(lst_copy_assignment) != id(lst))
print('Do copies made with [:] have different ids?', id(lst_copy_slicing) != id(lst))
print('Do copies made with .copy() have different ids?', id(lst_copy_copyfn) != id(lst))
print('Do copies made with copy.deepcopy() have different ids?', id(lst_copy_deepcopy) != id(lst))
print('Do copies made with our own copy_list function have different ids?',
      id(lst_copy_ourfn) != id(lst))

# All but the first "copy" has a different id (remember what happens on assignment)
# All other 4 methods create new list
# But do we have different objects inside the list?
# What if I do
# lst_copyX[0][2] = 'Change'
# print(lst)
# What will it print? Will the original list get changed? In which of the cases?

first_element_original_lst = lst[0]
print('Does the copy made with assignment hold different objects than those in original list?',
      id(first_element_original_lst) != id(lst_copy_assignment[0]))

print('Does the copy made with [:] hold different objects than those in original list?',
      id(first_element_original_lst) != id(lst_copy_slicing[0]))
print('Does the copy made with .copy() hold different objects than those in original list?',
      id(first_element_original_lst) != id(lst_copy_copyfn[0]))
print('Does the copy made with copy.deepcopy() hold different objects than those in original list?',
      id(first_element_original_lst) != id(lst_copy_deepcopy[0]))
print('Does the copy made with our own copy_list function hold different objects than those in original list?',
      id(first_element_original_lst) != id(lst_copy_ourfn[0]))

# Only .deepcopy and our function (in which we created new element-lists)
# hold different objects than those in the original list

# Q: what, if anything, changes if inside lst we have dicts? How about tuples?
