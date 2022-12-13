class MyDict(dict):
    """Класс Мой словарь. Родитель: dict."""

    def __init__(self):
        super().__init__()

    def get(self, key):
        """
        Возвращает значение ключа словаря
        :param key:
        :return: self[key] или 0
        Если полученный ключ есть в словаре то возвращается его значение,
        если же такого ключа в словаре нет то возвращается 0.
        """
        if key in self:
            return self[key]
        else:
            return 0


dict1 = MyDict()
dict1[1] = 22
dict1[2] = 44
print('Получаем значение ключа 1 словаря dict1 - {0}'.format(dict1.get(1)))  # Возвращает 22
print('Получаем значение ключа 2 словаря dict1 - {0}'.format(dict1.get(2)))  # Возвращает 44
print('Получаем значение ключа 3 словаря dict1 - {0}'.format(dict1.get(3)))  # Возвращает 0, т.к такого ключа в
# словаре, нет.
