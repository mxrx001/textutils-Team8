from textutils.core import word_count

def test_word_count():
    assert word_count("hello world") == {"hello": 1, "world": 1}
    assert word_count("") == {}
    assert word_count("this is a test") == {"this": 1, "is": 1, "a": 1, "test": 1}
