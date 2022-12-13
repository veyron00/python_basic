import functools
from typing import Callable, Optional

app = dict()


def callback(_func: Optional = None, *, parameter: str) -> Callable:
    """
    Декоратор обратного вызова.

    :param _func: Необязательный параметр функция.
    :param parameter: Параметр маршрута.
    :return: to_dict (Callable)
    """

    def to_dict(func):
        """
        Декоратор принимающий функцию для обертывания.

        :param func: Оборачиваемая функция.
        :return: wrapper (Callable)
        """
        app[parameter] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Функция обертка.

            :param args: Параметр оборачиваемой функции.
            :param kwargs: Параметр оборачиваемой функции.
            :return: func (Callable)
            """
            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return to_dict
    return to_dict(_func)


@callback(parameter='//')
def example() -> str:
    """
    Просто функция для примера.
    Выводит 'Пример функции, которая возвращает ответ сервера'.

    :return: str
    """
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


print(example.__doc__)
print(callback.__doc__)
