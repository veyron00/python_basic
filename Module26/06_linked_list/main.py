from typing import Any


class LinkedList:
    """
    Класс Связанный список.
    __count(int): Счетчик итераций, используется при вызове метода __next__
    Arguments:
        args: Значения добавляемые при создании экземпляра класса.
    """
    __count = -1

    def __init__(self, *args) -> None:
        self.args = []

    def __iter__(self):
        """
        Возвращает итератор объекта.
        :return: self
        """
        return self

    def __next__(self) -> Any:
        """
        Перебирает итератор объекта по элементам.
        :return: self.args[self.__count]
        """
        self.__count += 1
        if self.__count <= len(self.args) - 1:

            return self.args[self.__count]
        else:
            raise StopIteration

    def __str__(self) -> str:
        """
        Строковое представление объекта класса.
        :return: str
        """
        return '{}'.format(self.args)

    def append(self, element: Any) -> None:
        """
        Добавляет элемент к экземпляру класса.
        :param element: Добавляемый элемент.
        :return: None
        """
        self.args += [element]

    def get(self, index: int):
        """
        Предоставляет доступ к элементу объекта класса по индексу.
        :param index: индекс элемента экземпляра класса.
        :return: self.args[index] Возвращает элемент экземпляра класса
        находящийся по заданному индексу.
        :raise: IndexError
        Если индекс больше чем элементов в экземпляре класса то, вызывается
        исключение IndexError.
        Сообщение: Индекс списка вне диапазона. List index out of range
        """
        if index <= len(self.args) - 1:
            return self.args[index]
        else:
            try:
                raise IndexError
            except IndexError:
                print('Индекс списка вне диапазона. List index out of range')

    def remove(self, index: int) -> None:
        """
        Удаляет элемент по заданному индексу.
        :param index: Индекс удаляемого элемента.
        :return: None
        :raise ValueError
        Если индекс больше чем элементов в экземпляре класса то, вызывается
        исключение IndexError.
        Сообщение: self.args.remove(x): x нет в self.args. self.args.remove(x): x
        not in self.args
        """
        if index <= len(self.args) - 1:
            self.args.__delitem__(index)
        else:
            try:
                raise ValueError
            except ValueError:
                print('self.args.remove(x): x нет в self.args. self.args.remove(x): x not in self.args')


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

for i in my_list:
    print(i)
