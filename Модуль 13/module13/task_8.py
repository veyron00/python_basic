print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def factorial_calculation(num):
  if num == 0:
    return 1
  else:
    factorial = num * (num - 1) 
    num -= 1
    while num > 1:
      factorial *= (num - 1)
      num -= 1
    return factorial

def degree_num(x, n):
  count = 1
  for num in range (1, n + 1):
    count = count * x
  return count

def sum_sequence(x, precision):
    sequence_sum = 1
    n = 0
    result = 0
    while abs(sequence_sum) > precision:
      sequence_sum = degree_num(-1, n) * (degree_num(x, (2 * n)) / factorial_calculation((2 * n)))
      result += sequence_sum
      n += 1
    return f'Сумма ряда = {result}'


precision = float(input('Введите точность: '))
x = float(input('Введите x: '))


print(sum_sequence(x, precision))