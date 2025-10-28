def top_n(counts, n):
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:n]
