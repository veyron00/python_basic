def calc():    
    operator = input('Выберите операцию: ')
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
        return calc()
        
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))

    if operator == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operator == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operator == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operator == '/':
        print(f'{num1} / {num2} = {num1 / num2}')

calc()