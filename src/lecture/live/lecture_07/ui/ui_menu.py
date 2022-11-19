# import lecture.live.lecture_07.domain.rational_dict as rational_d
# import lecture.live.lecture_07.domain.rational_list as rational_l
# from lecture.live.lecture_07.domain.rational_dict import create_q
from lecture.live.lecture_07.domain.rational_list import create_q
from lecture.live.lecture_07.functions.calculator import add_q,to_str

def add_rational(total):
    num = int(input("enter numerator:"))
    den = int(input("enter denominator:"))

    q = create_q(num, den)
    if q is None:
        print("Invalid rational number")
        return

    return add_q(q, total)


def print_menu():
    print("+ add a rational number to the calculator")
    print("u undo the last operation")
    print("x exit")


def start():
    total = create_q(0)
    while True:
        print_menu()
        print("Total: " + to_str(total))
        opt = input(">")

        if opt == "+":
            total = add_rational(total)
        elif opt == "x":
            break
        else:
            print("Bad user option")


if __name__ == "__main__":
    start()
    # q = rational_d.create_q(1,2)
    # print(q)
    # q = rational_l.create_q(1, 2)
    # print(q)

