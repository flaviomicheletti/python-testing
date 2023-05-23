import re


def test_splti1():
    # Example 1: Splitting a string using a space delimiter
    str1 = "Hello World, How are you today?"
    result1 = re.split(" ", str1)
    assert result1 == ['Hello', 'World,', 'How', 'are', 'you', 'today?']


def test_splti2():
    # Example 2: Splitting a string using a comma delimiter
    str2 = "Apple, Banana, Orange, Mango"
    result2 = re.split(",", str2)
    assert result2 == ['Apple', ' Banana', ' Orange', ' Mango']


def test_splti3():
    # Example 3: Splitting a string using multiple delimiters
    str3 = "Hello;World|How,Are:You"
    result3 = re.split("[;|,:]", str3)
    assert result3 == ['Hello', 'World', 'How', 'Are', 'You']


def test_splti4():
    # Example 4: Splitting a string with a maximum number of splits
    str4 = "1-2-3-4-5-6-7-8-9-10"
    result4 = re.split("-", str4, maxsplit=5)
    assert result4 == ['1', '2', '3', '4', '5', '6-7-8-9-10']
