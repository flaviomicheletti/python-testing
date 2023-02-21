
https://www.datacamp.com/tutorial/decorators-python


# Instalation

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

    deactivate

## Install

In both environments you will need to install it only once.

    // in the first time
    pip install -U pytest
    pip install pytest-cov

## Running

    pytest


## Coverage

    pytest --cov . --cov-report html
