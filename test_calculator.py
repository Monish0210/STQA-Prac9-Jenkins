"""Automated tests for calculator.py. Run with: python -m pytest -v"""


from calculator import add, subtract, multiply, divide


# Addition
def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_sign_numbers():
    assert add(-2, 5) == 3


def test_add_zero():
    assert add(8, 0) == 8


def test_add_decimals():
    assert add(1.5, 2.5) == 4.0


# Subtraction
def test_subtract_positive_numbers():
    assert subtract(9, 4) == 5


def test_subtract_result_is_negative():
    assert subtract(3, 8) == -5


def test_subtract_negative_numbers():
    assert subtract(-3, -8) == 5


def test_subtract_zero():
    assert subtract(7, 0) == 7


# Multiplication
def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(100, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12


def test_multiply_two_negative_numbers():
    assert multiply(-3, -4) == 12


def test_multiply_decimals():
    assert multiply(1.5, 2) == 3.0


# Division
def test_divide_evenly():
    assert divide(10, 2) == 5


def test_divide_with_remainder():
    assert divide(7, 2) == 3.5


def test_divide_negative_number():
    assert divide(-10, 2) == -5


def test_divide_two_negative_numbers():
    assert divide(-10, -2) == 5


def test_divide_zero_numerator():
    assert divide(0, 5) == 0




def test_divide():
    assert divide(10, 2) == 5