def smallest_divisor(num):

    for i in range(2, num + 1):
        if num % i == 0:
            break
    return  i




number = int(input('Введите число: '))
divisor = smallest_divisor(number)
print(f'Наименьший делитель, отличный от единицы: {divisor}')