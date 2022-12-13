class Property:
    """
    Класс имущество - описывает имущество.
    Args:
        worth (int) - передается стоимость имущества.
    """

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        """
        Метод расчета налога на имущество.
        :return:None
        """
        pass


class Apartment(Property):
    """
    Класс Апартаменты (квартира). Родитель : Property.
    Args:
        worth (int) - передается стоимость имущества.
    """

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налога на квартиру.
        :return: tax
        :rtype: int
        """
        tax = self.worth / 1000
        return tax


class Car(Property):
    """
    Класс Автомобиль. Родитель : Property.
    Args:
        worth (int) - передается стоимость имущества.
    """

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налога на машину.
        :return: tax
        :rtype: int
        """
        tax = self.worth / 200
        return tax


class CountryHouse(Property):
    """
    Класс Дача. Родитель : Property.
    Args:
        worth (int) - передается стоимость имущества.
    """

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налога на дачу.
        :return: tax
        :rtype: int
        """
        tax = self.worth / 500
        return tax


money = int(input('Сколько у вас денег? '))
cost_apartment = int(input('Введите стоимость квартиры: '))
cost_car = int(input('Введите стоимость машины: '))
cost_dacha = int(input('Введите стоимость дачи: '))
flat = Apartment(cost_apartment)
car = Car(cost_car)
dacha = CountryHouse(cost_dacha)
apartment_tax = flat.tax_calculation()
car_tax = car.tax_calculation()
dacha_tax = dacha.tax_calculation()
amount_taxes = apartment_tax + car_tax + dacha_tax
print('Налог на квартиру составляет - {0} $'.format(apartment_tax))
print('Налог на машину составляет - {0} $'.format(car_tax))
print('Налог на дачу составляет - {0} $'.format(dacha_tax))
print('Итого общая сумма налогов составляет - {0} $'.format(amount_taxes))
if money > amount_taxes:
    money = money - amount_taxes
    print('Ваших денег хватает чтобы полностью расчитаться по налогам.'
          '\nПосле уплаты налогов у вас останется {0} $'.format(money))
else:
    not_enough = amount_taxes - money
    print('Не хватает {0} $ для уплаты налогов за имущество.'.format(not_enough))
