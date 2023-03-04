from bank import value


def test_hello_payout():
    """Any greetings starting with 'hello' have no payout"""
    assert value("Hello, Gus") == 0
    assert value("hello to all") == 0  # test lowercase


def test_start_h_payout():
    """All greetings starting with 'h' have a $20 payout"""
    assert value("How'd you like a twenty?") == 20
    assert value("Hey, you!") == 20
    assert value("hiiiiiii!") == 20  # test lowercase


def test_non_h_payout():
    """All greetings starting with anything starting with
    an 'h' has a $100 payout"""
    assert value("What feels better than a hundred?") == 100
    assert value("I bet you would like a hundred dollar bill") == 100
    assert value("can I interest you in a benjamin?") == 100  # test lowercase


def test_no_greeting():
    """All non-greetings are penalized by granting a $100 payout"""
    assert value("") == 100
