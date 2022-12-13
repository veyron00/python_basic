import datetime
import functools
import time
from typing import Callable


def create_time(cls, func: Callable, date_format: str) -> Callable:
    """
    Декоратор, замеряет время работы оборачиваемой функции и выводит
    на экран дату запуска функции в принимаемом формате даты и времени.

    :param cls: Принимаемый класс.
    :param func: Метод класса.
    :param date_format: Формат даты.
    :return: wrapper
    """
    def dt_format(date_format1: str) -> str:
        """
        Принимает формат даты в виде строки без %, и прибавляет знак % к
        каждой букве принимаемой строки.

        :param date_format1: Формат даты и времени.
        :return: str
        """
        dt_form = ''
        for i_sym in date_format1:
            if i_sym.isalpha():
                dt_form += '%' + i_sym
            else:
                dt_form += i_sym
        now1 = datetime.datetime.now()
        now2 = now1.strftime(dt_form)
        return 'Дата и время запуска: {0}'.format(now2)

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """
        Обертка функции.

        :param args: Позиционные аргументы принимаемой функции.
        :param kwargs: Именованные аргументы принимаемой функции.
        :return: result
        """
        print('Запускается "{}.{}". Дата и время запуска: {}'.
              format(cls.__name__, func.__name__, dt_format(date_format)))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        work_time = end - start
        print('Завершение "{}.{}", время работы = {}s'.
              format(cls.__name__, func.__name__, work_time))
        return result

    return wrapper


def log_methods(date_format: str) -> Callable:
    """
    Декоратор класса, декорирует каждый метод класса кроме магических.

    :param date_format: Формат даты и времени вывода.
    :return: log_dec
    """
    def log_dec(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                old_method = getattr(cls, i_method)
                decorate = create_time(cls, old_method, date_format)
                setattr(cls, i_method, decorate)
        return cls
    return log_dec


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

