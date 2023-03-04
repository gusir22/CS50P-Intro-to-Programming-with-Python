import random
import pytest
from fuel import convert, gauge


def test_gauge_readings():
    """Tests the outputs from the gauge function"""
    assert gauge(1) == "E"  # empty
    assert gauge(99) == "F"  # full tank
    assert gauge(100) == "F"  # full tank

    # test for values between 1 and 99
    for i in range(2, 99):
        assert gauge(i) == f"{i}%"


def test_convert_calculations():
    """Tests the accuracy of the percentages calculated using ten random fraction"""
    for i in range(10):
        x = random.randint(1, 10)
        y = random.randint(10, 20)  # range is higher to prevent x > y ValueError
        assert convert(f"{x}/{y}") == round((x/y)*100)


def test_convert_divide_by_zero_error():
    """Tests that convert() will raise a ZeroDivisionError if user assigns 0 to y"""
    with pytest.raises(ZeroDivisionError):
        convert(f"{random.randint(1, 10)}/0")


def test_x_greater_than_y_error():
    """Tests that convert() will raise a ValueError if user assigns x a greater
    value than y"""
    with pytest.raises(ValueError):
        for i in range(10):
            x = random.randint(10, 20)
            y = random.randint(1, 9)  # range is smaller to trigger x > y ValueError
            convert(f"{x}/{y}")


def test_convert_divide_by_str_error():
    """Tests that convert() will raise a ValueError if user assigns a str to x or y"""
    with pytest.raises(ValueError):
        convert("2/dog")
