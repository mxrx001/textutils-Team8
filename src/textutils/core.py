def word_count(text):
    import re
    from collections import Counter
    text = text.lower()
    words = re.split(r'\s+', text.strip())
    counts = Counter(word for word in words if word)
    return dict(counts)

def top_n(counts, n):
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]

def normalize_whitespace(text):
    import re
    return re.sub(r'\s+', ' ', text.strip())

def remove_punctuation(text):
    import string
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def count_sentences(text):
    import re
    sentences = re.findall(r'[^.!?]+[.!?]+', text)
    return len(sentences)

def normalize_unicode(text):
    import unicodedata
    return unicodedata.normalize('NFC', text)
