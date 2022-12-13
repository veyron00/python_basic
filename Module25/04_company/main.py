import random


class Person:
    """
    Класс Человек. Описывает человека.
    Attributes:
        name (str) : Передает имя человека
        surename (str) : Передает фамилию человека
        age (int) : Передает возраст человека
    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        """
        Метод выводит информацию о человеке.
        :return: ''.format(),
        :rtype: str
        """
        return 'Привет! Меня зовут {0} {1}, мне {2} лет.'. \
            format(self.__surname, self.__name, self.__age)

    def get_name(self):
        """
        Геттер для получения имени.
        :return: __name
        :rtype: str
        """
        return self.__name

    def get_surename(self):
        """
        Геттер для получения фамилии.
        :return: __surename
        :rtype: str
        """
        return self.__surname

    def get_age(self):
        """
        Геттер для получения возраста.
        :return: __age
        :rtype: int
        """
        return self.__age


class Employee(Person):
    """
    Класс Работник. Родитель Person.
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary_calculation(self):
        """Метод расчета заработной платы работника."""
        pass


class Manager(Employee):
    """
    Класс Менеджер. Родитель Employee/Person.
    Attributes:
        __salary (int): Зарплата менеджера
    """
    __salary = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def set_salary(self, number: int or float):
        """
        Сеттер для изменения зарплаты менеджера.
        Если новый параметр зарплаты больше или равно 0, то установится
        новый параметр.
        Иначе остается прежний размер.
        :return: None

        """
        if number >= 0:
            self.__salary = number
        else:
            self.__salary = self.__salary

    def salary_calculation(self):
        """
        Метод расчета зарплаты.
        :return: __salary
        :rtype: int or float
        """
        return self.__salary


class Agent(Employee):
    """
    Класс Агент. Родитель Person/Employee
    Attributes:
        __salary (int): Оклад агента
        __sales_volume (int): Объем продаж (генерируется случайное число от 100000 до 500000).
    """
    __salary = 5000
    __sales_volume = random.randint(100000, 500000)

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def set_sales_volume(self, number: int or float):
        """
        Сеттер для изменения объема продаж.
        :return: None
        Если новый параметр больше 0 то объем продаж принимает новый параметр.
        Иначе значение объема продаж не меняется.
        """
        if number >= 0:
            self.__sales_volume = number
        else:
            self.__sales_volume = self.__sales_volume

    def salary_calculation(self):
        """
        Метод расчета зарплаты.
        :return: to_receive
        :rtype: float
        """
        to_receive = round(self.__salary + (self.__sales_volume * 0.05), 2)
        return to_receive


class Worker(Employee):
    """
    Класс Рабочий. Родитель Person/Employee
    Attributes:
        __hours_worked (int): Отработанные часы.
        __bet (int): Ставка за один отработанный час.
    """
    __hours_worked = 160
    __bet = 100

    def __init__(self, name, surename, age):
        super().__init__(name, surename, age)

    def set_hours_worked(self, number: int or float):
        """
        Сеттер для изменения количества отработанный часов.
        (по умолчанию задано 160 часов, 40 часовая рабочая неделя)
        :return: None
        Если больше 8 часов (расчет производится минимум за 1 отработанный день)
        то __hours_worked принимает новый параметр.
        Иначе, остается без изменений.
        """
        if number >= 8:
            self.__hours_worked = number
        else:
            self.__hours_worked = self.__hours_worked

    def set_bet(self, number: int or float):
        """
        Сеттер для изменения ставки за 1 отработанный час.
        :return: None
        Если новое значение больше или равно 100 (минимальная ставка в час 100)
        то __bet принимает новое значение.
        Иначе остается без изменений.
        """
        if number >= 100:
            self.__bet = number
        else:
            self.__bet = self.__bet

    def salary_calculation(self):
        """
        Метод расчета зарплаты.
        :return: __salary
        :rtype (int or float)
        Расчет производится по формуле отработанные часы * ставку за час.
        """
        __salary = self.__hours_worked * self.__bet
        return __salary


def creating_employees(quantity, obj_class):
    """
    Создает экземпляры класса
    :return: employees_lst Список созданных экземпляров класса.
    :rtype: list
    """
    employees_lst = list()
    names = [
        'Алексей', 'Михаил', 'Дмитрий', 'Константин',
        'Федор', 'Иван', 'Владимир', 'Роман', 'Георгий'
    ]
    surenames = [
        'Голубев', 'Смирнов', 'Лобанов', 'Дроздов',
        'Титов', 'Фролов', 'Цой', 'Югай', 'Рыбин'
    ]

    for _ in range(quantity):
        name = random.choice(names)  # Случайное имя из списка name
        surename = random.choice(surenames)  # Случайная фамилия из списка surename
        age = random.randint(30, 60)  # Случайно сгенерированное число от 30 до 60
        employees_lst.append(obj_class(name, surename, age))
    return employees_lst


employees = creating_employees(3, Manager)
employees += creating_employees(3, Agent)
employees += creating_employees(3, Worker)
salarys = 0
for i_empl in employees:
    salarys += i_empl.salary_calculation()
    print('Сотрудник {0} {1} заработал {2} $'.
          format(i_empl.get_name(), i_empl.get_surename(), i_empl.salary_calculation()))

print('Общий фонд зарплат составляет - {0} $'.format(round(salarys, 2)))
