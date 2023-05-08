import re


def test_non_capturing_groups1():
    # Consider the regex pattern: (?:Mr|Ms|Mrs)\. (\w+)
    #
    # - The pattern starts with a non-capturing group (?:Mr|Ms|Mrs),
    #    which matches either "Mr", "Ms", or "Mrs" followed by a dot.
    # - The space character after the dot is matched literally.
    # - The second part (\w+) captures one or more word characters
    #   (letters, digits, or underscores) after the title.
    #
    # Using this pattern to match the string "Mr. Smith,"
    # the non-capturing group matches "Mr." without capturing it,
    # and the capturing group captures "Smith".
    pattern = r"(?:Mr|Ms|Mrs)\. (\w+)"
    text = "Mr. Smith"

    match = re.match(pattern, text)
    if match:
        entire_pattern = match.group()  # Captured value of the entire pattern
        assert entire_pattern == "Mr. Smith"

        name = match.group(1)  # Captured value of the capturing group
        assert name == "Smith"

        try:
            group2 = match.group(2)  # IndexError: no such group
        except IndexError:
            group2 = None

            assert group2 is None


def test_non_capturing_groups2():
    pattern = r"(?:https?|ftp)://\S+"
    text = "https://example.com"

    match = re.match(pattern, text)
    if match:
        url = match.group()  # Matched text
        assert url == "https://example.com"
