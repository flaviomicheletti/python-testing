def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


def say_hi():
    return "hello there-1"


@uppercase_decorator
def say_hi():
    return "hello there-2"


@split_string
@uppercase_decorator
def say_hi():
    return "hello there-3"


def test_step3():
    assert ["HELLO", "THERE-3"] == say_hi()
