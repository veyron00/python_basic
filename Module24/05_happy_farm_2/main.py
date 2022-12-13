class Patato:
    maturity_level = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}
    def __init__(self, number: int):
        self.number = number
        self.maturity_lv = 0

    def maturation_check(self):
        '''Проверка на уровень зрелости.

        Если меньше 3 то не зрелая, если 3 то зрелая'''
        if self.maturity_lv < 3:
            return False
        else:
            return True

    def maturation(self):
        '''Повышает уровень зрелости картошки.

        Пока уровень меньше 3 то прибавляет 1.'''
        if self.maturity_lv < 3:
            self.maturity_lv += 1



    def print_info_potato(self):
        '''Выводит информацию о состоянии зрелости картофеля на экран.'''
        print('Картошка {0} сейчас {1}'.
              format(self.number, self.maturity_level[self.maturity_lv]))


class PotatoBeds:

    def __init__(self, num: int):
        self.num = [Patato(i_num) for i_num in range(1, num + 1)]

    def info_potato_maturity(self):
        '''Выводит состояние зреловсти всей картошки на грядке.'''
        for i_potato in self.num:
            i_potato.print_info_potato()

    def maturity_all_potatoes(self):
        '''Проверяет уровень зрелости всей картошки на грядке.

        Выводит соответствующее значение на экран.'''
        if not all([i_val.maturation_check() for i_val in self.num]):
            print('\nКартошка ещё не созрела!\n')
        else:
            print('\nВся картошка созрела. Можно собирать!\n')

    def growing_potatoes(self):
        '''Повышает уровень зрелости всей картошки на грядке.'''
        for i_potato in self.num:
            i_potato.maturation()

class Gardener:
    '''Класс Садовник'''
    warehouse_potatoes = list()
    def __init__(self, name, berds):
        self.name = name
        self.berds = berds

    def take_care_garden(self, berds):
        '''Ухаживает за картофелем. '''
        berds.growing_potatoes()
        print('\nПоливаем, удобряем, пропалываем картофель.')
    def info_condition_potatoes(self, berds):
        '''Выводит состояние зреловсти всей картошки на грядке.'''
        for i_potato in berds:
            i_potato.print_info_potato()
    def harvesting(self, berds):
        '''Собирает урожай.

        Проверяет созрела ли картошка если нет то выводится соответствующее
        сообщение, если созрела то собирает картошку в список warehouse_potatoes'''
        if all([i_val.maturation_check() for i_val in berds]):
            warehouse_potatoes = [i_val for i_val in berds]
            print('\nУрожай картофеля собран.')
            print('\nА вот и урожай:', end= ' ')
            for i in warehouse_potatoes:
                print('Картошка-{0}'.format(i.number), end=', ')
        else:
            print('\nКартофель еще не созрел для сбора урожая.')


potato_beds = PotatoBeds(5)
gardener = Gardener('Tito', potato_beds)
print('Садовник {0} выращивает картофель.\n'.format(gardener.name))
for i in range(4):
    gardener.info_condition_potatoes(potato_beds.num)
    gardener.harvesting(potato_beds.num)
    gardener.take_care_garden(potato_beds)




