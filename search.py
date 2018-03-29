
def search(search_func, count=10):
    print('Standard lookup', end=' : ')
    for i in range(count):
        search_func('a', 2)
        search_func('m', 3)
        search_func('x', 1)
        search_func('e', 3)
        search_func('f', 3)
        search_func('a', 2)  # again
        search_func('m', 3)  # again
        search_func('x', 1)  # again
        search_func('a', 2)  # again
        search_func('m', 3)  # again
        search_func('x', 1)  # again
        search_func('e', 3)  # again


def search_more(search_func, count=10):
    print('Additional lookups', end=' : ')
    for i in range(count):
        search_func('a', 2)
        search_func('m', 3)
        search_func('x', 1)
        search_func('e', 3)
        search_func('f', 3)
        search_func('c', 2)  # non-standard
        search_func('h', 3)  # non-standard
        search_func('w', 2)  # non-standard
        search_func('a', 2)  # again
        search_func('m', 3)  # again
        search_func('x', 1)  # again
        search_func('h', 3)  # again


def search_less(search_func, count=10):
    print('Less standard lookups', end=' : ')
    for i in range(count):
        search_func('a', 2)  # standard
        search_func('c', 2)
        search_func('h', 3)
        search_func('w', 2)
        search_func('o', 4)
        search_func('i', 3)
        search_func('i', 3)  # again
        search_func('a', 2)  # again standard
        search_func('w', 2)  # again
        search_func('o', 4)  # again
        search_func('i', 3)  # again
        search_func('a', 2)  # again standard
