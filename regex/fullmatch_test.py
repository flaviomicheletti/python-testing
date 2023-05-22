import re


def test_fullmatch1():
    """Example 1: Matching a simple pattern"""
    pattern = r"hello"
    string = "hello"
    match = re.fullmatch(pattern, string)
    assert bool(match) == True
    assert str(match) == "<re.Match object; span=(0, 5), match='hello'>"

def test_fullmatch2():
    """Example 2: Pattern does not match the entire string"""
    pattern = r"\d+"
    string = "123abc"
    match = re.fullmatch(pattern, string)
    assert match == None
    assert bool(match) == False
    assert str(match) == "None"

def test_fullmatch3():
    """Example 3: Matching a more complex pattern"""
    pattern = r"\w+\s\w+"
    string = "John Doe"
    match = re.fullmatch(pattern, string)
    assert bool(match) == True
    assert str(match) == "<re.Match object; span=(0, 8), match='John Doe'>"