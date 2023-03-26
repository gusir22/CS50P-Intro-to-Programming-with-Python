from um import count


def test_new_line_um():
    """Tests that an 'um' will be caught at the beginning of a line"""
    assert count("um...") == 1
    assert count("um?") == 1


def test_end_line_um():
    """Tests that an 'um' will be caught at the end of a line"""
    assert count("what for um") == 1
    assert count("at the end of an um") == 1


def test_multiple_ums():
    """Tests that multiple 'um' will be caught"""
    assert count("um...whats good, um, sir?") == 2
    assert count("um... um, um?") == 3


def test_ignore_substring_ums():
    """Test that 'um' is only counted outside other words"""
    assert count("um, that's super yummy!") == 1
    assert count("umbrellas") == 0
    assert count("stupid mummy!") == 0


def test_case_sensitivity():
    """Test that 'um' are counted regardless of case type"""
    assert count("um") == 1
    assert count("uM") == 1
    assert count("Um") == 1
    assert count("UM") == 1
