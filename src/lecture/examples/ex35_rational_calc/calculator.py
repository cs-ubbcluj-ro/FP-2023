from lecture.examples.ex35_rational_calc.domain import Rational


class Calculator:
    def __init__(self):
        self._total = Rational(0)
        self._history = []

    @property
    def get_total(self):
        # Total is a read-only property
        return self._total

    def add(self, r):
        """
        Add a number to the calculator. Adding 0 will not create an undo point
        param:
            r - the number to add
        """
        if r == Rational(0):
            return
            # Record for undo
        self._history.append(self._total)
        # Add the value to calculator total
        self._total += r

    def undo(self):
        if len(self._history) == 0:
            raise ValueError('No more undo steps!')
        self._total = self._history.pop()

    @staticmethod
    def get_number_count():
        return Rational.get_total_number_of_instances()

    def reset(self):
        self._total = Rational(0)
