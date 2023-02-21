![image](https://user-images.githubusercontent.com/1257048/220415580-5feae350-6eb3-4b31-bd95-1d6b98f2885e.png)

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
