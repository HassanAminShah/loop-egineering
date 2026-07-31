import pytest

from calculator import add, subtract, multiply, divide, is_even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    # Intentionally wrong expected value -> fails
    assert multiply(3, 4) == 13


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_even_true():
    assert is_even(4) is True


def test_is_even_false():
    # Intentionally wrong assertion -> fails
    assert is_even(7) is True


def test_add_negative():
    # Intentionally wrong expected value -> fails
    assert add(-1, -1) == 0
