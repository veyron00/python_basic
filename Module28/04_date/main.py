class Date:
    """
    Класс Дата.
    Attributes:
        day: Число
        month: Месяц
        year: Год
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        """
        Строковое представление экземпляра класса.

        :return: str
        """
        return 'День: {0}  Месяц: {1}  Год: {2}'.format(self.__day, self.__month, self.__year)

    @classmethod
    def from_string(cls, day_month_year: str) -> object:
        """
        Преобразует строку в словарь по разделителю '-'
        Если строка имеет соответствующий формат
        :param day_month_year:
        :return: object
        """
        if cls.is_date_valid(day_month_year):
            date0 = day_month_year.split('-')
            return Date(int(date0[0]), int(date0[1]), int(date0[2]))
        else:
            print('Не верный формат полученной строки. '
                  '\nСтрока должна иметь вид 01-01-2030')

    @classmethod
    def is_date_valid(cls, day_month_year: str) -> bool:
        """
        Проверяет строку соответствует ли полученная строка нужному формату.

        :param day_month_year: Строка даты
        :return: bool
        """
        if day_month_year.count('-') == 2:
            date1 = day_month_year.split('-')
            if (0 < int(date1[0]) <= 31) and (len(date1[0]) == 2) and date1[0].isdigit():
                if (0 < int(date1[1]) <= 12) and (len(date1[1]) == 2) and date1[1].isdigit():
                    if (0 < int(date1[2]) <= 10000) and (len(date1[2]) == 4) and date1[2].isdigit():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    @property
    def day(self) -> int:
        """
        Геттер для получения числа.

        :return: __day
        """
        return self.__day

    @property
    def month(self) -> int:
        """
        Геттер для получения месяца.

        :return: __month
        """
        return self.__month

    @property
    def year(self) -> int:
        """
        Геттер для получения года.

        :return: __year
        """
        return self.__year

    @day.setter
    def day(self, day: int) -> None:
        """
        Сеттер для изменения числа.

        :param day:
        :return: None
        """
        self.__day = day

    @month.setter
    def month(self, month: int) -> None:
        """
        Сеттер для изменения числа.

        :param month:
        :return: None
        """
        self.__month = month

    @year.setter
    def year(self, year: int) -> None:
        """
        Сеттер для изменения числа.

        :param year:
        :return: None
        """
        self.__year = year


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('31-12-2077'))
print(Date.is_date_valid('40-12-2077'))
