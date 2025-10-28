def word_count(text: str) -> dict:
    import re
    from collections import Counter
    text = text.lower()
    words = re.split(r'\s+', text.strip())
    counts = Counter(word for word in words if word)
    return dict(counts)

def top_n(counts, n):
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:n]

def normalize_whitespace(text):
    import re
    return re.sub(r'\s+', ' ', text).strip()

import string
def remove_punctuation(text):
    import string
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def count_sentences(text):
    import re
    # This pattern matches a sentence ending with one or more . ! ?
    sentences = re.findall(r'[^.!?]+[.!?]+', text)
    return len(sentences)