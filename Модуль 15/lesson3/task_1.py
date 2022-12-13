# Задача 1. Текстовый редактор: возвращение
# Мы продолжаем участвовать в разработке нового текстового редактора
# и делать жизнь обычных пользователей чуть лучше. В этот раз у нас стоит
# задача сделать фишку с поиском и заменой символов в выделенной
# строчке. Например, человек что-то перечислял в тексте, но ошибся и
# вместо точек с запятой использовал двоеточия. Лингвисты негодуют.
#
#
# Пользователь вводит строку S. Напишите программу, которая заменяет в
# строке все двоеточия (:) на точки с запятой (;). Также подсчитайте
# количество замен и выведите ответ на экран (и новую строку тоже).
# Для решения используйте список.
#
#
# Пример:
#
# Введите строку: гвозди:шурупы:гайки
#
# Исправленная строка: гвозди;шурупы;гайки
#
# Кол-во замен: 2




line = 'гвозди:шурупы:гайки'
line_list = list(line)
to_replacement = input('Какой символ заменить? ')
replacement = input('На какой символ заменить? ')
count_replacement = 0
count = 0
for symbol in line_list:
    count += 1
    if symbol == to_replacement:
        line_list[count - 1] = replacement
        count_replacement += 1
line2 = ''
for i in line_list:
    line2 += i
print(f'Исправленная строка: {line2}')
print(f'Кол-во замен: {count_replacement}')