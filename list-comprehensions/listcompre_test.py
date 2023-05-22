
def test_list_comprehensions1():
    numbers = [1, 2, 3, 4, 5]
    squares = [x ** 2 for x in numbers]
    assert squares == [1, 4, 9, 16, 25]


def test_list_comprehensions2():
    """List comprehensions can also include conditional statements
    to filter elements based on certain criteria"""
    numbers = [1, 2, 3, 4, 5]
    even_numbers = [x for x in numbers if x % 2 == 0]
    assert even_numbers == [2, 4]


def test_list_comprehensions3():
    """List comprehensions can also be nested and used with multiple iterables."""
    colors = ['red', 'green', 'blue']
    sizes = ['small', 'medium', 'large']
    combinations = [(color, size) for color in colors for size in sizes]
    assert combinations == [
        ('red', 'small'),
        ('red', 'medium'),
        ('red', 'large'),
        ('green', 'small'),
        ('green', 'medium'),
        ('green', 'large'),
        ('blue', 'small'),
        ('blue', 'medium'),
        ('blue', 'large')
    ]

    # another example
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c', 'd', 'e']
    combined = [(x, y) for x in numbers for y in letters]
    assert combined == [
        (1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (1, 'e'),
        (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (2, 'e'),
        (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (3, 'e')
    ]

def test_list_comprehensions4():
    """List comprehensions can be adapted to create sets and dictionaries as well"""
    numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    unique_numbers = {x for x in numbers}
    assert unique_numbers == {1, 2, 3, 4, 5}

    # another example
    names = ['Alice', 'Bob', 'Charlie']
    name_lengths = {name: len(name) for name in names}
    assert name_lengths == {'Alice': 5, 'Bob': 3, 'Charlie': 7}

