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


"""
The `__repr__()` method is used to define the string representation of the 
object that can be used to recreate the object. In this case, it returns a 
string in the format "Point(x, y)", where `x` and `y` are the coordinates of 
the point. 

The `__str__()` method defines a human-readable string representation of the 
object. It returns a string in the format "(x, y)", where `x` and `y` are the 
coordinates of the point. 

The `__format__()` method allows customization of the string representation 
using the `format()` function. In this case, it checks the `format_spec` 
parameter and if it is "0.2f", it returns the formatted string representation 
of the point with two decimal places. Otherwise, it returns the default 
string representation. 
"""