import functools
from typing import Callable


def check_permission(status: str) -> Callable:
    """
    Декоратор принимающий аргумент.

    :param status: Статус пользователя
    :return: decorator (Callable)
    """
    ser_permissions = ['admin']

    def decorator(func: Callable) -> Callable:
        """
        Декоратор принимающий оборачиваемую функцию.

        :param func: Оборачиваемая функция.
        :return: wrapper (Callable)
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            """
            Функция обертка.
            Если параметр status есть в списке ser_permissions то произойдет
            вызов функции func.
            Иначе вызывается исключение PermissionError и выводит
            соответствующее сообщение.

            :param args: Параметры оборачиваемой функции.
            :param kwargs: Параметры оборачиваемой функции.
            :return: func (Callable)
            """
            if status in ser_permissions:
                return func(*args, **kwargs)
            else:
                try:
                    raise PermissionError
                except PermissionError:
                    print('PermissionError: У пользователя недостаточно прав, '
                          'чтобы выполнить функцию {}'.format(func.__name__))

        return wrapper

    return decorator


@check_permission('admin')
def delete_site() -> None:
    """
    Печатает на экран 'Добавляем комментарий'.
    
    :return: None
    """
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    """
    Печатает на экран 'Добавляем комментарий'.

    :return: None
    """
    print('Добавляем комментарий')


delete_site()
add_comment()
