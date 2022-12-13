import math


class Car:
    """
    Класс Автомобиль, описывает автомобиль.
    Attributes:
        __point_x (int): Координаты точки х
        __point_y (int): Координаты точки у
        __angle (int): Угол движения (направление движения
    """

    def __init__(self, point_x=0, point_y=0, angle=0):
        self.__point_x = point_x
        self.__point_y = point_y
        self.__angle = angle

    def get_coordinates(self):
        """
        Геттер для получения текущих координат точек х и у.
        :return: (__point_x, __point_y)
        :rtype: tuple
        """
        return self.__point_x, self.__point_y

    def get_angle(self):
        """
        Геттер для получения текущего угла (направления).
        :return: __angle
        :rtype: int
        """
        return self.__angle

    def move(self, distance: int or float):
        """
        Метод перемещения объекта класса.
        Расчитывается по формуле: x2 = sinɑ * distance +x1; y2 = cosɑ * distance + y1
        :param distance: Расстояние которое необходимо проехать.
        :return: None
        """
        self.__point_x = math.sin(self.__angle * 0.017) * distance + self.__point_x
        self.__point_y = math.cos(self.__angle * 0.017) * distance + self.__point_y

    def change_direction(self, new_angle: int or float):
        """

        Изменяет угол направления движения.
        :param new_angle: Новый угол направления.
        :return: None
        Если значение нового угла в диапазоне от 0 до 360 то __angle принимает
        новое значение.
        :raise : ValueError
        Иначе вызывается исключение ValueError.
        """
        if new_angle >= 0 or new_angle <= 360:
            self.__angle = new_angle
        else:
            try:
                raise ValueError
            except ValueError:
                print('Угол должен быть от 0 до 360.')


class Bus(Car):
    """
    Класс Автобус. Родитель Car.
    Attributes:
        __passengers (int): Количество пассажиров на борту (по умолчанию 0)
        __money (int): Сумма заработанных денег (по умолчанию 0)
        __bus_brand (str): Марка автобуса (по умолчанию MAN)
    """

    def __init__(self,
                 point_x=0, point_y=0, angle=0, passengers=0, money=0, bus_brand='MAN'):
        super().__init__(point_x, point_y, angle)
        self.__passengers = passengers
        self.__money = money
        self.__bus_brand = bus_brand

    def __str__(self):
        """
        Метод строкового представления объекта класса.
        :return: '.format
        :rtype: str
        """
        return 'Автобус - {0}, на борту {1} пассажиров, заработано денег {2}.'. \
            format(self.__bus_brand, self.__passengers, self.__money)

    def get_passengers(self):
        """
        Геттер для получения количества пассажиров на борту
        :return: __passengers
        :rtype: int
        """
        return self.__passengers

    def get_money(self):
        """
        Геттер для получения количества заработанных денег.
        :return: __money
        :rtype: int
        """
        return self.__money

    def get_bus_brand(self):
        """
        Геттер для получения марки автобуса.
        :return: __bus_brand
        :rtype: str
        """
        return self.__bus_brand

    def loading_passengers(self, passengers: int):
        """
        Метод посадки пассажиров на борт.
        :param passengers: Количество пассажиров на посадку.
        :return: None
        Если число пассажиров положительное, то значение __passengers увеличится
        на количество passengers.
        :raise: Исключение ValueError.
        Иначе вызывается исключение ValueError с соответствующим сообщением.
        """
        if passengers >= 0:
            self.__passengers += passengers
            print('Зашло {0} пассажиров.'.format(passengers))
        else:
            try:
                raise ValueError
            except ValueError:
                print('Неверное значение. Значение должно быть больше или равно 0.')

    def unloading_passengers(self, passengers: int):
        """
        Метод высадки пассажиров.
        :param passengers: Количество пассажиров на высадку.
        :return: None
        Если пассажиров в автобусе нет то ничего не происходит.
        :raise: Исключение ValueError
        Если пассажиров на высадку больше чем пассажиров в автобусе то
        вызывается исключение ValueError, и выводится сообщение. Количество
        пассажиров в автобусе не меняется.
        Если введено корректное значение то, количество пассажиров в автобусе
        уменьшится на заданное количество.
        :raise: Исключение ValueError
        Иначе вызывается исключение ValueError, и выводится сообщение.
        """
        if self.__passengers == 0:
            pass
        elif self.__passengers - passengers < 0:
            try:
                raise ValueError
            except ValueError:
                print('Значение не может быть больше числа пассажиров на борту,'
                      'в автобусе {0} человек.'.format(self.__passengers))
        elif passengers >= 0 and self.__passengers - passengers > 0:
            self.__passengers -= passengers
            print('Вышло {0} пассажиров.'.format(passengers))
        else:
            try:
                raise ValueError
            except ValueError:
                print('Неверное значение. Значение должно быть больше или равно 0.')

    def move(self, distance: int or float):
        """
        Метод перемещения объекта класса.
        :param distance: Дистанция на которую необходимо переместиться.
        :return: None
        Если количество пассажиров больше 0 то значение __money увеличится.
        Расчет происходит по формуле:
        деньги = (количество пассажиров * пройденную дистанцию) * тариф
        (по умолчанию тариф = 1, менять нельзя)
        """
        super().move(distance)
        if self.__passengers > 0:
            self.__money = (self.__passengers * distance) * 1
        print('Проехали {0} км.'.format(distance))


bus1 = Bus()
bus1.loading_passengers(20)
bus1.move(10)
print(bus1)
bus1.unloading_passengers(10)
bus1.loading_passengers(35)
bus1.move(50)
print(bus1)
bus1.unloading_passengers(45)
print(bus1)
print(bus1.get_coordinates())
bus1.change_direction(30)
print(bus1.get_angle())
bus1.move(20)
print(bus1.get_coordinates())
