class Parent:
    '''Класс родителя / Parent class'''
    verified_list = []
    def __init__(self, name, age, childrens):
        self.name =name
        self.age = age
        for i in childrens: # проверка на корректность возраста ребенка
            if i[1] + 16 <= self.age:
                self.verified_list.append(i)
            else:
               print('Возраст ребенка {0} слишком большой, разница между '
                     'родителем и ребенком должна быть минимум 16 лет.'.format(i[0]))
        self.childrens = [Children(i[0], i[1]) for i in self.verified_list]

    def print_info(self):
        '''Вывод информации о родителе на экран.
        Displaying information about the parent on the screen'''
        print('Привет! Меня зовут {0} мне {1} лет, у меня {2} детей.'
              .format(self.name, self.age, len(self.verified_list)))
    def comfort_child(self):
        '''Понижает уровень спокойствия ребенка.
        Lowers the level of calmness of the child'''
        for i_child in self.childrens:
            i_child.lowering_level_calm()
    def feed_baby(self):
        '''Понижает уровень голода ребенка.
        Lowers the child's hunger level.'''
        for i_child in self.childrens:
            i_child.lowering_level_hunger()

    def checking_level_calm(self):
        '''Проверка и вывод на экран текущего уровня спокойствия ребенка.
        Checking and displaying the current level of calmness of the child'''
        for i_child in self.childrens:
            print('Состояние {0} - {1}'.format(i_child.name, i_child.level_calm[i_child.calm_lv]))

    def checking_hunger_level(self):
        '''Проверка и вывод на экран текущего уровня сытости ребенка.
        Checking and displaying the current level of satiety of the child'''
        for i_child in self.childrens:
            print('Состояние {0} - {1}'.format(i_child.name, i_child.hunger_level[i_child.hunger_lv]))

    def raise_appetite(self):
        '''Повышает аппетит ребенку / Increases the child's appetite'''
        for i_child in self.childrens:
            i_child.increasing_hunger_levels()

    def cheer_up(self):
        '''Поднимает настроение ребенку / Lifts the mood of the child'''
        for i_child in self.childrens:
            i_child.increasing_level_calm()

class Children:
    '''Класс Ребенок / Class Child'''
    level_calm = {0: 'Спокойный', 1: 'Игривый', 2: 'Легко раздраженный', 3: 'Капризный'}
    hunger_level = {0: 'Сытый', 1: 'Умеренно сытый', 2: 'Слегка голодный', 3: 'Голодный'}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_lv = 0 # Уровень состояния спокойствия
        self.hunger_lv = 0 # Уровень состояния голода
    def lowering_level_calm(self):
        '''Понижает уровень беспокойства / Lowers the level of anxiety'''
        if self.calm_lv == 0:
            self.calm_lv = 0
        else:
            self.calm_lv -= 1

    def increasing_level_calm(self):
        '''Повышает уровень беспокойства / Increases the level of anxiety.'''
        if self.calm_lv == 3:
            self.calm_lv = 3
        else:
            self.calm_lv += 1

    def lowering_level_hunger(self):
        '''Понижает уровень голода / Lowers the level of hunger'''
        if self.hunger_lv == 0:
            self.hunger_lv = 0
        else:
            self.hunger_lv -= 1

    def increasing_hunger_levels(self):
        '''Повышает уровень голода / Increases the level of hunger'''
        if self.hunger_lv == 3:
            self.hunger_lv = 3
        else:
            self.hunger_lv += 1




children_list = [('Alex', 30), ('John', 7), ('Margy', 12)]
parent1 = Parent('Nick', 45, children_list)

print(parent1.childrens[0].name)
print(parent1.childrens[0].age)
print(parent1.childrens[0].hunger_lv)
parent1.print_info()
parent1.checking_level_calm()
parent1.checking_hunger_level()
parent1.raise_appetite()
parent1.cheer_up()
parent1.checking_level_calm()
parent1.checking_hunger_level()
parent1.raise_appetite()
parent1.cheer_up()
parent1.checking_level_calm()
parent1.checking_hunger_level()
parent1.raise_appetite()
parent1.cheer_up()
parent1.checking_level_calm()
parent1.checking_hunger_level()
parent1.comfort_child()
parent1.feed_baby()
parent1.checking_level_calm()
parent1.checking_hunger_level()
