# Collections


## Tell me about Collections in Python?

In Python, a collection refers to a group of objects or values that are 
stored together as a single unit. Python provides several built-in collection 
types that are used to store and organize data in different ways, depending 
on the requirements of your program. The commonly used collection types in 
Python include lists, tuples, sets, and dictionaries. 

1. Lists:
   - Lists are ordered collections that can hold a sequence of objects.
   - They are created using square brackets ([]).
   - Lists can store elements of different types, and they allow duplicates.
   - You can access elements in a list using indexing and slicing.
   - Lists are mutable, which means you can modify, add, or remove elements after creation.

2. Tuples:
   - Tuples are similar to lists but are immutable, meaning they cannot be modified once created.
   - They are created using parentheses ().
   - Tuples can store elements of different types, and they allow duplicates.
   - You can access elements in a tuple using indexing and slicing, similar to lists.

3. Sets:
   - Sets are unordered collections of unique elements.
   - They are created using curly braces ({}) or the `set()` function.
   - Sets do not allow duplicate elements, and the order of elements is not preserved.
   - You can perform various set operations like union, intersection, and difference.
   - Sets are mutable, so you can add or remove elements after creation.

4. Dictionaries:
   - Dictionaries are key-value pairs, where each value is associated with a unique key.
   - They are created using curly braces ({}) or the `dict()` constructor.
   - Dictionaries are unordered, meaning the order of elements may not be preserved.
   - Keys in dictionaries must be immutable types (strings, numbers, or tuples), while values can be of any type.
   - You can access, add, modify, or delete elements in a dictionary using keys.

Python also provides additional collection types through built-in modules or 
libraries, such as `collections` and `array`. 

Additionally, you can use various operations and methods on collections to 
perform common tasks, like iterating over elements, checking membership, 
sorting, filtering, and more. 

Collections in Python are versatile and widely used, allowing you to handle 
and manipulate data efficiently in different scenarios. 


## Tell about module `collections`?

The `collections` module is a built-in module in Python that provides 
additional collection types and utilities beyond the basic built-in 
collections. It offers specialized data structures that can be used to solve 
specific programming problems efficiently. Some commonly used classes 
provided by the `collections` module include: 

1. `namedtuple`:
   - This class creates tuple subclasses with named fields.
   - It provides a way to define a tuple type with named fields, similar to a struct in C or a record in Pascal.
   - Namedtuples are immutable and can be accessed by both index and attribute names.
   - They are useful for creating lightweight objects with a small, fixed set of fields.

2. `deque`:
   - A deque (double-ended queue) is a data structure that allows efficient insertion and deletion from both ends.
   - It provides O(1) time complexity for appending and popping elements from either end.
   - Deques can be used as queues, stacks, or general-purpose dynamic arrays.
   - They offer features like thread-safe, bounded length deques and rotating elements.

3. `Counter`:
   - The `Counter` class is used to count the occurrences of elements in a collection.
   - It is a subclass of `dict` and provides a convenient way to count hashable objects.
   - Counters can be created from iterables, such as lists or strings

