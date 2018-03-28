"""
Presents tabulation solution to problem.
"""

from read_dictionary import load_words
from search import search
import time

# len() == 370101
english_dictionary = load_words()

tabs = {}

def build_tabs():
    cases = {'a': 2, 'm': 3, 'x': 1, 'e': 3, 'f': 3}

    for letter, count in cases.items():
        case_key = f'{letter}{count}'
        words = []
        for word in english_dictionary:
            if word.count(letter) == count:
                words.append(word)

        tabs[case_key] = words


def tabulation_search(letter: str, l_count: int):
    """
    Uses memoization to cash elements
    :param letter: Letter to find in word
    :param l_count: Number of occurences of letter in the word
    """
    found_words = []

    search_key = f'{letter}{l_count}'

    if search_key in tabs.keys():
        found_words = tabs[search_key]

    else:
        for word in english_dictionary.keys():
            if word.count(letter) == l_count:
                found_words.append(word)

        # tabs[search_key] = found_words

    print(f'Found {len(found_words):,d} that contains {l_count} letters {letter}.')
    return found_words


start = time.time()
build_tabs()
search(tabulation_search)
stop = time.time()

print(f'It took {stop - start:.6f} sec.')
