import re


def test_findall_1():
    sentence = "The quick brown fox jumps over the lazy dog."
    word_occurrences = re.findall(r'\b\w+\b', sentence)
    assert word_occurrences == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


def test_findall_2():
    text = "Contact us at info@example.com or support@example.com for assistance."
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    assert email_addresses == ['info@example.com', 'support@example.com']

