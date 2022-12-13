class MyMath:
    """
    Класс Математических вычислений.
    Attributes:
        PI - константа (число Пи)
    """
    PI = 3.14

    @classmethod
    def circle_length(cls, radius: float) -> float:
        """
        Метод расчета длинны окружности.

        :param radius: Радиус окружности
        :return: 2 * MyMath.PI * radius
        """
        return 2 * MyMath.PI * radius

    @classmethod
    def circle_area(cls, radius: float) -> float:
        """
        Расчитывает площадь окружности.

        :param radius: Радиус окружности
        :return: MyMath.PI * radius ** 2
        """
        return MyMath.PI * radius ** 2

    @classmethod
    def cube_volume(cls, side: float) -> float:
        """
        Расчитывает объем куба по длинне стороны.

        :param side: Длинна стороны.
        :return: side ** 3
        """
        return side ** 3

    @classmethod
    def sphere_area(cls, radius: float) -> float:
        """
        Расчитывает площадь сферы.
        :param radius: Радиус окружности сферы.
        :return: 4 * MyMath.PI * radius ** 2
        """
        return 4 * MyMath.PI * radius ** 2


circle1 = MyMath.circle_area(radius=5)
print('Длинна окружности - {}'.format(circle1))
circle2 = MyMath.circle_area(radius=6)
print('Площадь окружности  - {}'.format(circle2))
cube = MyMath.cube_volume(side=10)
print('Объем куба - {}'.format(cube))
