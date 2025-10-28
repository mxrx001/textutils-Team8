from textutils.core import normalize_unicode

def test_basic():
    # Example: accented characters composed/decomposed
    s = "é"  # composed
    s_alt = "e\u0301"  # decomposed (e + accent)
    # Both should normalize to "é"
    assert normalize_unicode(s) == "é"
    assert normalize_unicode(s_alt) == "é"

def test_non_unicode():
    assert normalize_unicode("Hello!") == "Hello!"

def test_empty():
    assert normalize_unicode("") == ""
