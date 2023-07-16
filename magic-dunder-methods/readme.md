# Magic(dunder) methods in Python

In Python, magic methods, also known as dunder (double underscore) methods, 
are special methods that provide functionality to classes. These methods are 
surrounded by double underscores on both sides of their name, hence the term 
"dunder." Magic methods are automatically invoked by Python in response to 
certain events or operations. 

While it's not necessarily accurate to categorize all magic methods into 
distinct groups, we can loosely group some of them based on their 
functionality. Here are a few general groups of magic methods:

1. Initialization and String Representation:
   - `__init__(self, ...)`: Initialization method.
   - `__repr__(self)`: Debugging representation.
   - `__str__(self)`: String representation.
   - `__format__(self, format_spec)`: Custom string formatting.

2. Comparison and Equality:
   - `__eq__(self, other)`: Equality comparison.
   - `__ne__(self, other)`: Inequality comparison.
   - `__lt__(self, other)`: Less than comparison.
   - `__gt__(self, other)`: Greater than comparison.
   - `__le__(self, other)`: Less than or equal to comparison.
   - `__ge__(self, other)`: Greater than or equal to comparison.

3. Numeric Operations:
   - `__add__(self, other)`: Addition.
   - `__sub__(self, other)`: Subtraction.
   - `__mul__(self, other)`: Multiplication.
   - `__truediv__(self, other)`: Division.
   - `__floordiv__(self, other)`: Floor division.
   - `__mod__(self, other)`: Modulo (remainder).
   - `__pow__(self, other[, modulo])`: Exponentiation.

4. Container and Iteration:
   - `__len__(self)`: Length of the object.
   - `__getitem__(self, key)`: Item retrieval using indexing or slicing.
   - `__setitem__(self, key, value)`: Item assignment using indexing or slicing.
   - `__delitem__(self, key)`: Item deletion using indexing or slicing.
   - `__iter__(self)`: Iterator object creation.
   - `__next__(self)`: Retrieve next item from an iterator.
   - `__contains__(self, item)`: Membership check.

5. Attribute Access and Management:
   - `__getattr__(self, name)`: Attribute retrieval.
   - `__setattr__(self, name, value)`: Attribute assignment.
   - `__delattr__(self, name)`: Attribute deletion.


These groups provide a rough categorization of some commonly used magic 
methods based on their functionality. However, it's important to note that 
some magic methods may belong to multiple groups or have unique purposes. 

