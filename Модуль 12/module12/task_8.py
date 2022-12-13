print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def common_divisor(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    print('Наибольший общий делитель:', x + y)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

common_divisor(num_1, num_2)

