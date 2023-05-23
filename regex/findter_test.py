import re

"""
In Python, the re.finditer(pattern, str) function is used to 
find all non-overlapping matches of a regular expression 
pattern within a given string. It returns an iterator yielding 
match objects for each match found.
"""


def test_finditer_1():
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"\b\w+\b"  # Matches words

    matches = re.finditer(pattern, text)
    word_list = [match.group() for match in matches]

    assert word_list == ['The', 'quick', 'brown',
                         'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


def test_finditer_2():
    text = "The cat in the hat sat on the mat."
    pattern = r"\b\w{3}\b"  # Matches three-letter words

    matches = re.finditer(pattern, text)
    word_list = [match.group() for match in matches]

    assert word_list == ['The', 'cat', 'the', 'hat', 'sat', 'the', 'mat']


def test_finditer_3():
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"\b\w{4}\b"  # Matches four-letter words

    matches = re.finditer(pattern, text)
    word_list = [match.group() for match in matches]

    assert word_list == ['over', 'lazy']
