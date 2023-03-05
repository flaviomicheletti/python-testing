def test_lambda_simple():
    key = lambda x: x[1]

    assert "b" == key(
        [
            "a",
            "b",
            "c",
            "d",
        ]
    )  # list
    assert "b" == key(("a", "b", "c", "d"))  # tuple
    assert (2, 1) == key([(1, 3), (2, 1), (3, 2)])  # a list of tuples


def test_lambda_square():
    """squares each element of the list"""
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, numbers))
    assert squares == [1, 4, 9, 16, 25]


def test_lambda_number_even():
    """whether the number is even"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    assert even_numbers == [2, 4, 6, 8, 10]


def test_lambda_sort_list1():

    students = [("Alice", 22), ("Bob", 19), ("Charlie", 21), ("David", 20)]

    students_sorted = sorted(students, key=lambda x: x[1])

    assert students_sorted == [
        ("Bob", 19),
        ("David", 20),
        ("Charlie", 21),
        ("Alice", 22),
    ]


def test_lambda_sort_list2():
    """Sort list of tuples by second element"""

    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20},
    ]

    # Sort the list of dictionaries by age
    people_sorted = sorted(people, key=lambda x: x["age"])
    assert people_sorted == [
        {"name": "Charlie", "age": 20},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
    ]

    people_sorted = sorted(people, key=lambda x: x["name"])
    assert people_sorted == [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20},
    ]


def test_lambda_sort_dic():
    """Sort dictionary by value"""
    my_dict = {"apple": 3, "banana": 1, "orange": 2, "pear": 4}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    assert sorted_dict == {"banana": 1, "orange": 2, "apple": 3, "pear": 4}


def test_lambda_return_another_func():
    """Creating a function that returns another function"""

    def power(n):
        return lambda x: x**n

    # Create a function that squares a number
    square = power(2)
    assert square(5) == 25

    # Create a function that cubes a number
    cube = power(3)
    assert cube(5) == 125


def test_lambda_combine_lists():
    """Combine two lists using a lambda function"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = list(map(lambda x, y: x + y, list1, list2))
    assert combined_list == [5, 7, 9]
