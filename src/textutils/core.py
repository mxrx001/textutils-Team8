def word_count(text: str) -> dict:
    import re
    from collections import Counter

    text = text.lower()
    words = re.split(r'\s+', text.strip())
    counts = Counter(word for word in words if word)

    return dict(counts)
