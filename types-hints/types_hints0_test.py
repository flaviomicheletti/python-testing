from typing import List, Tuple, Union, Optional


def test_tType_aliases():
    Vector = List[float]

    def scale_vector(vector: Vector, scalar: float) -> Vector:
        return [element * scalar for element in vector]

    input_vector = [1.0, 2.0, 3.0]
    output_vector = scale_vector(input_vector, 2.0)
    assert output_vector == [2.0, 4.0, 6.0]


def test_type_hints_for_variables():
    name: str = "John"
    age: int = 25

    def greet_person(name: str) -> str:
        return f"Hello, {name}!"

    greeting = greet_person(name)
    assert greeting == "Hello, John!"


def test_type_hints_for_function_parameters():
    def add_numbers(x: int, y: int) -> int:
        return x + y

    input_x = 5
    input_y = 3
    result = add_numbers(input_x, input_y)
    assert result  == 8


def test_type_hints_for_function_return_values():
    def calculate_average(numbers: List[float]) -> float:
        total = sum(numbers)
        return total / len(numbers)

    input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    average = calculate_average(input_numbers)
    assert average  == 3.0


def test_type_hints_for_collections():
    def process_names(names: List[str]) -> List[str]:
        processed_names = [name.upper() for name in names]
        return processed_names

    input_names = ["Alice", "Bob", "Charlie"]
    processed_names = process_names(input_names)
    assert processed_names  == ["ALICE", "BOB", "CHARLIE"]


def test_generic_types():
    def reverse_pairs(pairs: List[Tuple[str, int]]) -> List[Tuple[int, str]]:
        reversed_pairs = [(pair[1], pair[0]) for pair in pairs]
        return reversed_pairs

    input_pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    reversed_pairs = reverse_pairs(input_pairs)
    assert reversed_pairs  == [(25, "Alice"), (30, "Bob"), (35, "Charlie")]


def test_union_types():
    def square_or_double(value: Union[int, float]) -> Union[int, float]:
        if isinstance(value, int):
            return value ** 2
        elif isinstance(value, float):
            return value * 2.0

    input_value = 3.5
    result = square_or_double(input_value)
    assert result  == 7.0


def test_optional_types():
    def get_length(string: Optional[str]) -> Optional[int]:
        if string is None:
            return None
        return len(string)

    input_string = "Hello"
    length = get_length(input_string)
    assert length  == 5

