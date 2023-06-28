def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper


def say_hi1():
    return "hello there-1"


@uppercase_decorator
def say_hi2():
    return "hello there-2"


def test_decorator2():
    assert "hello there-1" == say_hi1()
    assert "HELLO THERE-2" == say_hi2()
