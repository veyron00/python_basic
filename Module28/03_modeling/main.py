import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    @abstractmethod
    def area(self):
        """
        Абстрактный метод вычисления площади фигуры.
        :return: None
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Абстрактный метод вычисления периметра фигуры.

        :return: None
        """
        pass


class Square(Figure):
    """
    Класс Квадрат.

    Arguments:
        side: Длинна стороны квадрата.
    """

    def __init__(self, side_a: int) -> None:
        super().__init__(side_a, side_a)
        self.__side_a = side_a
        self.__side_b = self.__side_a
        self.__side_c = self.__side_a
        self.__side_d = self.__side_a

    def __str__(self) -> str:
        return 'Квадрат с длинной сторон {}'.format(self.__side_a)

    def perimeter(self) -> int or float:
        """
        Вычисляет периметр квадрата.

        :return: perimeter
        """
        perimeter = self.__side_a * 4
        return perimeter

    def area(self) -> int or float:
        """
        Вычисляет площадь квадрата.

        :return: area
        """
        area = self.__side_a ** 2
        return area

    @property
    def side_a(self) -> int:
        """
        Геттер для получения длинны стороны квадрата.

        :return: __side_a
        """
        return self.__side_a


class Triangle(Figure):
    """
    Класс Треугольник. Описывает равнобедренный треугольник..

    Arguments:
        height: Высота треугольника
        base: Основание треугольника

        __side_a : Сторона треугольника
        __side_b : Сторона треугольника
    """

    def __init__(self, height: int, base: int) -> None:
        super().__init__(height, base)
        self.__height = height
        self.__base = base
        self.__side_a = math.sqrt(height ** 2 + (base / 2) ** 2)
        self.__side_b = self.__side_a

    def __str__(self) -> str:
        """
        Строковое представление объекта класса.

        :return: str
        """
        return 'Треугольник с высотой {} и основанием {}'.format(self.height, self.base)

    @property
    def side_a(self) -> float:
        """
        Геттер для получения длинны стороны треугольника.

        :return: __side_a
        """
        return self.__side_a

    @property
    def side_b(self) -> float:
        """
        Геттер для получения длинны стороны треугольника.

        :return: __side_b
        """
        return self.__side_b

    @property
    def base(self) -> int:
        """
        Геттер для получения длинны основания.

        :return: __base
        """
        return self.__base

    @property
    def height(self) -> int:
        """
        Геттер для получения высоты.

        :return: __height
        """
        return self.__height

    def perimeter(self) -> float:
        """
        Находит периметр равнобедренного треугольника.

        :return: perimeter
        """
        perimeter = self.__side_a + self.__side_b + self.__base
        return perimeter

    def area(self) -> float:
        """
        Находит площадь равнобедренного треугольника через основание
        и высоту.

        :return: area
        """
        area = self.__base / 4 * math.sqrt(4 * self.__side_a ** 2 - self.__base ** 2)
        return area


class Pyramid(Triangle):
    """
    Класс Пирамида. Родитель(Triangle)
    """
    __pyramid = []

    def __init__(self, height: int, base: int, sides_num=4) -> None:
        super().__init__(height, base)
        self.sides_num = sides_num
        self.__pyramid = [Triangle(height, base) for _ in range(sides_num)]
        self.__pyramid += [Square(side_a=base)]

    def __str__(self) -> str:
        """
        Строковое представление пирамиды.

        :return: str
        """
        return 'Пирамида с высотой {} и основанием {}'.format(self.height, self.base)

    def area(self) -> float:
        """
        Вычисляет площадь поверхности пирамиды.

        :return: area
        """
        sides_area = [i_side.area() if isinstance(i_side, Triangle) else i_side.area() for i_side in self.__pyramid]
        area = sum(sides_area)
        return area

    @property
    def pyramid(self) -> list:
        """
        Геттер для получения списка частей пирамиды.

        :return: __pyramid
        """
        return self.__pyramid


class Cube(Square):
    """
    Класс Куб. Родитель(Square).

    __cube : Список частей куба.
    Arguments:
        SIDES_NUM : Количество сторон куба.
    """
    __cube = []
    SIDES_NUM = 6

    def __init__(self, side_a: int) -> None:
        super().__init__(side_a)
        self.__cube = [Square(side_a) for _ in range(self.SIDES_NUM)]

    def __str__(self) -> str:
        """
        Строковое представление объекта класса.

        :return: str
        """
        return f'Куб с длинной сторон {self.side_a}'

    def area(self) -> int or float:
        """
        Вычисляет площадь поверхности куба.

        :return: area
        """
        sides_area = [i_side.area() for i_side in self.__cube]
        area = sum(sides_area)
        return area

    @property
    def cube(self) -> list:
        """
        Геттер для получения списка частей куба.

        :return: __cube
        """
        return self.__cube


triangle = Triangle(5, 8)
print(triangle)
print('Площадь треугольника с высотой {} и основанием {} равна {}'.
      format(triangle.height, triangle.base, triangle.area()))

pyramid = Pyramid(height=5, base=8)
print(pyramid)
print('Площадь поверхности пирамиды с высотой {} и основанием {} равна {}'.
      format(pyramid.height, pyramid.base, pyramid.area()))
print('Высота пирамиды {}'.format(pyramid.height))

cube = Cube(2)
print(cube)
print('Площадь поверхности куба с длинной сторон {} равна {}'.format(cube.side_a, cube.area()))

