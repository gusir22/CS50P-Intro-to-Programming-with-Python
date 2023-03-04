from twttr import shorten


def test_only_numbers():
    """All numbers should be unaffected"""
    for i in range(10):
        assert shorten(str(i)) == str(i)


def test_only_symbols():
    """All symbols should be unaffected"""
    symbols = "!@#$%^&*()-_=+[]{};:,<.>/?`~'\""
    for s in symbols:
        assert shorten(s) == s


def test_words():
    """All vowels should disappear. A dict of word full and shortened pairs are used
    to confirm all vowels get removed"""
    word_pairs = {
        "cat":"ct",
        "egg":"gg",
        "ice":"c",
        "ore":"r",
        "urn":"rn"
    }
    for key in word_pairs:
        assert shorten(key) == word_pairs[key]  # test in lowercase
        assert shorten(key.upper()) == word_pairs[key].upper()  # test in uppercase
