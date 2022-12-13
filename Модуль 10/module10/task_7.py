print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

num_quantity = int(input('Введи количество цифр: '))
sum_count = 0
sum_number = 0
num1 = 0
for num in range(num_quantity):
    number = int(input('Введите натуральное число: '))
    
    if number > num1:
        num1 = number
    while number > 0:
        count = number % 10
        sum_count += count
        number //= 10
    
    if sum_count > sum_number:
        sum_number = sum_count
        sum_count = 0
    else:
        sum_number = sum_number
        sum_count = 0
    
print(f'Наибольшее по сумме цифр число {num1}, сумма его цифр {sum_number}')