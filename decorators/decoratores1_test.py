def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hi():
    return "hello there"


def test_decorator1():
    decorate = uppercase_decorator(say_hi)
    assert "HELLO THERE" == decorate()
