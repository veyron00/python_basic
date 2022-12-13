import functools
import time
from typing import Callable


def slowing_down(func: Callable) -> Callable:
    """
    Декоратор замедляет запуск принимаемой функции.
    :param func: Принимаемая функция
    :return: wrapper (Callable)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Функция обертка.
        :param args: Аргументы принимаемой функции.
        :param kwargs: Аргументы принимаемой функции.
        :return: func (Callable)
        """
        period = 0
        print('waiting [ ', end='')
        for _ in range(30):
            start = time.time()
            time.sleep(0.3)
            stop = time.time()
            period += stop - start
            if period <= 30:
                print('=', end='')
        print(' ]100%')
        func(*args, **kwargs)
        return func

    return wrapper


@slowing_down
def print_func(text: str) -> None:
    """
    Выводит на экран строки из принимаемого текста
    :param text: Принимаемый текст.
    :return: None
    """
    for i_word in text.split('\n'):
        time.sleep(0.9)
        print(i_word)
    time.sleep(0.9)


poem = 'Мороз и солнце; день чудесный!' \
       '\nЕще ты дремлешь, друг прелестный ' \
       '\nПора, красавица, проснись:' \
       '\nОткрой сомкнуты негой взоры' \
       '\nНавстречу северной Авроры,' \
       '\nЗвездою севера явись!'

print('Запуск функции {}().'.format(print_func.__name__))
print_func(poem)
