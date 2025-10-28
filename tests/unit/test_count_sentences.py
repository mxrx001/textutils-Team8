from textutils.core import count_sentences

def test_basic():
    assert count_sentences("Hello. Goodbye!") == 2
    assert count_sentences("We won. Did you see? Wow!") == 3

def test_no_sentence():
    assert count_sentences("") == 0
    assert count_sentences("Just a phrase") == 0

def test_edge():
    assert count_sentences("Hello... How are you??!") == 2
