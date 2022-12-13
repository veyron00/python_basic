import random


def func_1(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y
    except ZeroDivisionError:
        print('Деление на ноль. Функция 1.')

def func_2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)

        return y / x
    except ZeroDivisionError:
        print('Деление на ноль. Функция 2.')



with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        res1 = func_1(int(nums_list[0]), int(nums_list[1]))

        res2 = func_2(int(nums_list[0]), int(nums_list[1]))

        number = random.randint(0, 100)
        with open('result.txt', 'a') as file2:
            my_list = sorted([str(res1), str(res2), str(number)])
            file2.write(' '.join(my_list) + '\n')





