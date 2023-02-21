import pytest
from typing import List, Dict


def list_summation(lst: List[int]) -> int:
    return sum(lst)


class TestListSummation:
    #
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    #
    def test_list_summation(self):
        numbers: List[int] = [1, 2, 3]
        list_summation(numbers) == 6

        with pytest.raises(Exception) as context:
            names: List[str] = ["Bob", "Mark", "Jack"]
            list_summation(names)

    #
    # hints
    #
    def test_dict(self):
        emails: Dict[str, str] = {
            "Bob": "bob@email.com",
            "Mark": "mark@email.com",
            "Jack": "jack@email.com",
        }

        emails: Dict[str, str] = {
            "Bob": 123,
            456: "mark@email.com",
            "Jack": "jack@email.com",
        }
