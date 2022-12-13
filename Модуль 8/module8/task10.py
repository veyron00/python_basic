print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
seating_arrangements = ''

for place in range(1, boys + girls + 1):
    if boys < girls / 2 or girls < boys / 2:
        print('Нет решения')
        break
    elif boys == girls:
        if place % 2 == 0:
            seating_arrangements += 'B'
        elif place % 2 != 0:
            seating_arrangements += 'G'
        
    elif boys > girls:
        num1 = boys - girls
        for past in range(num1):
            seating_arrangements += 'BGB'
        num2 = girls - num1
        for past in range(num2):
            seating_arrangements += 'BG'
        break
    elif girls > boys:
        num3 = girls - boys
        for past in range(num3):
            seating_arrangements += 'GBG'
        num4 = boys - num3
        for past in range(num4):
            seating_arrangements += 'GB'
        break
print(seating_arrangements)
