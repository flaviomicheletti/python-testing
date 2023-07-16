class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        return NotImplemented

    def area(self):
        return self.width * self.height


def test_comparison_example():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(5, 6)
    r3 = Rectangle(3, 4)

    # Equality comparison
    assert r1 == r3
    assert r1 != r2

    # Less than comparison
    assert r1 < r2
    assert not r2 < r1

    # Greater than comparison
    assert r2 > r1
    assert not r1 > r2

    # Less than or equal to comparison
    assert r1 <= r3
    assert r1 <= r2
    assert not r2 <= r1

    # Greater than or equal to comparison
    assert r2 >= r1
    assert r1 >= r3
    assert not r1 >= r2

"""
The comparison and equality methods are implemented as follows: 

- `__eq__(self, other)`: This method checks if two rectangles are equal by 
comparing their `width` and `height` attributes. It returns `True` if the 
rectangles have the same dimensions, and `False` otherwise. 

- `__ne__(self, other)`: This method uses the `__eq__()` method to determine 
inequality. It returns the negation of the result of `__eq__()`. 

- `__lt__(self, other)`: This method compares rectangles based on their 
areas. It calculates the areas of both rectangles using the `area()` method 
and returns `True` if the area of the current rectangle is less than the area 
of the other rectangle. 

- `__gt__(self, other)`: This method compares rectangles based on their 
areas. It calculates the areas of both rectangles using the `area()` method 
and returns `True` if the area of the current rectangle is greater than the 
area of the other rectangle. 

- `__le__(self, other)`: This method compares rectangles based on their 
areas. It calculates the areas of both rectangles using the `area()` method 
and returns `True` if the area of the current rectangle is less than or equal 
to the area of the other rectangle. 

- `__ge__(self, other)`: This method compares rectangles based on their 
areas. It calculates the areas of both rectangles using the `area()` method 
and returns `True` if the area of the current rectangle is greater than or 
equal to the area of the other rectangle. 

The `test_comparison_example()` function tests the comparison and equality 
methods. It creates three instances of the `Rectangle` class: `r1`, `r2`, 
and `r3`. It then asserts the expected results for equality, less than, 
greater than, less than or equal to, and greater than or equal to 
comparisons. 

This example demonstrates how the comparison and equality methods can be used 
to define custom comparisons between objects of a class based on specific 
attributes or criteria.
"""