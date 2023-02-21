def sum_numbers_without_hint(a, b):
    return a + b


def sum_numbers_with_hint(a: int, b: int) -> int:
    return a + b


class TestHints:
    def test_sum_numbers_without_hint(self):
        assert sum_numbers_without_hint(10, 5) == 15
        assert sum_numbers_without_hint(10.3, 5) == 15.3
        assert sum_numbers_without_hint("Bob", "Mark") == "BobMark"

    def test_sum_numbers_with_hint(self):
        """
        Type hints are just that — hints.
        They show you which data type is expected,
        but nothing is stopping you from ignoring them.
        We’ll later explore how to force type checking by the Python interpreter,
        but let’s cover the basics first.
        """
        assert sum_numbers_with_hint(10, 5) == 15
        assert sum_numbers_with_hint(10.3, 5) == 15.3
        assert sum_numbers_with_hint("Bob", "Mark") == "BobMark"

    def test_variables_annotations(self):
        """
        We can also provide type hints for variables.
        Once again, these are just hints and do not affect how the code runs.
        """
        name: str = "Bob"
        age: int = 32
        rating: float = 7.9
        is_premium: bool = True

        assert name == "Bob"
        assert age == 32
        assert rating == 7.9
        assert is_premium == True
