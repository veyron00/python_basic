print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

number = int(input('Введите число: '))
num = 0
num2 = 0
for line in range(number):
  for row in range(number, 0, -1):
    if row < number - num:
      print('.', end = '')
    
    else:
      print(row, end = '')
  num += 1
  for row2 in range(1, number + 1):
    if row2 < number - num2:
      print('.', end = '')
    
    else:
      print(row2, end = '')
  num2 += 1
  print()