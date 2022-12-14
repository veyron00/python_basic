print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона,
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию,
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.

# Юра задумался: может быть, её можно как-то использовать
# для нахождения максимума уже от трёх чисел?

# Напишите программу,
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.


def highest_value(num1, num2, num3):

    largest_num = int(((num1 + num2) + abs(num1 - num2)) / 2)
    largest_num2 = int(((largest_num + num3) + abs(largest_num - num3)) / 2)
    return largest_num2


first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))
third_num = float(input('Введите второе число: '))
print(highest_value(first_num, second_num, third_num))
