# Python Testing


## Instalation

    # venv
    python3 -m venv .venv && . .venv/bin/activate
    deactivate

    # deps
    pip install -U pytest
    pip install pytest-cov

## Running

    # tests
    pytest

    # coverage
    pytest --cov . --cov-report html
