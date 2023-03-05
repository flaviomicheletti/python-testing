import pytest


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


"""
my_car = Car()
my_car.start() # Output: Engine started
"""


def test_car_start_method():
    my_car = Car()
    my_car.start()

    assert True


def test_engine_start_method(capsys):
    my_engine = Engine()
    my_engine.start()

    captured = capsys.readouterr()
    assert captured.out == "Engine started\n"
