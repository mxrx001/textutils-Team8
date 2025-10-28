def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """
    Return the top n (word, count) pairs sorted by:
      1) highest count (desc),
      2) word (asc) for ties.

    - If n > number of items, return all.
    - If n <= 0 or counts is empty, return [].
    """
    if not counts or n <= 0:
        return []

    # sort by count desc, then word asc
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    return items if n >= len(items) else items[:n]
    