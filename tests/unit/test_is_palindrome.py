from textutils.core import is_palindrome

def test_palindrome_true():
    assert is_palindrome("madam")
    assert is_palindrome("A man a plan a canal Panama")
    assert is_palindrome("No lemon no melon")

def test_palindrome_false():
    assert not is_palindrome("hello")
    assert not is_palindrome("Python")

def test_palindrome_empty():
    assert is_palindrome("")
    assert is_palindrome(" ")