"""
The `sorted()` function is a built-in function in Python that returns a new 
sorted list from the items in an iterable object (e.g., a list, tuple, or set).

The basic syntax of `sorted()` is as follows:

    sorted(iterable, key=None, reverse=False)

## iterable

Required argument. The iterable object to be sorted.

## key

Optional argument. A function that takes one argument and returns a 
value to use for sorting. By default, the sorting is done based on 
the elements themselves, rather than a derived value.

## reverse
 
Optional argument. If `True`, the items are sorted in descending order.
By default, the items are sorted in ascending order.
"""


def test_sorted1():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sorted(my_list)
    assert sorted_list == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_sorted2():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    unique_list = list(set(my_list))
    assert unique_list == [1, 2, 3, 4, 5, 6, 9]


def test_sorted3():
    """just for curiosity"""
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    unique_list = []
    for value in my_list:
        if value not in unique_list:
            unique_list.append(value)
    assert unique_list == [3, 1, 4, 5, 9, 2, 6]


def test_sorted4():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    sorted_fruits = sorted(fruits)
    assert sorted_fruits == ["apple", "banana", "cherry", "date", "elderberry"]


def test_sorted5():
    fruits = ["apple", "banana", "cherry", "date"]

    # Sort by the length of each fruit's name
    sorted_fruits_by_length = sorted(fruits, key=len)
    assert sorted_fruits_by_length == ["date", "apple", "banana", "cherry"]

    # Sort alphabetically, but with 'c' coming first
    sorted_fruits_by_c = sorted(fruits, key=lambda x: x.replace("c", "a"))
    assert sorted_fruits_by_c == ["cherry", "apple", "banana", "date"]


def test_sorted6():
    my_list = [("apple", 3), ("banana", 5), ("cherry", 6), ("date", 4)]
    sorted_list = sorted(my_list, key=lambda x: x[1]) # <-- based on number
    assert sorted_list == [("apple", 3), ("date", 4), ("banana", 5), ("cherry", 6)]

    my_list = [("apple", 3), ("banana", 5), ("cherry", 6), ("date", 4)]
    sorted_list = sorted(my_list, key=lambda x: x[0]) # <-- based on string
    assert sorted_list == [("apple", 3), ("banana", 5), ("cherry", 6), ("date", 4)]

