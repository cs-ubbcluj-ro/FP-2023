"""
Created on Nov 23, 2016

@author: Arthur
"""


class Shape:
    def __init__(self, color):
        # print("building a shape")
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def area(self):
        return 0

    def __str__(self):
        return "a " + self.color + " shape"


class Rectangle(Shape):
    def __init__(self, width, height, color):
        Shape.__init__(self, color)
        # print("building a rectangle")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return "a " + self.color + " rectangle"


class Square(Rectangle):
    def __init__(self, side, color):
        # print("building a square")
        Rectangle.__init__(self, side, side, color)

    @property
    def side(self):
        return self._width

    def __str__(self):
        return "a " + self.color + " square"


class Ellipse(Shape):
    def __init__(self, major, minor, color):
        Shape.__init__(self, color)
        # print("building an ellipse")
        self._major = major
        self._minor = minor

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def area(self):
        return 3.14 * self._minor * self._major

    def __str__(self):
        return "a " + self.color + " ellipse"


class Circle(Ellipse):
    def __init__(self, radius, color):
        Ellipse.__init__(self, radius, radius, color)
        # print("building a circle")

    @property
    def radius(self):
        return self.major

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return "a " + self.color + " circle"


if __name__ == "__main__":
    shape = Shape("red")
    print(str(shape) + ", area is = " + str(shape.area))

    """
        The rectangle 'is a' shape
    """
    rectangle = Rectangle(5, 2, "blue")
    print(str(rectangle) + ", area is = " + str(rectangle.area))

    """
        The square 'is a' particular rectangle
    """
    square = Square(3, "green")
    print(str(square) + ", area is =" + str(square.area))

    ellipse = Ellipse(10, 6, "pink")
    print(str(ellipse) + ", area is =" + str(ellipse.area))

    """
        The circle 'is a' particular ellipse
    """
    circle = Circle(8, "magenta")
    print(str(circle) + ", area is =" + str(circle.area))
