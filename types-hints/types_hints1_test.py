def add_numbers(a: int, b: int) -> int:
    return a + b


def test_type_hints():
    assert add_numbers(10, 5) == 15
    assert add_numbers(10.3, 5) == 15.3
    assert add_numbers("Bob", "Mark") == "BobMark"