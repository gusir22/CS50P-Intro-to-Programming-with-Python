from numb3rs import validate


def test_correct_ip():
    """Tests a few correct IPv4 addresses to confirm validate()'s accuracy"""
    assert validate("0.0.0.0") is True  # ip is at bottom of range
    assert validate("22.22.22.22") is True  # ip is within range
    assert validate("255.255.255.255") is True  # ip is at top of range
    assert validate("127.0.0.1") is True  # local ip


def test_incorrect_ip():
    """Tests a few incorrect IPv4 addresses to confirm validate()'s accuracy"""
    assert validate("not an ip address") is False  # ip is a str sentence
    assert validate("-2.0.0.0") is False  # negative int in ip
    assert validate("256.256.256.256") is False  # ip numbers are above range
    assert validate("275.3.6.28") is False  # invalid ip from numb3rs show
    assert validate("0.0.0") is False  # ip is missing groups
    assert validate("0.0.0.0.0") is False  # ip has too many groups
    assert validate("one.two.three.four") is False  # ip has written numbers instead of int chars
    assert validate("256.0.0.0") is False  # first byte is out of range
    assert validate("0.256.0.0") is False  # second byte is out of range
    assert validate("0.0.256.0") is False  # third byte is out of range
    assert validate("0.0.0.256") is False  # fourth byte is out of range
