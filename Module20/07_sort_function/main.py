def tpl_sort(unsorted_tuple: tuple) -> tuple:
    sorted_tuple = tuple()
    for num in unsorted_tuple:
        if type(num) != int:
            return unsorted_tuple
    return tuple(sorted(unsorted_tuple))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

