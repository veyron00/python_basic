import math

class Circle:
    '''Класс Круг.'''
    def __init__(self, r,  x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def calculating_area(self):
        '''Функция расчета площади круга.'''
        area = round(math.pi * (self.r ** 2), 2)
        return 'Площадь круга равна {0}'.format(area)
    def perimeter_calculation(self):
        '''Функция расчета длинны периметра круга.'''

        perimeter = round(2 * math.pi * self.r, 2)
        return 'Периметр круга равен {0}'.format(perimeter)

    def expanding_circle(self, multiplicity):
        '''Функция увеличения радиуса круга.'''

        self.r = round(self.r * multiplicity, 2)

    def intersection_circles(self, point):
        '''Функция проверки пересекаются ли окружности экземпляров класса.'''

        dist_between_points = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        if self.r + point.r > dist_between_points:
            return 'Окружности пересекаются.'
        else:
            return 'Окружности не пересекаются'

circle1 = Circle(5, -4, 3)
circle2 = Circle(3, 2, -5)
print(circle1.calculating_area())
print(circle2.calculating_area())
print(circle1.perimeter_calculation())
print(circle2.perimeter_calculation())
print(circle1.intersection_circles(circle2))
print('Увеличиваем размер круга в 2 раза.')
circle2.expanding_circle(2)
print(circle2.calculating_area())
print(circle1.intersection_circles(circle2))
