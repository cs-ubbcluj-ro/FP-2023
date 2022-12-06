from lecture.examples.ex35_rational_calc.calculator import Calculator
from lecture.examples.ex35_rational_calc.domain import Rational


class UI:
    def __init__(self, calculator):
        self._commands = {'+': self.add_number, 'c': self.clear, 'u': self.undo, '?': self.count}
        self._calculator = calculator

    def _print_menu(self):
        """
        Print out the calculator menu
        """
        print("Calculator:")
        print("   + for adding a rational number")
        print("   c to clear the calculator")
        print("   u to undo the last operation")
        print("   ? to count the rational numbers created")
        print("   x to close the calculator")

    def add_number(self):
        a = int(input("Give numerator:"))
        b = int(input("Give denominator:"))
        q = Rational(a, b)
        self._calculator.add(q)

    def undo(self):
        self._calculator.undo()

    def clear(self):
        self._calculator.reset()

    def count(self):
        print("Number of rational instances created so far: " + str(self._calculator.get_number_count()))

    def start(self):

        self._calculator.reset()
        while True:
            self._print_menu()
            print("Total: " + str(self._calculator.get_total))
            _command = input().strip().lower()
            # Exit program
            if _command == 'x':
                return
                # Invalid option
            if _command not in self._commands:
                print("Bad command")
            # Run user option
            try:
                self._commands[_command]()
            except ValueError as ve:
                print("error - " + str(ve))


if __name__ == "__main__":
    # Initialize the calculator class
    calc = Calculator()
    # This allows us to use the UI class with any implementation of the Calculator
    ui = UI(calc)
    # Start the UI
    ui.start()
