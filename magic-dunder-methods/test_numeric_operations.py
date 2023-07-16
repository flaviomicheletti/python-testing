class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imag = self.imag + other.imag
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imag = self.imag - other.imag
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real ** 2 + other.imag ** 2
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, ComplexNumber):
            raise TypeError("Floor division is not supported for complex numbers.")
        return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, ComplexNumber):
            raise TypeError("Modulo operation is not supported for complex numbers.")
        return NotImplemented
    
    def __pow__(self, other, modulo=None):
        if isinstance(other, ComplexNumber):
            raise TypeError("Exponentiation is not supported for complex numbers.")
        return NotImplemented
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"


def test_numeric_operations_example():
    c1 = ComplexNumber(2, 3)
    c2 = ComplexNumber(4, 5)
    
    # Addition
    result_add = c1 + c2
    assert str(result_add) == "6 + 8i"
    
    # Subtraction
    result_sub = c1 - c2
    assert str(result_sub) == "-2 + -2i"
    
    # Multiplication
    result_mul = c1 * c2
    assert str(result_mul) == "-7 + 22i"
    
    # Division
    result_div = c1 / c2
    assert str(result_div) == "0.5609756097560976 + 0.04878048780487805i"
    
    # Floor Division
    try:
        c1 // c2
    except TypeError as e:
        assert str(e) == "Floor division is not supported for complex numbers."
    
    # Modulo
    try:
        c1 % c2
    except TypeError as e:
        assert str(e) == "Modulo operation is not supported for complex numbers."
    
    # Exponentiation
    try:
        c1 ** c2
    except TypeError as e:
        assert str(e) == "Exponentiation is not supported for complex numbers."


"""
In this example, we have a `ComplexNumber` class representing complex 
numbers. The class has attributes `real` and `imag` to store the real and 
imaginary parts of the complex number. 

The numeric operation methods are implemented as follows: 

- `__add__(self, other)`: This method performs addition of two complex 
numbers. It checks if the other operand is also a `ComplexNumber` object and 
performs addition on their real and imaginary parts. It returns a new `
ComplexNumber` object representing the sum. 

- `__sub__(self, other)`: This method performs subtraction of two complex 
numbers. It checks if the other operand is also a `ComplexNumber` object and 
performs subtraction on their real and imaginary parts. It returns a new `
ComplexNumber` object representing the difference. 

- `__mul__(self, other)`: This method performs multiplication of two complex 
numbers. It checks if the other operand is also a `ComplexNumber` object and 
performs complex multiplication using the formula: `(a + bi) * (c + di) = (
ac - bd) + (ad + bc)i`. It returns a new `ComplexNumber` object representing 
the product. 

- `__truediv__(self, other)`: This method performs division of two complex 
numbers. It checks if the other operand is also a `ComplexNumber` object and 
performs complex division using the formula: `(a + bi) / (c + di) = [(ac + 
bd) / (c^2 + d^2)] + [(bc - ad) / (c^2 + d^2)]i`. It returns a new `
ComplexNumber` object representing the quotient. 

- `__floordiv__(self, other)`: This method raises a `TypeError` as floor 
division is not supported for complex numbers. 

- `__mod__(self, other)`: This method raises a `TypeError` as modulo 
operation is not supported for complex numbers. 

- `__pow__(self, other, modulo=None)`: This method raises a `TypeError` as 
exponentiation is not supported for complex numbers. 

The `test_numeric_operations_example()` function tests the numeric operation 
methods. It creates two instances of the `ComplexNumber` class: `c1` and `c2`
. It then performs addition, subtraction, multiplication, and division on 
these complex numbers using the implemented methods. The function asserts the 
expected results for each operation. 

This example demonstrates how the numeric operation methods can be used to 
define custom arithmetic operations for objects of a class, allowing them to 
behave like numeric types. 

"""