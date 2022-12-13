print('Задача 9. Выражение')

#Дано число x.
#Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))
num_x = int(input('Введите число X: '))
denominator = 1
numerator = 1
for degree in range(1, 6 + 1):
    denominator *= (num_x - (2**degree))
    numerator *= (num_x - (2**degree - 1))
print(f'RES равно {numerator / denominator}')
