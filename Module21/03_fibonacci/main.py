def fibonachchi(num):
    if num ==1 and num <= 2:
        return 1
    elif num <=0:
        return 0
    else:
        return fibonachchi(num - 1) + fibonachchi(num - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
fib_num = fibonachchi(number)
print('Число: {0}'.format(fib_num))
