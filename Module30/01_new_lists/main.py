from typing import List
from functools import reduce

if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    print('Возводим числа из списка floats в третью степень и округляем до 3 знаков после запятой, с помощью функции '
          'map().')
    new_floats: List[float] = list(map(lambda x: round(x**3, 3), floats))
    print('Список new_floats: {}\n'.format(new_floats))
    print('Создаем список имен с длинной больше или равно 5 знакам, из списка names, с помощью функции filter().')
    new_names: List[str] = list(filter(lambda x: len(x) >= 5, names))
    print('Список new_names: {}\n'.format(new_names))
    print('Перемножаем значения списка numbers между собой с помощью функции reduce().')
    new_numbers: int = reduce(lambda x, y: x*y, numbers)
    print('Значение new_numbers: {}\n'.format(new_numbers))

