from jar import Jar
import pytest


def test_init():
    # Default jar tests
    jar = Jar()
    assert jar.capacity == 12  # jar has correct default capacity
    assert jar.size == 0  # jar starts with 0 cookies everytime

    # Invalid jar capacity tests
    with pytest.raises(ValueError):
        jar = Jar(capacity="non-integer capacity")  # invalid non-integer capacity

    with pytest.raises(ValueError):
        jar = Jar(capacity=-2)  # invalid negative capacity


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)  # add six
    assert jar.size == 6  # count six
    jar.deposit(6)  # add six
    assert jar.size == 12  # count twelve

    with pytest.raises(ValueError):
        jar.deposit(6)  # added too many cookies


def test_withdraw():
    jar = Jar()
    jar.deposit(12)  # fill jar
    jar.withdraw(4)  # remove four
    assert jar.size == 8  # count eight
    jar.withdraw(6)  # remove 6
    assert jar.size == 2  # count two

    with pytest.raises(ValueError):
        jar.withdraw(3)  # removed too many cookies
