def test_normalize_whitespace_removes_extra_spaces():
    text = "  a   b \n  c  "
    assert normalize_whitespace(text) == "a b c"


