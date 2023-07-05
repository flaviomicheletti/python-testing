
def test_merging_two_dictionaries():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    merged_dict = {**dict1, **dict2}
    assert merged_dict == {"a": 1, "b": 2, "c": 3, "d": 4}


def test_overriding_values():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    merged_dict = {**dict1, **dict2}
    assert merged_dict == {"a": 1, "b": 3, "c": 4}


def test_function_call_with_dictionary_unpacking():
    def person_info(name, age):
        return f"Name: {name}, Age: {age}"

    person = {"name": "Alice", "age": 30}

    assert person_info(**person) == "Name: Alice, Age: 30"


def test_adding_additional_key_value_pairs():
    original_dict = {"a": 1, "b": 2}

    extended_dict = {**original_dict, "c": 3, "d": 4}
    assert extended_dict == {"a": 1, "b": 2, "c": 3, "d": 4}
