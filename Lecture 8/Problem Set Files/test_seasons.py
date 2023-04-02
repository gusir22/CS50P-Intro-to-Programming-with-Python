import datetime

import pytest

from seasons import (
    get_birthdate,
    calculate_total_minutes,
    translate_to_words
)


def test_get_birthdate():
    """Tests for valid and invalid user inputs based on YYYY-MM-DD format"""
    # Valid Dates
    assert isinstance(get_birthdate("1996-08-22"), datetime.date)
    assert isinstance(get_birthdate("2001-09-07"), datetime.date)
    assert isinstance(get_birthdate("2022-03-17"), datetime.date)

    # Invalid Dates; trigger sys.exit()
    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("invalid format")  # invalid string format
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("1996/08/22")  # invalid date separators
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("08-22-1996")  # invalid order
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("19996-08-22")  # too many year digits
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("196-08-22")  # too little year digits
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("1996-008-22")  # too many month digits
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("1996-8-22")  # too little month digits
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("1996-08-222")  # too many day digits
    assert pytest_wrap.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrap:
        get_birthdate("1996-08-2")  # too little day digits
    assert pytest_wrap.type == SystemExit


def test_calculate_total_minutes():
    """Tests the accuracy of calculate_total_minutes()"""
    today = datetime.date.today()
    assert calculate_total_minutes(today) == 0  # this should always be 0
    assert type(calculate_total_minutes(today)) == type(int())  # function returns an int


def test_translate_to_words():
    """Confirms method is correctly translating and formatting an int to english written word"""
    assert translate_to_words(22) == "Twenty-two minutes"  # valid answer
    assert translate_to_words(100) != "Two minutes"  # wrong translation
    assert translate_to_words(2) != "Two"  # missing "minutes" suffix
    assert translate_to_words(1) != "1 minutes"  # did not translate to english
