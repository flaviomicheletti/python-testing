"""
In Python, interfaces are typically implemented using abstract base classes 
(ABCs) from the abc module. Here's an example that demonstrates the concept 
of interfaces:
"""

from abc import ABC, abstractmethod

# Define the interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Implement classes that adhere to the interface
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

def test_interface():
    # Create instances of the classes
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    # Use the instances as instances of the interface
    assert rectangle.area() ==   20
    assert rectangle.perimeter() ==  18
    assert round(circle.area(), 2) == 28.27
    assert round(circle.perimeter(), 2) == 18.85
