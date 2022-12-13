import os
from typing import TextIO


class File:
    """
    Класс работы с файлами.
    Открывает, производит работу и закрывает файл.

    Attributes:
        file_name(str): Имя файла.
        file_mod(str): Режим работы с файлом.

    """

    def __init__(self, file_name: str, file_mod: str) -> None:
        self.file_name = file_name
        self.file_mod = file_mod
        print('Открытие файла.')

    def __enter__(self) -> TextIO:
        """
        Открывает файл.
        Если file_mod не является str то file_mod = 'w'.
        Если файла со значением file_name не существует то,
        создается новый файл с именем значения file_name.

        :return: file
        """
        if not isinstance(self.file_mod, str):
            self.file_mod = 'w'
            self.file = open(self.file_name, self.file_mod)
            return self.file
        elif not os.path.isfile(self.file_name):
            self.file_mod = 'w'
            self.file = open(self.file_name, self.file_mod)
            return self.file
        elif self.file_mod not in ['r', 'w', 'r+', 'w+', 'a', 'a+']:
            self.file_mod = 'w'
            self.file = open(self.file_name, self.file_mod)
        else:
            self.file = open(self.file_name, self.file_mod)
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Закрывает файл.

        :param exc_type: Тип исключения
        :param exc_val: Значение исключения
        :param exc_tb: След исключения.
        :return: None
        """
        self.file.close()
        print('Файл закрыт.')
        if exc_type:
            return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!')