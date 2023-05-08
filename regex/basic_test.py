# Step1: Import the regex module
import re


def test_regex1():
    # Step 2: Define a pattern
    pattern = re.compile(r'Hello')

    # Step 4: Perform matching or searching operations
    string = 'Hello, world!'
    match_obj = pattern.search(string)

    # Step 5: Extract matched data
    if (match_obj):
        matched_data = match_obj.group()
        assert matched_data == "Hello"


def test_regex2():

    # Encapsulated in a function
    def myregex(string):
        pattern = re.compile(r'Hello')
        match_obj = pattern.search(string)
        if (match_obj):
            return match_obj.group()
        else:
            return None

    assert "Hello" == myregex('Hello, world!')
    assert None == myregex('H000, world!')
