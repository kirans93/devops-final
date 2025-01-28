import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 3 * 3 == 9

def test_division():
    assert 10 / 2 == 5

if __name__ == "__main__":
    pytest.main()
