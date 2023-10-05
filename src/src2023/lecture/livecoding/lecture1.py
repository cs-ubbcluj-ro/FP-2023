# print("hello world")

"""
Display a menu
    1. Enter numbers
    2. Exit
    
after entering numbers, print out the prime ones
"""
def is_prime(n :int) -> bool:
    # TODO homework
    pass

while True:
    print("1. Enter numbers")
    print("2. Exit")
    option = input(">")
    if option == "1":
        numbers = input("enter numbers: ")
        number_list =numbers.split()
        int_number_list = [] # empty list

        for number in number_list:
            int_number_list.append(int(number))
            # go through the number list, call is_prime
            # print out prime numbers

        print(int_number_list)

        print(numbers)
    elif option =="2":
        print("bye")
        break
    else:
        print("error")






