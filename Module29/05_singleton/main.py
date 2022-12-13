from typing import Callable


def singleton(cls) -> Callable:
    """
    Декоратор класса позволяющий создавать только один экземпляр класса.

    :param cls: Оборачиваемый класс.
    :return: wrapper
    """
    def wrapper():
        """
        Обертка класса. Возвращает инстанс класса.

        :return: cls
        """
        return cls

    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()
my_another_obj0 = Example()

print(id(my_obj))
print(id(my_another_obj))
print(id(my_another_obj0))

print(my_obj is my_another_obj)
