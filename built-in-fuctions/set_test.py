"""
The signature of the built-in `set` function in Python is as follows:

```python
set(iterable)
```
The `set` function accepts a single optional parameter:

1. `iterable` (optional): An iterable object, such as a list, tuple, string, 
or any other iterable, that provides the initial elements for the set. If 
provided, the `set` function creates a new set containing the unique elements 
from the iterable. If omitted, an empty set is created. 

The `iterable` parameter is optional, which means you can call the `set` 
function without any arguments to create an empty set. If you pass an 
iterable as an argument, the `set` function iterates over the elements of the 
iterable and adds the unique elements to the new set. Duplicates are 
automatically removed, as sets only contain unique elements. 

It's important to note that the `iterable` parameter is not limited to a 
specific type and can accept any object that provides an iteration interface. 
Some examples of valid iterables are lists, tuples, strings, sets, 
dictionaries (which will use their keys), and even user-defined objects that 
implement the iterable protocol. 

When using the `set` function, remember that the order of the elements in the 
resulting set may not necessarily match the order of the elements in the 
original iterable. Sets are unordered collections, and the ordering of 
elements is not preserved. 

In summary, the `set` function creates a new set object and accepts an 
optional iterable parameter to initialize the set with unique elements from 
the iterable. If no iterable is provided, an empty set is created. 
"""
def test_set_list_tuple_string():
    my_set = set([1, 2, 3])
    assert my_set == {1, 2, 3}

    my_set = set((1, 2))
    assert my_set == {1, 2}

    my_set = set("hello")
    assert my_set == {"e", "h", "l", "o"}


def test_set_remove_duplicates():

    """
    In this example, the `set` function is used to create a set from a list of
    fruits. Note that the resulting set only contains unique items, as sets do
    not allow duplicates.
    """

    fruits = ["apple", "banana", "orange", "kiwi", "apple"]
    fruit_set = set(fruits)
    assert fruit_set == {"orange", "banana", "kiwi", "apple"}

    my_list = [1, 2, 3, 3, 4, 5, 5]
    my_set = set(my_list)
    assert my_set == {1, 2, 3, 4, 5}

    my_string = "hello world"
    my_set = set(my_string)
    assert my_set == {"e", "d", "r", "h", "l", "o", "w", " "}


def test_set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    intersection = set1.intersection(set2)
    assert intersection == {3, 4, 5}
