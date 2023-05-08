import re


def test_capturing_groups1():
    # Consider the regex pattern: (\d{3})-(\d{3})
    #
    # - The pattern consists of two capturing groups.
    # - The first capturing group (\d{3}) matches and captures
    # three consecutive digits.
    # - The hyphen - is matched literally.
    # - The second capturing group (\d{3}) matches and captures another three
    # consecutive digits.
    #
    # Using this pattern to match the string "123-456," the capturing groups will capture
    # "123" and "456" respectively.
    pattern = r"(\d{3})-(\d{3})"
    text = "123-456"

    match = re.match(pattern, text)
    if match:
        group1 = match.group(1)  # Captured value of the first group
        group2 = match.group(2)  # Captured value of the second group
        assert group1 == '123'
        assert group2 == '456'

        try:
            group3 = match.group(3)  # IndexError: no such group
        except IndexError:
            group3 = None

            assert group3 is None


def test_capturing_groups2():
    pattern = r"(\w+)\s(\w+)"
    text = "John Doe"

    match = re.match(pattern, text)
    if match:
        first_name = match.group(1)  # Captured value of the first group
        last_name = match.group(2)  # Captured value of the second group
        assert first_name == "John"
        assert last_name == "Doe"
