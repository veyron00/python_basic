from collections.abc import Iterable


def find_func(find_num: int, list_1: list, list_2: list) -> Iterable[int]:
    """
    Функция генератор находит заданное число, перемножением значений
    2-x списков.
    :param find_num: Искомое число.
    :param list_1: Список для перемножения его значений.
    :param list_2: Список для перемножения его значений.
    :return: x, y, result
    """
    result = 0
    while result != find_num:
        for x in list_1:
            for y in list_2:
                result = x * y
                yield x, y, result
                if result == find_num:
                    print('Found!!!')
                    return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

print('Результат сгенерированных значений:')
for i in find_func(to_find, list_1, list_2):  # Перебор сгенерированных значений.
    print('{0} * {1} = {2}'.format(i[0], i[1], i[2]))
