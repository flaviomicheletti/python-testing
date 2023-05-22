# Python types

- http://mypy-lang.org/
- https://betterdatascience.com/python-statically-typed/

    python3 -m unittest discover -p '*_test.py'

    mypy my.py


## Try My.py

    cd types_hints
    pip install -r requirements.txt
    mypy try-my.py

    try-my.py:6: error: Argument 1 to "add_numbers" has incompatible type "float"; expected "int"  [arg-type]
    try-my.py:7: error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]
    try-my.py:7: error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"  [arg-type]    

## See Also

- https://realpython.com/python-type-checking/