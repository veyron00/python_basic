print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
num1 = int(input('Введите начальное число: '))
num2 = int(input('Введите конечное число: '))
sum_num = 0 # the sum of the numbers of multiples of 3
num_count = 0 # counter of multiples of 3
for number in range(num1, num2 + 1):
  if number % 3 == 0:
    sum_num += number
    num_count += 1
      
arithmetic_mean = int(sum_num / num_count) # calculation of the arithmetic mean
print(f'Среднее арифметическое всех чисел даипазона {num1}-{num2} равно {arithmetic_mean}')    
