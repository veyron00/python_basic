import random


class Human:
    """

    Класс Человек, описывает человека.
    Attributes:
        __name (str): Имя человека
        owner (None or class): Владелец дома
        __satiety (int): Уровень сытости
        home (class): Дом (объект дома может принадлежать нескольким людям)

    """

    def __init__(self, name, owner=None, satiety=30, happiness_level=100):
        self.__name = name
        self.__satiety = satiety
        self.owner = owner
        self.__happiness_level = happiness_level
        if owner is not None:
            self.home = owner.home
        else:
            self.home = House()

    def get_name(self):
        """
        Геттер для получения имени.
        :return: __name
        :rtype: str
        """
        return self.__name

    def get_satiety(self):
        """
        Геттер для получения уровня сытости.
        :return: __satiety
        :rtype: int
        """
        return self.__satiety

    def get_happynes_lvl(self):
        """
        Геттер для получения уровня счастья.
        :return: __happiness_level
        :rtype: int
        """
        return self.__happiness_level

    def set_satiety(self, number: int, set_satiety=False):
        """
        Сеттер для изменения уровня сытости
        :param number: число на которое необходимо изменить уровень сытости.
        :param set_satiety: Если False, то number прибавляется к  __satiety
        если Tru, то __satiety принимает значение number.
        :return:
        """
        if not set_satiety:
            if isinstance(number, int):
                if number > 0:
                    self.__satiety += number
                else:
                    if self.__satiety + number < 0:
                        self.__satiety = 0
                    else:
                        self.__satiety += number
            else:
                try:
                    raise ValueError
                except ValueError:
                    print('Передаваемое значение должно быть целым числом.')
        else:
            self.__satiety = number

    def set_happynes_level(self, number: int, set_happy=False):
        """
        Сеттер для изменения уровня счастья.
        :param number: число на которое необходимо изменить уровень счастья
        :param set_happy: Если False, то number прибавляется к  __happiness_level
        если Tru, то __happiness_level принимает значение number.
        :return:
        """
        if not set_happy:
            if isinstance(number, int):
                self.__happiness_level += number
            else:
                try:
                    raise ValueError
                except ValueError:
                    print('Передаваемое значение должно быть целым числом.')
        else:
            self.__happiness_level = number

    def to_eat(self):
        """Есть еду."""
        pass

    def buy_food(self):
        """Покупать еду."""
        pass

    def go_to_work(self):
        """Ходить на работу."""
        pass

    def play(self):
        """Играть."""
        pass

    def pet_cat(self):
        """Гладить кота."""
        pass

    def print_info(self):
        """Вывод информации на экран"""
        print('Уровень сытости у {0}  {1}, еды в холодильнике {2}, денег в сейфе {3}'.
              format(self.__name, self.__satiety, self.home.get_fridge(), self.home.get_safe()))


class House:
    """
    Класс Дом. Описывает дом.
    Attributes:
        __fridge (int): Заполненность холодильника продуктами.
        __safe (int): Количество денег в доме.
        __amount_dirt (int): Количество грязи в доме.
        __cat_food (int): Количество кошачьей еды в доме..
    """

    def __init__(self, fridge=50, safe=100, amount_dirt=0, cat_food=30):
        self.__fridge = fridge
        self.__safe = safe
        self.__amount_dirt = amount_dirt
        self.__cat_food = cat_food

    def __str__(self):
        return 'Уровень заполненности холодильника {0}' \
               '\nКоличество денег в сейфе {1}' \
               '\nКоличество грязи в доме {2}' \
               '\nКоличество еды кота {3}'.format(self.get_fridge(), self.get_safe(),
                                                  self.get_amount_dirt(), self.get_cat_food())

    def get_fridge(self):
        """
        Геттер для получения количества еды в холодильнике.
        :return: __fridge
        :rtype: int
        """
        return self.__fridge

    def get_safe(self):
        """
        Геттер для получения количества денег в доме.
        :return: __safe
        :rtype: int
        """
        return self.__safe

    def get_amount_dirt(self):
        """
        Геттер для получения количества грязи в доме.
        :return: __amount_dirt
        :rtype: int
        """
        return self.__amount_dirt

    def get_cat_food(self):
        """
        Геттер для получения количества кошачьей еды.
        :return: __cat_food
        """
        return self.__cat_food

    def meal(self, number):
        """
        Уменьшает количество еды в холодильнике.
        :param number: Параметр на который необходимо уменьшить количество
         еды в холодильнике.
        :return: number
        """
        if self.__fridge > number:
            self.__fridge -= number
            return number
        elif self.__fridge == 0:
            print('В холодильнике закончилась еда.')
            self.__fridge = self.__fridge
            return 0
        else:
            self.__fridge = 0
            return (self.__fridge - number) + number

    def restock(self, number: int):
        """
        Пополнение запасов еды в холодильнике.
        :parameter: number: Количество еду на которое необходимо пополнить
        холодильник.
        :return: None

        """
        cat_food = number // 3
        if self.__safe - (number + cat_food) > 0:
            self.__fridge += number
            self.set_cat_food(cat_food)
            self.__safe -= number + cat_food
        elif self.__safe == 0:
            self.__safe = 0
            print('В доме закончились деньги!')
        elif self.__safe < number:
            self.__fridge += self.__safe
            print('Денег хватило всего только на {0} еды для людей.'.format(self.__safe))
            self.__safe = 0
        elif self.__safe < number + cat_food:
            self.__fridge += number
            self.__safe -= number
            self.__cat_food += self.__safe
            print('Денег хватило всего лишь на {0} еды для людей и {1} для кота.'.format(number, self.__safe))
            self.__safe = 0

    def spend_money(self, amount):
        """
        Потратить деньги.
        :param amount: Сумма покупок.
        :return: True or False
        """
        if self.__safe > amount:
            self.__safe -= amount
            return True
        else:
            try:
                raise ValueError
            except ValueError:
                print('Не хватает денег на покупку.')
        return False

    def set_amount_dir(self, quantity):
        """
        Повышение либо понижение количества грязи в доме.
        Если quantity положительное число, то грязи прибавиться.
        Если quantity отрицательное число, то грязи уменьшится.
        :param quantity: +/- Количество грязи
        :return: None
        """
        if quantity >= 0:
            self.__amount_dirt += quantity

        else:
            if self.__amount_dirt + quantity < 0:
                self.__amount_dirt = 0
                print('В доме идеальная чистота.')
            else:
                self.__amount_dirt += quantity
                print('В доме прибрано.')

    def set_cat_food(self, number, set_catfood=False):
        """
        Сеттер для изменения количества еды кота.
        :param set_catfood:
        :param number: Количество еды кота которое необходимо + или -.
        :return: None
        """
        if not set_catfood and number > 0:
            self.__cat_food += number
        if not set_catfood and number < 0:
            if self.__cat_food + number < 0:
                self.__cat_food = 0
            else:
                self.__cat_food += number
        else:
            self.__cat_food = number

    def top_up_safe(self):
        """
        Пополнение сейфа деньгами в доме.
        :return: None
        """
        self.__safe += 150


class Husband(Human):
    """
    Класс Муж. Родитель Human

    """

    def __str__(self):
        """
        Строковое представление класса Husband.
        :return: ''.format
        :rtype: str

        """
        return '{0}:' \
               '\nУровень сытости {1}' \
               '\nУровень счастья {2}'.format(self.get_name(), self.get_satiety(),
                                              self.get_happynes_lvl())

    def play(self):
        """
        Играть на компьютере.
        Уровень сытости уменьшается на 10.
        Уровень счастья увеличивается на 10
        :return: None
        """
        self.set_satiety(-10)
        self.set_happynes_level(20)
        print('{0} поиграл на компьютере.'.format(self.get_name()))

    def to_eat(self, number: int):
        """
        Есть еду.
        :param number: Количество съеденной еды.
        :return: None
        """
        sat_level = self.home.meal(number)
        self.set_satiety(sat_level)
        print('{0} поел {1} еды.'.format(self.get_name(), number))

    def go_to_work(self):
        """
        Ходить на работу.
        :return: None
        """
        self.set_satiety(-10)
        self.home.top_up_safe()
        print('{0} сходил на работу, заработал денег.'.format(self.get_name()))

    def pet_cat(self):
        """
        Гладить кота.
        :return: None
        """
        print('{0} погладил кота.'.format(self.get_name()))
        self.set_happynes_level(5)  # Увеличивается уровень счастья.
        self.set_satiety(-10)  # Уменьшается уровень сытости.


class Wife(Human):
    """
    Класс Жена. Родитель Human.
    Attributes:
        __number_coats (int): Количество купленных шуб.

    """
    __number_coats = 0

    def __str__(self):
        """
        Строковое представление класса Wife.
        :return: ''.format
        :rtype: str
        """
        return '{0}:' \
               '\nУровень сытости {1}' \
               '\nУровень счастья {2}' \
               '\nКоличество купленных шуб {3}'.format(self.get_name(), self.get_satiety(),
                                                       self.get_happynes_lvl(), self.__number_coats)

    def to_eat(self, number: int):
        """
        Есть еду.
        :param number: Количество еды которое необходимо съесть.
        :return: None
        """
        sat_level = self.home.meal(number)
        self.set_satiety(sat_level)
        print('{0} поела {1} еды.'.format(self.get_name(), number))

    def buy_food(self, number):
        """
        Покупать еду.
        :param number: Количество купленной еды.
        :return: None
        :raise: Если number не целое число то вызывается исключение ValueError
        """
        if isinstance(number, int):
            self.set_satiety(-10)
            self.home.restock(number)
            print('{0} сходил в магазин.'.format(self.get_name()))
        else:
            try:
                raise ValueError
            except ValueError:
                print('Передаваемое значение должно быть целым числом.')

    def buy_coat(self):
        """
        Покупка шубы
        :return: None
        """
        if self.home.spend_money(350):
            self.set_happynes_level(60)  # Увеличивается уровень счастья
            self.set_satiety(-10)  # Уменьшается уровень сытости
            self.__number_coats += 1  # Количество шуб увеличивается.

    def cleaning(self, number):
        """
        Убираться в доме.0
        :param number: Количество грязи которое было убрано в доме.
        :return: None
        """
        print('{0} начала уборку в доме.'.format(self.get_name()))
        self.home.set_amount_dir(number)  # Уменьшается количество грязи в доме
        self.set_satiety(-10)  # Уменьшается уровень сытости

    def pet_cat(self):
        print('{0} погладила кота.'.format(self.get_name()))
        self.set_happynes_level(5)  # Увеличивается уровень счастья
        self.set_satiety(-10)  # Уменьшается уровень сытости


class Cat:
    """
    Класс Кот, описывает кота.
    Attributes:
        __name (str): Имя кота.
        owner (object(class)): Объект класса House.
        __degree_satiety (int): Степень сытости.
    """

    def __init__(self, name, owner=None, degree_satiety=30):
        self.__name = name
        self.__degree_satiety = degree_satiety
        if owner is not None:
            self.home = owner.home
        else:
            self.home = House()

    def __str__(self):
        """
        Строковое представление класса Cat.
        :return: 'Кот {0} уровень его сытости {1}'.format(self.get_name_cat(),
                                                        self.get_degree_satiety())
        :rtype: str
        """
        return 'Кот {0} уровень его сытости {1}'.format(self.get_name_cat(),
                                                        self.get_degree_satiety())

    def get_name_cat(self):
        """
        Геттер для получения имени кота.
        :return: __name
        """
        return self.__name

    def get_degree_satiety(self):
        """
        Геттер для получения степени сытости кота.
        :return: __degree_satiety
        """
        return self.__degree_satiety

    def set_degree_satiety(self, number):
        """
        Сеттер для изменения уровня сытости кота.
        :param number: Количество которое кот поел, либо потерял.
        :return: None
        """
        if number > 0:

            if self.home.get_cat_food() + number > 0:
                self.__degree_satiety += number * 2
                self.home.set_cat_food(-number)
            elif self.home.get_cat_food() <= 0:
                self.__degree_satiety = self.__degree_satiety
                self.home.set_cat_food(0, True)
            elif self.home.get_cat_food() + number < 0:
                self.home.set_cat_food(-(self.home.get_cat_food() - number + number))
                self.__degree_satiety += (self.home.get_cat_food() - number + number) * 2
                self.home.set_cat_food(0, True)

            print('Кот {0} подкрепился.'.format(self.get_name_cat()))
        elif number < 0:
            if self.__degree_satiety + number <= 0:
                self.__degree_satiety = 0
            else:
                self.__degree_satiety += number

    def sleep(self):
        """
        Кот спит.
        При каждом вызове метода уменьшается значение __degree_satiety
        на 10.

        :return: None
        """
        print('Кот {0} поспал.'.format(self.get_name_cat()))
        self.set_degree_satiety(-10)

    def rip_off_wallpaper(self):
        """
        Кот обдирает обои.
        При каждом вызове метода, увеличивается значение __amount_dir
        класса House на 5.
        Уменьшается значение __degree_satiety на 10.
        :return: None
        """
        print('Кот {} ободрал обои'.format(self.get_name_cat()))
        self.home.set_amount_dir(5)
        self.set_degree_satiety(-10)


man = Husband('Alex')
woman = Wife('Molly', man)
cat = Cat('Tom', man)

print(man)
print(woman)
print(cat)

day_count = 0
for _ in range(365):

    if man.get_satiety() > 0 and man.get_happynes_lvl() > 10:
        random_num = random.randint(1, 6)
        if random_num == 1:
            man.to_eat(number=random.randint(15, 30))
        elif random_num == 2:
            man.go_to_work()
        elif random_num == 3:
            man.play()
        elif random_num == 4:
            man.pet_cat()
        elif random_num == 5:
            man.to_eat(number=random.randint(15, 30))
        elif random_num == 6:
            man.play()
        if man.home.get_safe() < 50:
            man.go_to_work()
        if man.get_satiety() < 10:
            man.to_eat(30)

        if man.get_satiety() <= 0:
            man.set_happynes_level(0, True)
            print('{0} умер от недоедания.'.format(man.get_name()))
            # del man
        if man.get_happynes_lvl() < 10:
            man.set_satiety(0, True)
            print('{0} умер от депрессии.'.format(man.get_name()))
            # del man
        elif man.home.get_amount_dirt() > 90:
            man.set_happynes_level(-10)
    if woman.get_satiety() > 0 and woman.get_happynes_lvl() > 10:
        random_num = random.randint(1, 7)
        if random_num == 1:
            woman.buy_food(number=random.randint(60, 120))
        elif random_num == 2:
            woman.to_eat(number=random.randint(15, 30))
        elif random_num == 3:
            number = random.randint(50, 100)
            woman.cleaning(-number)
        elif random_num == 4:
            woman.pet_cat()
        elif random_num == 5:
            woman.buy_coat()
        elif random_num == 6:
            woman.to_eat(number=random.randint(15, 30))
        elif random_num == 7:
            woman.pet_cat()

        if woman.home.get_fridge() < 50:
            woman.buy_food(60)
        if woman.home.get_cat_food() < 10:
            woman.buy_food(60)
        if woman.get_satiety() < 10:
            woman.to_eat(30)
        if woman.home.get_amount_dirt() > 150:
            woman.cleaning(-100)
        if woman.get_satiety() <= 0:
            print('{0} умерла от недоедания.'.format(woman.get_name()))
            woman.set_happynes_level(0, True)
            # del man
        if woman.get_happynes_lvl() < 10:
            print('{0} умерла от депрессии.'.format(woman.get_name()))
            woman.set_satiety(0, True)
            # del man
        elif woman.home.get_amount_dirt() > 90:
            woman.set_happynes_level(-10)
    if cat.get_degree_satiety() > 0:
        random_num = random.randint(1, 5)
        if random_num == 1:
            cat.sleep()
        elif random_num == 2:
            cat.rip_off_wallpaper()
        elif random_num == 3:
            cat.set_degree_satiety(number=random.randint(5, 10))
        elif random_num == 4:
            cat.set_degree_satiety(number=random.randint(5, 10))
        elif random_num == 5:
            cat.set_degree_satiety(number=random.randint(5, 10))

    if cat.get_degree_satiety() <= 0:
        print('Кот {0} умер от недоедания.'.format(cat.get_name_cat()))

    man.home.set_amount_dir(5)

print('------------------------ИТОГИ ГОДА ЖИЗНИ------------------------')
print(man.home)
print(man)
print(woman)
print(cat)
