import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


def test_shape():
    shape = Shape()
    assert shape.area() is None


def test_circle_area():
    c = Circle(5)
    assert math.isclose(c.area(), 78.5398, rel_tol=1e-3)


def test_square_area():
    s = Square(5)
    assert s.area() == 25


def test_polymorphism():
    shapes = [Circle(5), Square(5)]
    areas = [shape.area() for shape in shapes]
    assert math.isclose(areas[0], 78.5398, rel_tol=1e-3)
    assert areas[1] == 25
