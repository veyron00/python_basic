import logging
import functools
import datetime
from typing import Callable


def loging(func: Callable):
    """
    Декоратор логирующий ошибки возникающие в принимаемой функции,
     вносит их в файл.

    :param func: Принимаемая функция.
    :return: wrapper (Callable)
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Обертка функции. Перед запуском принимаемой функции выводит ее название
         и документацию.

        :param args: Аргументы принимаемой функции.
        :param kwargs: Аргументы принимаемой функции.
        :return: wrapper (Callable)
        """
        print('Запуск функции {0}()'.format(func.__name__))
        print('Документация к функции {0}()'.format(func.__name__))
        print(func.__doc__)
        try:
            func(*args, **kwargs)
        except TypeError:
            logging.basicConfig(filename='function_errors.log', level=logging.DEBUG)
            logging.debug('{0} в функции "{1}" произошла ошибка {2}'.
                          format(datetime.datetime.now(), func.__name__.upper(), TypeError.__name__))
        except ValueError:
            logging.basicConfig(filename='function_errors.log', level=logging.DEBUG)
            logging.debug('{0} в функции "{1}" произошла ошибка {2}'.
                          format(datetime.datetime.now(), func.__name__.upper(), ValueError.__name__))
        except AttributeError:
            logging.basicConfig(filename='function_errors.log', level=logging.DEBUG)
            logging.debug('{0} в функции "{1}" произошла ошибка {2}'.
                          format(datetime.datetime.now(), func.__name__.upper(), AttributeError.__name__))
        return func

    return wrapper


@loging
def squares_of_numbers(nums: list) -> list:
    """
    Возводит числа из полученного списка в квадрат, и добавляет в новый список.

    :param nums: Список с числами.
    :return: sqrt_nums (list)
    """
    sqrt_nums = []
    for i_num in nums:
        sqrt_nums.append(i_num ** 2)
    return sqrt_nums


@loging
def checking_words(words: list) -> list:
    """
    Проверяет слова из принимаемого списка есть ли там еще что-то кроме букв.
    Если в слове кроме букв есть цифры или другие знаки, вызывается исключение
    ValueError.

    :param words: Список со словами.
    :return: verified_words (list)
    :raise: ValueError

    """
    verified_words = []
    for i_word in words:
        if i_word.isalpha():
            verified_words.append(i_word)
        else:
            raise ValueError

    return verified_words


number = [1, 2, 3, 4, '5', 6, 7, 8, 9, '10', 11, 12, 13, 14, 15]

squares_of_numbers(number)

my_words = ['Ночь', 'улица', 'фонарь', "аптека",
            'Бессмысленный', 'и', 'тусклый', 'свет.',
            'Живи', 'еще', 'х0ть', 'четверть века', '—',
            'Все', 'будет', 'так.', 'Исхода', 'нет.',
            'Умрешь', '—', 'на4нешь', 'опять', 'сначала',
            'И', 'повторится', 'все,', 'как', 'встарь:',
            'Но4ь,', 'ледяная', 'рябь', 'канала,',
            'Аптека', 'улица', 'фонарь.']

checking_words(my_words)

checking_words(number)
