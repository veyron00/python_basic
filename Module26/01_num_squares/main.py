from collections.abc import Iterable


class SquaresOfNumbers:
    """
    Класс квадратов чисел.
    __count (int): Начало последовательности увеличивающаяся с каждой
    итерацией.
    :parameter: num конечное число последовательности.
    """
    __count = 0

    def __init__(self, num: int) -> None:
        self.num = num

    def __iter__(self):
        """
        Создает итератор.
        :return: self
        """
        return self

    def __next__(self) -> Iterable[int]:
        """
        Переходит к следующему элементу итератора.
        :return: self.__count ** 2
        """
        if self.__count < self.num:
            self.__count += 1
            return self.__count ** 2
        else:
            raise StopIteration


def gen_squares_numbers(num: int) -> Iterable[int]:
    """
    Функция генератор квадратов чисел.
    :param num: Окончание последовательности квадратов чисел.
    :return: start ** 2
    """
    start = 1
    while start <= num:
        yield start ** 2
        start += 1


number = int(input('Введите число конец последовательности: '))
nums = SquaresOfNumbers(number)
print('Реализация через класс итератор.')
print('Последовательность квадратов чисел от 1 до {0}  - '.format(number), end='')
for i in nums:
    print('{0}'.format(i), end=', ')

print('\nРеализация через функцию генератор.')
num_gen = gen_squares_numbers(number)
print('Последовательность квадратов чисел от 1 до {0}  - '.format(number), end='')
for i_num in num_gen:
    print('{0}'.format(i_num), end=', ')

print('\nРеализация через генераторное выражение.')
generator_expression = [i_num ** 2 for i_num in range(1, number + 1)]
print('Последовательность квадратов чисел от 1 до {0}  - '.format(number), end='')
for i_elem in generator_expression:
    print('{0}'.format(i_elem), end=', ')
