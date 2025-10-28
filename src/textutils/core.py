import re

def normalize_whitespace(text: str) -> str:
    if text is None:
        return ""
    collapsed = re.sub(r"\s+", " ", text)
    return collapsed.strip()