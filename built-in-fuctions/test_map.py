
def test_map1():
    # Using map() to apply the custom function to each number
    numbers = [1, 2, 3, 4, 5]

    # Custom function to square a number
    def square(x):
        return x ** 2

    squared_numbers = map(square, numbers)
    assert list(squared_numbers) == [1, 4, 9, 16, 25]

    squared_numbers = list(map(square, numbers))
    assert squared_numbers == [1, 4, 9, 16, 25]


def test_map2():
    # Using map() to calculate the length of each string
    words = ["cat", "dog", "elephant", "lion"]

    word_lengths = map(len, words)
    assert list(word_lengths) == [3, 3, 8, 4]

    word_lengths = list(map(len, words))
    assert word_lengths == [3, 3, 8, 4]


def test_map3():
    # Using map() to convert each string to uppercase
    words = ["apple", "banana", "cherry"]

    uppercased_words = map(str.upper, words)
    assert list(uppercased_words) == ["APPLE", "BANANA", "CHERRY"]

    uppercased_words = list(map(str.upper, words))
    assert uppercased_words == ["APPLE", "BANANA", "CHERRY"]


def test_map4():
    # Using map() to double each number
    numbers = [1, 2, 3, 4, 5]

    doubled_numbers = map(lambda x: x * 2, numbers)
    assert list(doubled_numbers) == [2, 4, 6, 8, 10]
    
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    assert doubled_numbers == [2, 4, 6, 8, 10]
