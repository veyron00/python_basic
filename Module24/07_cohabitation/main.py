import random
class Human:

    def __init__(self, name, owner=None, satiety=50):
        self.name = name
        self.satiety = satiety
        self.owner = owner
        if owner != None:
            self.home = owner.home
        else:
            self.home = House()
    def to_eat(self):
        self.home.meal()
        self.satiety += 10
        print('{0} поел.'.format(self.name))
    def buy_food(self):
        self.home.restock()
        print('{0} сходил в магазин.'.format(self.name))
    def go_to_work(self):
        self.home.top_up_safe()
        print('{0} сходил на работу.'.format(self.name))
    def play(self):
        self.satiety -= 10
        print('{0} поиграл.'.format(self.name))
    def print_info(self):
        print('Уровень сытости у {0}  {1}, еды в холодильнике {2}, денег в сейфе {3}'.
              format(self.name, self.satiety, self.home.fridge, self.home.safe))
class House:
    def __init__(self, fridge=50, safe=0):
        self.fridge = fridge
        self.safe = safe

    def meal(self):
        if self.fridge >10:
            self.fridge -= 10
        elif self.fridge == 0:
            self.fridge = 0

    def restock(self):
        self.fridge += 20
        if self.safe > 20:
            self.safe -= 20
        elif self.safe == 0:
            self.safe = 0

    def top_up_safe(self):
        self.safe += 30

man = Human('Alex')
woman = Human('Molly', man)


for _ in range(365):
    value_of_cube = random.randint(1, 6)
    if man.satiety < 0:
        print('Голодовка {0} не пошла на пользу!'.format(man.name))
        del(man)
    elif man.satiety < 20:
        man.to_eat()
    elif man.home.fridge < 10:
        man.buy_food()
    elif man.home.safe < 50:
        man.go_to_work()
    elif value_of_cube == 1:
        man.go_to_work()
    elif value_of_cube == 2:
        man.to_eat()
    else:
        man.play()

    value_of_cube = random.randint(1, 6)
    if woman.satiety < 0:
        print('Голодовка {0} не пошла на пользу!'.format(man.name))
        del (woman)
    elif woman.satiety < 20:
        woman.to_eat()
    elif woman.home.fridge < 10:
        woman.buy_food()
    elif woman.home.safe < 50:
        woman.go_to_work()
    elif value_of_cube == 1:
        woman.go_to_work()
    elif value_of_cube == 2:
        woman.to_eat()
    else:
        woman.play()
man.print_info()
woman.print_info()
