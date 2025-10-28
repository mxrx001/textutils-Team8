from textutils.core import top_n

def test_top_n_basic():
    counts = {"apple": 5, "banana": 3, "cherry": 5}
    top2 = top_n(counts, 2)
    assert top2 == [("apple", 5), ("cherry", 5)]  # Ties broken alphabetically

def test_top_n_empty():
    assert top_n({}, 3) == []
