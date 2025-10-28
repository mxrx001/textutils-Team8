def word_count(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.
    Example: "Red red BLUE" -> {"red": 2, "blue": 1}
    """
    # 1️⃣ Normalize to lowercase
    lower = text.lower()

    # 2️⃣ Split into words (on whitespace)
    words = lower.split()

    # 3️⃣ Initialize a dictionary to hold counts
    counts = {}

    # 4️⃣ Count each word
    for word in words:
        if word:  # skip empty strings
            counts[word] = counts.get(word, 0) + 1

    # 5️⃣ Return the frequency dictionary
    return counts


