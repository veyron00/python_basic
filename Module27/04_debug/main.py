import functools
from typing import Callable


def debug(func: Callable) -> Callable:
    """
    Декоратор выводит на экран название полученной функции, а также
    имена и значения ее атрибутов.

    :param func: Принимаемая функция
    :return: wrapper(Callable)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Функция обертка.

        :param args: Атрибуты принимаемой функции.
        :param kwargs: Атрибуты принимаемой функции.
        :return: func(Callable)
        """
        if args:
            print('Вызывается {0}("{1}")'
                  '\n"{0}" вернула значение "{2}"'.
                  format(func.__name__,
                         args[0], func(*args, **kwargs)))
            print(func(*args, **kwargs))
            return func, '\n'
        elif args and kwargs:
            print('Вызывается {0}("{1}", {2}={3})'
                  '\n"{0}" вернула значение "{4}"'.
                  format(func.__name__,
                         args[0], kwargs.keys(), kwargs.values(), func(*args, **kwargs)))
            print(func(*args, **kwargs))
            return func, '\n'
        elif kwargs:
            print('Вызывается {0}({1}="{2}", {3}={4})'
                  '\n"{0}" вернула значение "{5}"'.
                  format(func.__name__,
                         [(key, value) for key, value in kwargs.items()][0][0],
                         [(key, value) for key, value in kwargs.items()][0][1],
                         [(key, value) for key, value in kwargs.items()][1][0],
                         [(key, value) for key, value in kwargs.items()][1][1],
                         func(*args, **kwargs)))
            print(func(*args, **kwargs))
            return func, '\n'

    return wrapper


@debug
def greeting(name: str, age: int = None) -> str:
    """
    В зависимости от полученных атрибутов, функция выводит разные
    сообщения.

    :param name: Имя
    :param age: Возраст
    :return: str
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
print()
greeting("Миша", age=100)
print()
greeting(name="Катя", age=16)
