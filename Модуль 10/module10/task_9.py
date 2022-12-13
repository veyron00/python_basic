print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

hight = int(input('Введите высоту треугольника: '))
num = 1
for line in range(1, hight + 1):
    print('\t' * (hight - line), end='')
    for i in range(line):
        print(num, end='')
        num += 2
        print('\t' * 2, end='')
    print()