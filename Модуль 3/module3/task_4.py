print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

cathet_a = int(input('Введите катет а: '))
cathet_b = int(input('Введите катет b: '))
s = (cathet_a * cathet_b) / 2
print('Площадь треугольника равна -', s, 'см3.')
