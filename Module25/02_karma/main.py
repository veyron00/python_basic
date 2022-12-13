import logging
from random import randint


class KillError(Exception):
    """Класс Убийства. Родитель: Exception"""
    pass


class DrunkError(Exception):
    """Класс Пьяного. Родитель: Exception"""
    pass


class CarCrashError(Exception):
    """Класс Автомобильная авария. Родитель: Exception"""
    pass


class GluttonyError(Exception):
    """Класс Обжорства. Родитель: Exception"""
    pass


class DepressionError(Exception):
    """Класс Депрессия. Родитель: Exception"""
    pass


def one_day():
    """
    Возвращает случайно сгенерированные очки карты число от 1 до 7.
    :return: point_day
    :rtype: int
    :raise: Если в error_probability генерируется число 10 то вызывается
    случайное исключение из списка exceptions, и происходит запись лога
    в karma.log.
    """
    exceptions = [
        KillError, DrunkError, CarCrashError, GluttonyError, DepressionError
    ]
    error_probability = randint(1, 10)
    point_day = randint(1, 7)
    if error_probability != 10:
        return point_day
    else:
        point_day = 0
        error_index = randint(0, 4)
        try:
            raise exceptions[error_index]
        except(KillError, DrunkError, CarCrashError, GluttonyError, DepressionError):
            print('Произошла ошибка {0}'.format(exceptions[error_index]))
            logging.basicConfig(filename='karma.log', level=logging.DEBUG)
            logging.debug('Произошла ошибка {0}'.format(exceptions[error_index]))
        return point_day


CARMA = 500
carma_score = 0
day_counter = 0
while carma_score < CARMA:
    if isinstance(one_day(), int):
        print(carma_score)
        carma_score += one_day()
    else:
        continue
    day_counter += 1

print('Вы набрали {0} очков кармы, и достигли просветления за {1} дней'.
      format(carma_score, day_counter))
