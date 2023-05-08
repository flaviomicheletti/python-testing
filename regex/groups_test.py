import re


def test_groups():
    pattern = re.compile(r'(\w+)\s-\s(\w+)')
    match_obj = pattern.match('John - Doe')

    if match_obj:
        # here
        assert match_obj.groups() == ('John', 'Doe')

        # just for curiosity
        assert match_obj.group(0) == 'John - Doe'
        assert match_obj.group(1) == 'John'
        assert match_obj.group(2) == 'Doe'


def test_groupdict():
    pattern = re.compile(r'(?P<last>\w+),\s(?P<first>\w+)')
    match_obj = pattern.match('Doe, John')
    if match_obj:
        # here
        assert match_obj.groupdict() == {'first': 'John', 'last': 'Doe'}

        # just for curiosity
        assert match_obj.group(0) == 'Doe, John'
        assert match_obj.group(1) == 'Doe'
        assert match_obj.group(2) == 'John'
