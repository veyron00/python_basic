def sum_all_numbers(num):
    sum_num = 0
    while num != 0:
        sum_num += num % 10
        num //= 10
    return sum_num

def number_of_digits(num):
    num_count = 0
    while num != 0:
        num_count += 1
        num //= 10
    return num_count
number = int(input('Введите число: '))

num1 = sum_all_numbers(number)
num2 = number_of_digits(number)

print(f'Сумма чисел: {num1}')
print(f'Количество цифр в числе: {num2}')
print(f'Разность суммы и количества цифр: {num1 - num2}')




