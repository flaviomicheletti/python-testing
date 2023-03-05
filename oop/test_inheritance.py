import pytest


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("make_sound method not implemented")


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


"""
my_dog = Dog("Fido", "Canine")
my_cat = Cat("Whiskers", "Feline")

print(my_dog.name)    # Output: Fido
print(my_cat.species) # Output: Feline

print(my_dog.make_sound()) # Output: Woof!
print(my_cat.make_sound()) # Output: Meow!
"""


def test_animal():
    # Test Animal class constructor and attributes
    animal = Animal("Bob", "Mammal")
    assert animal.name == "Bob"
    assert animal.species == "Mammal"

    # Test Animal class make_sound method
    with pytest.raises(NotImplementedError):
        animal.make_sound()


def test_dog():
    # Test Dog class constructor and attributes
    dog = Dog("Fido", "Canine")
    assert dog.name == "Fido"
    assert dog.species == "Canine"

    # Test Dog class make_sound method
    assert dog.make_sound() == "Woof!"


def test_cat():
    # Test Cat class constructor and attributes
    cat = Cat("Whiskers", "Feline")
    assert cat.name == "Whiskers"
    assert cat.species == "Feline"

    # Test Cat class make_sound method
    assert cat.make_sound() == "Meow!"
