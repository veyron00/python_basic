import random
number_sticks = int(input('Количество палок: '))
sticks_list = ['I' for _ in range(number_sticks)]
number_throws = int(input('Количество бросков: '))
left_i = 0
for num in range(1, number_throws + 1):
    print(f'Бросок {num}. ', end='')
    left_i = int(input('Сбиты палки с номера '))
    right_i = int(input('по номер '))
    for i in range(left_i, right_i + 1):
        sticks_list[i - 1] = '.'


print('Результат: ', end='')
for i in sticks_list:
    print(i, end=' ')

