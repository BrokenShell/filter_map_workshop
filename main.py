""" Introduction to map and filter - contrived examples """


def add_one(n: int) -> int:
    """ Transformer to be used with map """
    return n + 1


def is_odd(n: int) -> bool:
    """ Predicate for use with filter """
    return n % 2 != 0


if __name__ == '__main__':
    print("\noriginal array")
    arr = list(range(10))
    print(arr)

    print("\nmapped array (add_one)")
    print(list(map(add_one, arr)))

    print("\nfiltered array (is_odd)")
    print(list(filter(is_odd, arr)))
