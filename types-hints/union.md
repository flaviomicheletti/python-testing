# Union

In Python, the notation "Union[int, float]" represents a type hint using the `
Union` class from the `typing` module. It is used to indicate that a variable 
or function parameter can accept values of either `int` or `float` types. 

The `Union` class allows you to define multiple possible types for a single 
variable. In this case, `Union[int, float]` means that the variable can be 
assigned an integer (`int`) or a floating-point number (`float`). 

Here's an example of how you can use `Union[int, float]` as a type hint:

```python
from typing import Union

def process_number(num: Union[int, float]) -> None:
    # Function code here
    print(num)

# Example usage
process_number(5)       # Valid, an integer
process_number(3.14)    # Valid, a float
process_number('hello') # Invalid, not an int or float
```

In the example above, the `process_number` function takes a parameter `num` 
of type `Union[int, float]`, indicating that it can accept either an integer 
or a float as an argument. The function body can then handle the value 
accordingly. 

Using type hints like `Union[int, float]` can help improve code readability 
and enable static type checkers to catch potential type errors before runtime.