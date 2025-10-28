from textutils.core import remove_punctuation

def test_remove_basic():
    assert remove_punctuation("Hello, world!") == "Hello world"
    assert remove_punctuation("Hi... I'm Miba!") == "Hi Im Miba"

def test_remove_edge():
    assert remove_punctuation("123 ? !") == "123  "
    assert remove_punctuation("") == ""
