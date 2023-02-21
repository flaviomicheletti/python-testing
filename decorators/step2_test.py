def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper


def say_hi():
    return "hello there-1"


@uppercase_decorator
def say_hi():
    return "hello there-2"


def test_step2():
    assert "HELLO THERE-2" == say_hi()
