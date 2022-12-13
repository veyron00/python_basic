def calculating_math_func(data, factorial_dict):

    result = 1
    if data in factorial_dict:
        result = factorial_dict[data]
        result /= data ** 3
        result = result ** 10
        return result
    else:
        while len(factorial_dict) != data:
            for index in range(1, data + 1):
                # Добавил проверку, если значение есть в словаре то повторное вычисление не происходит
                if index in factorial_dict:
                    continue
                else:
                    result *= index
                    factorial_dict[index] = result

        result /= data ** 3
        result = result ** 10
        return result

factorial_dict = dict()
while True:
    num = int(input('Введите число: '))
    print(calculating_math_func(num, factorial_dict))
    print(factorial_dict)


