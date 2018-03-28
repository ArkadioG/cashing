"""
Presents naive solution to problem.
"""

from read_dictionary import load_words
from search import search
import time

# len() == 370101
english_dictionary = load_words()

def naive_search(letter: str, l_count: int):

    found_words = []

    for word in english_dictionary.keys():
        if str(word).count(letter) == l_count:
            found_words.append(word)

    print(f'Found {len(found_words):,d} that contains {l_count} letters {letter}.')


start = time.time()
search(naive_search)
stop = time.time()

print(f'It took {stop - start:.6f} sec.')
