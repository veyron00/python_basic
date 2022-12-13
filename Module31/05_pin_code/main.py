import itertools


def pin_combinations(num_digits: int) -> None:
    """
    Находит все возможные варианты комбинаций цифр от 0 до 9, с длинной
    принимаемого аргумента. Выводит на экран все полученные варианты.

    :param num_digits: Количество цифр в последовательности чисел.
    :return: None
    """
    pin_codes = [i_pin for i_pin in itertools.permutations(range(10), num_digits)]
    nums = 1  # Счетчик комбинаций
    for i_pin in pin_codes:
        print('{}. - {}'.format(nums, i_pin))
        nums += 1


pin_combinations(4)