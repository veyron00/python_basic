class Unit:
    damage = 20
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def blow(self, unit):
        if unit.health <= 0:
            print('Победу одержал {}, {} погиб.'.format(self.name, unit.name))
        else:
            unit.health -= Unit.damage
            print('Удар нанес {0}, у {1} осталось {2} здоровья.'.
                  format(self.name, unit.name, unit.health))



warrior1 = Unit('Воин1', 100)
warrior2 = Unit('Воин2', 100)

warrior1.blow(warrior2)
warrior1.blow(warrior2)
warrior1.blow(warrior2)
warrior1.blow(warrior2)
warrior1.blow(warrior2)
warrior1.blow(warrior2)
