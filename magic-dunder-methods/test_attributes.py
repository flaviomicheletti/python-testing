class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getattr__(self, name):
        return f"Attribute '{name}' does not exist."
    
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age cannot be negative.")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        if name == "age":
            raise AttributeError("Cannot delete age attribute.")
        super().__delattr__(name)


def test_attribute_management_example():
    person = Person("Alice", 25)
    
    # Attribute retrieval
    assert person.name == "Alice"
    assert person.age == 25
    assert person.gender == "Attribute 'gender' does not exist."
    
    # Attribute assignment
    person.name = "Bob"
    assert person.name == "Bob"
    
    try:
        person.age = -5
    except ValueError as e:
        assert str(e) == "Age cannot be negative."
    
    # Attribute deletion
    try:
        del person.age
    except AttributeError as e:
        assert str(e) == "Cannot delete age attribute."


"""
The attribute access and management methods are implemented as follows: 

- `__getattr__(self, name)`: This method is called when an attribute 
retrieval fails using the dot notation. It returns a custom message 
indicating that the attribute does not exist. 

- `__setattr__(self, name, value)`: This method is called when an attribute 
assignment is made using the dot notation. It checks if the attribute being 
set is `"age"` and if the value is negative. If so, it raises a `ValueError` 
indicating that the age cannot be negative. Otherwise, it uses `super()
.__setattr__(name, value)` to set the attribute normally. 

- `__delattr__(self, name)`: This method is called when an attribute deletion 
is attempted using the `del` statement. It checks if the attribute being 
deleted is `"age"`. If so, it raises an `AttributeError` indicating that the 
age attribute cannot be deleted. Otherwise, it uses `super().__delattr__(
name)` to delete the attribute normally. 

The `test_attribute_management_example()` function tests the attribute access 
and management methods. It creates an instance of the `Person` class and 
performs operations such as attribute retrieval, attribute assignment, and 
attribute deletion. It asserts the expected results for each operation. 

This example demonstrates how the attribute access and management methods can 
be used to customize attribute retrieval, assignment, and deletion behavior 
in a class. 
"""