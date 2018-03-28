
def search(search_func, count=10):
    for i in range(count):
        search_func('a', 2)
        search_func('m', 3)
        search_func('x', 1)
        search_func('e', 3)
        search_func('f', 3)


def search_more(search_func, count=10):
    for i in range(count):
        search_func('a', 2)
        search_func('m', 3)
        search_func('x', 1)
        search_func('e', 3)
        search_func('f', 3)
        search_func('c', 2)
        search_func('h', 3)
        search_func('w', 2)


def search_less(search_func, count=10):
    for i in range(count):
        search_func('c', 2)
        search_func('h', 3)
        search_func('w', 2)
        search_func('o', 4)
        search_func('i', 3)
