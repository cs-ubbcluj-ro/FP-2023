from src2023.lecture.livecoding.lecture08.calculator import Calculator


class UI:
    def __init__(self):
        self.__calc = Calculator()

    def start(self):
        # TODO print menu
        print("Total " + str(self.__calc.value()))
        # ...


"""
A couple of rules
    UI class calls Calculator class methods
    Calculator class does not know about the UI
    Rational class does not know anything about the
        rest of the program
        
Function call flow:
    UI -> Calculator
    UI -> Rational (str for diplay)
    Calculator -> Rational (add, ...)
"""
ui = UI()
ui.start()
