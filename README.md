# textutils-Team8
Team 8 - Python for Data Science, Term 1

Small Python package for text utilities — group assignment.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/mxrx001/textutils-Team8.git
    cd textutils-Team8
    ```

2. **Create the environment (with micromamba):**
    ```
    micromamba create -f environment.yml -y
    micromamba activate textutils
    ```

3. **Install the package in editable mode:**
    ```
    pip install -e .
    ```

## Running Tests

**To run all tests:**
```
pytest
```
**To see a coverage report:**
```
pytest --cov=src/textutils --cov-report=term-missing
```

## Features

- `word_count(text)` — case-insensitive word counts
- `top_n(counts, n)` — top-N frequent words (alphabetical for ties)
- `normalize_whitespace(text)` — collapses whitespace, trims ends
- `remove_punctuation(text)` — strips punctuation, keeps spaces/letters
- `is_palindrome(text)` — palindrome check (ignore case and spaces)
- `count_sentences(text)` — counts sentences by punctuation
- `normalize_unicode(text)` — standardizes Unicode form

## Team 8 - Python for Data Science, Term 1

- Mohamed Aymen Elmezouari
- Amat Montoto
- Ferdinand Rasmussen
- Mara Rusen
- Abhay Mathahalli
