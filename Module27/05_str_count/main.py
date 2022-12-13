import functools
from typing import Callable


def counter(func: Callable):
    """
    Декоратор, считает количество вызовов принимаемой функции и выводит
    сообщение на экран.

    :param func: Принимаемая функция.
    :return: wrapper (Callable)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Обертка функции.

        :param args: Аргументы принимаемой функции
        :param kwargs: Аргументы принимаемой функции
        :return: func (Callable)
        """
        wrapper.count += 1
        print('Вызывается {0}, количество вызовов {1}.'.
              format(func.__name__, wrapper.count))
        func(*args, **kwargs)
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def squares_of_numbers(nums: list[int]) -> list:
    """
    Возводит числа из получаемого списка в квадрат и добавляет в новый список.

    :param nums: Список с числами.
    :return: sqrt_nums (list)
    """
    sqrt_nums = []
    for i_num in nums:
        sqrt_nums.append(i_num ** 2)
    return sqrt_nums


my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

squares_of_numbers(my_number)
squares_of_numbers(my_number)
squares_of_numbers(my_number)
squares_of_numbers(my_number)
squares_of_numbers(my_number)
squares_of_numbers(my_number)
print('Результат вычислений функции {0} - {1}'.
      format(squares_of_numbers.__name__, squares_of_numbers(my_number)))
