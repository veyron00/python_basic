print('Задача 5. Простые числа')

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.
num_quantity = int(input('Введите кол-во чисел: '))
natural_numbers = 0
for num in range(num_quantity):
    number = int(input('Введите число: '))
    count = 0
    for num2 in range(1, number + 1):
        
        if number % num2 == 0:
            count += 1
    if count == 2:    
        natural_numbers += 1
                
print('Количество простых чисел в последовательности:', natural_numbers)