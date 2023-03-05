"""
*args    = Positional arguments
**kwargs = Keyword arguments
"""


def test_args_kwargs1():
    def foo(*args, **kwargs):
        param = []
        for arg in args:
            param.append(arg)
        for key, value in kwargs.items():
            param.append(f"{key} = {value}")
        return param

    expected = ["hello", "world", "name = Alice", "age = 30"]
    assert expected == foo("hello", "world", name="Alice", age=30)


def test_args_kwargs2():
    def foo(name, age, *hobbies, **kwargs):
        params = []
        params.append(f"Name: {name}")
        params.append(f"Age: {age}")
        params.append("Hobbies:")
        for hobby in hobbies:
            params.append(f"- {hobby}")
        if kwargs:
            params.append("Additional information:")
            for key, value in kwargs.items():
                params.append(f"- {key}: {value}")
        return params

    """
    Name: Alice
    Age: 25
    Hobbies:
    - reading
    - painting
    Additional information:
    - city: New York
    - occupation: engineer
    """

    expected = [
        "Name: Alice",
        "Age: 25",
        "Hobbies:",
        "- reading",
        "- painting",
        "Additional information:",
        "- city: New York",
        "- occupation: engineer",
    ]
    assert expected == foo(
        "Alice", 25, "reading", "painting", city="New York", occupation="engineer"
    )


def test_args_kwargs3():
    def concatenate(*args, **kwargs):
        separator = kwargs.get("separator", " ")
        return separator.join(args)

        assert "hello world" == concatenate("hello", "world")

        assert "hello-world" == concatenate("hello", "world", separator="-")

        expected = "hello\nworld\nhow\nare\nyou"
        assert expected == concatenate("hello", "world", "how", "are", "you", separator="\n")
