from working import convert, parse_time
import pytest


def test_correct_convert():
    """Tests correct inputs for conversions to ensure accuracy of convert() method"""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"  # convert hours and meridiem to 24-h
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"  # convert hours, minutes, and meridiem to 24-h
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"  # convert different hours and meridiem to 24-h
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"  # convert different hours, minutes, and meridiem to 24-h


def test_incorrect_convert():
    """Tests incorrect inputs for conversions to ensure accuracy of convert() method"""
    with pytest.raises(ValueError):  # lower case meridians cause ValueError
        convert("9 am to 5 am")

    with pytest.raises(ValueError):  # dash separation instead of "to" cause ValueError, short format
        convert("9 - 5")

    with pytest.raises(ValueError):  # dash separation instead of "to" cause ValueError, full format
        convert("09:00 AM - 05:00 PM")

    with pytest.raises(ValueError):  # incorrect times cause ValueError
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):  # omitting "to" cause ValueError
        convert("9:00 AM 5:00 PM")

    with pytest.raises(ValueError):  # incorrect spacing on input causes ValueError
        convert("9AM to 5PM")  # incorrect meridiem spacing

    with pytest.raises(ValueError):  # incorrect spacing on input causes ValueError
        convert("9AMto5PM")  # no spacing

    assert convert("9 AM to 5 PM") is not "10:00 to 16:00"  # catches hour off by one +-
    assert convert("9:00 AM to 5:30 PM") is not "09:05 to 17:25"  # catches minutes off by five +-
