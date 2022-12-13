def flips_number(num):
    integer_number = int(num)
    fractional_part = num % 1 * 1000
    revers_num1 = 0
    revers_num2 = 0
    revers_num3 = 0
    while integer_number > 0:
        revers_num1 = revers_num1 * 10 + (integer_number % 10)
        integer_number //= 10
    while fractional_part > 0:
        revers_num2 = round(revers_num2 * 10 + (fractional_part % 10))
        fractional_part //= 10

    while revers_num2 >= 1:
        revers_num3 = (revers_num3 + (revers_num2 % 10)) / 10
        revers_num2 //= 10
    return revers_num1 + revers_num3
number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

num1 = flips_number(number1)
num2 = flips_number(number2)
print(f'Первое число наоборот: {num1}')
print(f'Второе число наоборот: {num2}')
print(f'Сумма: {num1 + num2}')
