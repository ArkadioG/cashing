import naive, memoization, tabulation
from search import search, search_less, search_more


def main():
    print(f"{10*'-'} Standard set lookup, 7 lookups repeated")
    naive.main()
    memoization.main()
    tabulation.main()
    tabulation.tab_with_memo()
    print()

    print(f"{10*'-'} Additional 3 non-standard (not tabulated) lookups, 4 repeated")
    naive.main(search_more)
    memoization.main(search_more)
    tabulation.main(search_more)
    tabulation.tab_with_memo(search_more)
    print()

    print(f"{10*'-'} Only 1 standard lookup (tabulated), 6 repeated")
    naive.main(search_less)
    memoization.main(search_less)
    tabulation.main(search_less)
    tabulation.tab_with_memo(search_less)
    print()


if __name__ == '__main__':
    main()
