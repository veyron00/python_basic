print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 
number = int(input('Введите число для вычисления: '))
factorial_sum = 0
while number != 0:
    count = number % 10
    factorial = 1
    for num in range(1, count + 1):
        factorial *= num
        
    number //= 10
    factorial_sum += factorial
print(factorial_sum)