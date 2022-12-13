class Water:
    '''Класс Вода'''

    def __init__(self, name = 'Вода'):
        self.name =name
    def __add__(self, other):
        if not isinstance(other, (Fire, Air, Ground, Warm, Water, Frost)):
            raise TypeError('Значение должно быть класс Fire, Air, Ground, Warm, Water, Frost')
        if isinstance(other, Air):
            print('Смешались {0} и {1} получили "ШТОРМ"'.format(self.name, other.name))
        elif isinstance(other, Fire):
            print('Смешались {0} и {1} получили "ПАР"'.format(self.name, other.name))
        elif isinstance(other, Ground):
            print('Смешались {0} и {1} получили "ГРЯЗЬ"'.format(self.name, other.name))
        else:
            print(None)
    def __radd__(self, other):
        return self + other

class Fire:
    '''Класс Огонь'''

    def __init__(self, name = 'Огонь'):
        self.name = name

    def __add__(self, other):
        if not isinstance(other, (Water, Air, Ground, Warm, Fire, Frost)):
            raise TypeError('Значение должно быть класс Water, Air, Ground, Warm, Fire, Frost')
        if isinstance(other, Air):
            print('Смешались {0} и {1} получили "МОЛНИЯ"'.format(self.name, other.name))
        elif isinstance(other, Water):
            print('Смешались {0} и {1} получили "ПАР"'.format(self.name, other.name))
        elif isinstance(other, Ground):
            print('Смешались {0} и {1} получили "ЛАВА"'.format(self.name, other.name))
        else:
            print(None)
    def __radd__(self, other):
        return self + other


class Air:
    '''Класс Воздух'''

    def __init__(self, name = 'Воздух'):
        self.name = name

    def __add__(self, other):
        if not isinstance(other, (Water, Fire, Ground, Warm, Air, Frost)):
            raise TypeError('Значение должно быть класс Water, Fire, Ground, Warm, Air, Frost')
        if isinstance(other, Water):
            print('Смешались {0} и {1} получили "ШТОРМ"'.format(self.name, other.name))
        elif isinstance(other, Fire):
            print('Смешались {0} и {1} получили "МОЛНИЯ"'.format(self.name, other.name))
        elif isinstance(other, Ground):
            print('Смешались {0} и {1} получили "ПЫЛЬ"'.format(self.name, other.name))
        else:
            print(None)
    def __radd__(self, other):
        return self + other


class Ground:
    '''Класс Земля'''

    def __init__(self, name = 'Земля'):
        self.name = name

    def __radd__(self, other):
        return self + other

class Warm:
    '''Класс Тепло'''

    def __init__(self, name='Тепло'):
        self.name = name
    def __add__(self, other):
        if not isinstance(other, (Water, Fire, Ground, Warm, Frost)):
            raise TypeError('Значение должно быть класс Water, Fire, Ground, Warm, Frost')
        if isinstance(other, Water):
            print('Смешались {0} и {1} получили "ПАРНИКОВЫЙ ЭФФЕКТ"'.format(self.name, other.name))
        else:
            print(None)
    def __radd__(self, other):
        return self + other

class Frost:
    '''Класс Холод'''
    def __init__(self, name='Холод'):
        self.name = name
    def __add__(self, other):
        if not isinstance(other, (Water, Fire, Ground, Warm, Frost)) :
            raise TypeError('Значение должно быть класс Water, Fire, Ground, Warm, Frost')
        if isinstance(other, Water):
            print('Смешались {0} и {1} получили "ЛЁД"'.format(self.name, other.name))
        else:
            print(None)

    def __radd__(self, other):
        return self + other

c1, c2 = Water(), Air()
c3 = c2 + c1
c3

c4, c5 = Water(), Fire()
c6 = c5 + c4
c6

c7, c8 = Ground(), Water()
c9 = c7 + c8
c9

c10, c11 = Fire(), Air()
c12 = c10 + c11
c12

c13, c14 = Ground(), Air()
c15 = c13 + c14
c15

c16, c17 = Fire(), Ground()
c18 = c16 + c17
c18

c19, c20 = Warm(), Water()
c21 = c19 + c20
c21

c22, c23 = Frost(), Water()
c25 = c22 + c23
c25
