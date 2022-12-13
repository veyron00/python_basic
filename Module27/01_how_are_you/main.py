import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, перед запуском полученной функцией выводит сообщение.

    :param func: Получаемая функция.
    :return: wrapper
    """
    @functools.wraps(func)
    def wrapper():
        """
        Обертка функции.

        :return: func
        """
        question = input('Как дела? ')
        if question:
            print('А у меня не очень! Ладно, держи свою функцию.')
            func()
        return func

    return wrapper


@how_are_you
def test() -> None:
    """
    Тестовая функция, выводит просто сообщение.
    <Тут что-то происходит...>

    :return: None
    """
    print('<Тут что-то происходит...>')


test()
print('\nДокументация к функции {}()'.format(test.__name__))
print(test.__doc__)