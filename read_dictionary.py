import json
import os


def load_words() -> dict:
    """
    Reads dictionary form json file.
    :return: Dict with words from dictionary: {word: 1}
    """
    try:
        filename = os.path.join(os.getcwd(), "words_dictionary.json")
        with open(filename) as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except FileNotFoundError as e:
        print("Dictionary file not found.", e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print(english_words["fate"])
