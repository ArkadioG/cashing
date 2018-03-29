"""
Presents naive solution to problem.
"""

from read_dictionary import load_words
from search import search
from time import time

# len() == 370101
english_dictionary = load_words()


def naive_search(letter: str, l_count: int):
    found_words = []

    for word in english_dictionary.keys():
        if str(word).count(letter) == l_count:
            found_words.append(word)
    # print(f'Found {len(found_words):,d} that contains {l_count} letters {letter}.')
    return found_words


def main(search_type=search):
    start = time()
    search_type(naive_search)
    stop = time()

    print(f'NAIVE - It took {stop - start:.6f} sec.')


if __name__ == '__main__':
    main()
