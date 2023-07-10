from pymongo import MongoClient

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.client = None

    def connect(self, connection_string):
        if not self.client:
            self.client = MongoClient(connection_string)

    def get_connection(self):
        if self.client:
            return self.client
        else:
            raise Exception("Connection has not been established.")

    def close(self):
        if self.client:
            self.client.close()
            self.client = None

"""
In this code snippet, we're implementing the singleton pattern. Here's what 
each part does: 

1. `_instance = None`: This line initializes a class attribute `_instance` 
to `None`. The purpose of this attribute is to store the single instance of 
the class that will be created. 

2. `def __new__(cls, *args, **kwargs):`: The `__new__` method is a special 
method in Python that is responsible for creating and returning a new 
instance of the class. It is called before the `__init__` method. 

3. `if not cls._instance:`: This condition checks if the `_instance` 
attribute is `None`. If it is `None`, it means that no instance of the class 
has been created yet. 

4. `cls._instance = super().__new__(cls)`: If the `_instance` attribute is `
None`, this line creates a new instance of the class using `super().__new__(
cls)`. The `super()` function is used to call the parent class's `__new__` 
method, which handles the actual creation of the instance. 

5. `return cls._instance`: Finally, the newly created instance is stored in 
the `_instance` attribute and returned. On subsequent calls to create an 
instance of the class, the existing instance stored in `_instance` will be 
returned instead of creating a new instance. This ensures that only one 
instance of the class exists throughout the program. 

By implementing this logic in the `__new__` method, we ensure that only one 
instance of the `DatabaseConnection` class is created, and subsequent calls 
to create an instance will return the existing instance instead of creating a 
new one. This enforces the singleton pattern and allows all parts of your 
code to access and use the same instance of the class, ensuring the reuse of 
the database connection. 
"""


