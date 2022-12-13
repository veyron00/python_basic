import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorated_decorator1: Callable) -> Callable:
    """
    Декоратор декоратора. Позволяет своей конструкции принимать любые
    аргументы декораторам.

    :param decorated_decorator1: Декорируемый декоратор.
    :return: dec1
    """
    def dec1(*args, **kwargs) -> Callable:
        """
        Декоратор принимающий любые аргументы принимаемого декоратора.

        :param args: Позиционные аргументы принимаемого декоратора.
        :param kwargs: Именованные аргументы принимаемого декоратора.
        :return: dec2
        """
        def dec2(func: Callable) -> Callable:
            """
            Декоратор принимающий функцию для передачи в оборачиваемый декоратор.

            :param func: Функция передаваемая в оборачиваемый декоратор.
            :return: decorated_decorator1
            """
            return decorated_decorator1(func, *args, **kwargs)

        return dec2

    return dec1


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):

    @functools.wraps(func)
    def wrapper(*fargs, **fkwargs):
        print('Переданные арги и кварги в декоратор: {}, {}'.format(args, kwargs))
        func(*fargs, **fkwargs)
        return func

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
