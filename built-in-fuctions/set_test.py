def test_set_list_tuple_string():
    my_set = set([1, 2, 3])
    assert my_set == {1, 2, 3}

    my_set = set((1, 2))
    assert my_set == {1, 2}

    my_set = set("hello")
    assert my_set == {"e", "h", "l", "o"}


def test_set_remove_duplicates():

    """
    In this example, the `set` function is used to create a set from a list of
    fruits. Note that the resulting set only contains unique items, as sets do
    not allow duplicates.
    """

    fruits = ["apple", "banana", "orange", "kiwi", "apple"]
    fruit_set = set(fruits)
    assert fruit_set == {"orange", "banana", "kiwi", "apple"}

    my_list = [1, 2, 3, 3, 4, 5, 5]
    my_set = set(my_list)
    assert my_set == {1, 2, 3, 4, 5}

    my_string = "hello world"
    my_set = set(my_string)
    assert my_set == {"e", "d", "r", "h", "l", "o", "w", " "}


def test_set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    intersection = set1.intersection(set2)
    assert intersection == {3, 4, 5}
