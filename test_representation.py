"""
string representation functions

The `repr()` and `str()` functions in Python belong to a broader category of
functions called "object representation functions" or "string representation functions." 

These functions are responsible for providing string representations of objects.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __format__(self, format_spec):
        if format_spec == "0.2f":
            return f"({self.x:.2f}, {self.y:.2f})"
        else:
            return str(self)


def test_reprexample():
    point = Point(3, 4)
    assert repr(point) == "Point(3, 4)"
    assert ascii(point) == "Point(3, 4)"
    assert str(point) == "(3, 4)"
    assert format(point) == "(3, 4)"
    assert format(point, "0.2f") == "(3.00, 4.00)"

    # others...
    assert hex(10) == "0xa"
    assert oct(10) == "0o12"
    assert bin(10) == "0b1010"
    assert chr(65) == "A"
    assert ord("A") == 65
