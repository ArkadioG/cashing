"""
Presents memoization solution to problem.
"""

from read_dictionary import load_words
from search import search
from time import time

# len() == 370101
english_dictionary = load_words()

memo = {}


def memoization_search(letter: str, l_count: int):
    """
    Uses memoization to cash elements
    :param letter: Letter to find in word
    :param l_count: Number of occurences of letter in the word
    """
    global memo
    found_words = []

    search_key = f'{letter}{l_count}'

    # check in cache
    if search_key in memo.keys():
        found_words = memo[search_key]

    else:
        for word in english_dictionary.keys():
            if word.count(letter) == l_count:
                found_words.append(word)

        # memorize data into the cache
        memo[search_key] = found_words

    # print(f'Found {len(found_words):,d} that contains {l_count} letters {letter}.')
    return found_words

def main(search_type=search):
    start = time()
    search_type(memoization_search)
    stop = time()
    print(f'MEMOIZATION - It took {stop - start:.6f} sec.')


if __name__ == '__main__':
    main()
