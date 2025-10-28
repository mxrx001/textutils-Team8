def test_top_n_order_and_ties():
       counts = {"a": 2, "b": 2, "c": 1}
       assert c.top_n(counts, 2) == [("a", 2), ("b", 2)]



