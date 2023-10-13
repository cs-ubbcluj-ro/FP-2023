"""
After the seminar, you will be able to:
    - write a menu-driven application
    - work with Python lists and dictionaries
    - manage program entities
        - representation
        - manipulation
"""
"""
Problem statement
    A program that manages a list of TO-DO tasks.
    A TO-DO task has a description (description, str) and day of deadline
        (deadline_day, int, 1<deadline_day<365)

    The program must allow the following actions through a menu:
        - [Seminar] Add a TO-DO task from the console
        - [Seminar] Generate random tasks (descriptions are chosen from predefined set)
        - [A] Sort the list of tasks by deadline
        - [+] Print the list of tasks by day
        - [+] Count the number of tasks in a given interval of days (e.g. 3-100)
        - Exit the program
"""

import random

PREDEFINED_DESCRIPTIONS = ['BookSkydivingAdventure', 'HostMovieMarathon', 'TravelToUnchartedIsland',
                           'LearnJuggling', 'StartVegetableGarden', 'BuildTreehouse', 'VisitAlpacaFarm',
                           'MasterArtOfOrigami', 'StartBookClub', 'WriteSong']


# functions that manage my program entity, a task
# other parts of the program should only use these functions
# and not access the representation directly
def create_task(description, deadline):
    """
    Create task with given description
    :param description: description of the task
    :param deadline: day of deadline for task
    :return: newly created task
    """
    return {"description": description, "deadline": deadline}


def get_description(task):
    return task['description']


def get_deadline(task):
    return task['deadline']


# Uijfalusi Abel
# Q: is read_task a good name for the function? does it do reading/only reading?
def read_task():
    description = input("Please provide a task description:\n")
    deadline = int(input("Please provide a deadline:"))
    task = create_task(description, deadline)
    return task


def print_task_list(task_list):
    # Q: In what other ways could we write the print code? Hint: check other seminar problems+solutions
    print('This is the current list of tasks:')
    for task in task_list:
        print('Description:', get_description(task), '| Deadline day:', get_deadline(task))

    #different ways to go through the list
    #for index in range(len(task_list)):
    #   task = task_list[index]
    #   print('['+str(index)+']', 'Description: ', get_description(task), 'Deadline day:', get_deadline(task))
    #for task_index, task in enumerate(task_list):
    #   print('['+str(task_index)+']', 'Description: ', get_description(task), 'Deadline day:', get_deadline(task))


def add_to_list(task_list, task):
    """
    Adds the given task to the list of tasks
    :return: modifies the task_list by adding the given task at the end
    """
    task_list.append(task)


# check out https://pythontutor.com/render.html#mode=edit
# for a cool visualization of code (especially useful to visualize
# what happens in code like the above, and in functions like the other
# one we discussed, e.g.
# def modify_list_by_reassignment(tl):
#   tl = [new_task_1, new_task_2,...]
# which, in calling modify_list_by_reassignment(task_list) wouldn't actually modify task_list
# you could also try:
# a=[1,2,3]
# b=a
# b.append(4)
# print(a)
# to see what happens :)


# data representation
# R1: example_task = {'description': 'LearnJuggling', 'deadline_day': 176}
# R2: example_task = ['LearnJuggling', 176] (convention that on the first pos we have description and on second the day)
# R3: example_task = ('LearnJuggling', 176) (...)

# task_list = [example_task_1, example_task_2,...]
# task_list = list of dictionaries if task represented as dict (R1)
# task_list = list of lists if task represented as list (R2)
# task list = list of tuples if task represented as tuple (R3)


task_list = []
menu_text = "0. Print all tasks\n1. Add task\n2. Generate random task\n3. Sort list by day\n4. Exit"

while True:
    print(menu_text)
    option = input(">>>")
    option = option.strip()

    if option.isdigit():
        option = int(option)
    else:
        print("Invalid command. Enter number (between 0-4).")
        continue
    if option == 0:
        print_task_list(task_list)
    # also see match-case syntax
    if option == 1:
        task = read_task()
        add_to_list(task_list, task)
    elif option == 2:
        # generate task
        day = random.randint(1, 365)
        # we could have also used: random.choice
        description_index = random.randint(0, len(PREDEFINED_DESCRIPTIONS) - 1)
        description = PREDEFINED_DESCRIPTIONS[description_index]
        task = create_task(description, day)
        add_to_list(task_list, task)

    elif option == 3:
        # sort tasks
        pass
    elif option == 4:
        break
    else:
        print('Invalid command.')



# Working with dictionaries
# let's define a dict that contains information about persons
# key should be something unique, that differentiates that person from others (e.g. CNP)
# Example 1
# For each person, we keep pairs of key=CNP and value = Name
# persons = {}
# persons[123] = 'Michael' (let's assume 123 is valid CNP)
# persons[832] = 'John' (Q: should the CNP be str or int?)

# but we can hold more info about a person - we can have lists, dicts, lists of dicts as values
# start with a dictionary already containing 1 entry
# persons = {'123':{'name': 'Michael', 'job':'programmer', 'birthplace':'Hawaii', 'age': 49}}
# persons['463']={'ocupation':'juggler', 'birthplace':'USA'}
# Q: Is it a problem that the second value-dict (for person with CNP=463)
#           doesn't have the same keys? Will it give me an error?

# for person_id, person_information in persons.items():
#     print('CNP:', person_id)
#     for person_attribute, attribute_value in person_information.items():
#         print(person_attribute, attribute_value)
#for person_id in persons:
#   ...
#persons.keys() -> all the keys in my dictionary
#persons.values() -> all values in my dictionary