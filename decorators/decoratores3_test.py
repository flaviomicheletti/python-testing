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


def say_hi1():
    return "hello there-1"


@uppercase_decorator
def say_hi2():
    return "hello there-2"


@split_string
@uppercase_decorator
def say_hi3():
    return "hello there-3"


def test_decorator3():
    assert "hello there-1" == say_hi1()
    assert "HELLO THERE-2" == say_hi2()
    assert ["HELLO", "THERE-3"] == say_hi3()
