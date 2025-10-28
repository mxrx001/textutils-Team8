from textutils.core import normalize_whitespace

def test_normalize_simple():
    assert normalize_whitespace("  a   b   ") == "a b"
    assert normalize_whitespace("hello     world") == "hello world"
    assert normalize_whitespace("\tfoo\nbar  baz\t") == "foo bar baz"
    assert normalize_whitespace("") == ""

def test_normalize_no_change():
    assert normalize_whitespace("abc def") == "abc def"
