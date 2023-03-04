from plates import is_valid


def test_plate_starts_with_two_letters():
    """Tests that the plate starts with two letters only"""
    assert is_valid("ab12") is True  # starts with two letters
    assert is_valid("ba21") is True  # starts with two letters
    assert is_valid("12ab") is False  # starts with two numbers
    assert is_valid("a1b2") is False  # starts with letter and a number


def test_plate_char_len_minimum():
    """Tests that the char length in a plate is no less than 2"""
    assert is_valid("a") is False  # len 1
    assert is_valid("ab") is True  # len 2
    assert is_valid("abc") is True  # len 3
    assert is_valid("abcd") is True  # len 4


def test_plate_char_len_maximum():
    """Tests that the char length in a plate is no more than 6"""
    assert is_valid("abc") is True  # len 3
    assert is_valid("abcd") is True  # len 4
    assert is_valid("abcde") is True  # len 5
    assert is_valid("abcdef") is True  # len 6
    assert is_valid("abcdefg") is False  # len 7
    assert is_valid("abcdefgh") is False  # len 8


def test_plate_alphanumeric():
    """Tests that plate is simply alphanumeric"""
    assert is_valid("abc123") is True  # alphanumeric 1
    assert is_valid("cba321") is True  # alphanumeric 2
    assert is_valid("ab12!@") is False  # non-alphanumeric


def test_no_numbers_or_letters():
    """Tests that plates can be valid when without a number sequence"""
    assert is_valid("nonum") is True  # no number sequence 1
    assert is_valid("noseq") is True  # no number sequence 2
    assert is_valid("123456") is False  # no letter sequence 1
    assert is_valid("123") is False  # no letter sequence 2


def test_no_chars_after_number_sequence_begins():
    """Tests that plates do NOT contain a char after a number sequence begins"""
    assert is_valid("abc123") is True  # no chars after sequence begins 1
    assert is_valid("def456") is True  # no chars after sequence begins 2
    assert is_valid("ab12c3") is False  # chars after sequence begins 1
    assert is_valid("de45f6") is False  # chars after sequence begins 2


def test_number_sequence_does_not_start_with_zero():
    """Tests that plate number sequences do not begin with 0"""
    assert is_valid("abc123") is True  # non-zero starting number sequence 1
    assert is_valid("def456") is True  # non-zero starting number sequence 2
    assert is_valid("abc012") is False  # zero starting number sequence
