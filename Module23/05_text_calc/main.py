import pathlib
from pathlib import Path

def from_file_to_list(file_dir) -> list:
    '''Получает из файла данные и возвращает список.'''
    with open(file_dir, 'r') as file:
        list_with_expressions = list()
        for i_line in file:
            new_list = list()
            for line in i_line.split():
                new_list += [line]
            list_with_expressions += [new_list]
    return list_with_expressions


def calculating_expressions(expression):
    '''Функция подсчета полученных выражений.'''
    result = 0
    count_expr = 0

    if expression[1] == '+':
        result += int(expression[0]) + int(expression[2])
    elif expression[1] == '-':
        result += int(expression[0]) - int(expression[2])
    elif expression[1] == '*':
        result += int(expression[0]) * int(expression[2])
    elif expression[1] == '/':
        result += int(expression[0]) / int(expression[2])
    elif expression[1] == '**':
        result += int(expression[0]) ** int(expression[2])
    elif expression[1] == '//':
        result += int(expression[0]) // int(expression[2])
    elif expression[1] == '%':
        result += int(expression[0]) % int(expression[2])
    return result


def processing_expressions(list_expressions, list_result: list = []):
    '''Функция распределяет на правильные и неправильные выражения.

    Получает на вход список с выражениями и если математический оператор
    имеет не верный формат предлагает изменить на верный формат, после ввода
    обработка продолжается.'''
    count_expr = 0
    for i_list in list_expressions:

        if len(i_list[1]) == 1 or i_list[1] == '**' or i_list[1] == '//':
            list_result.append(calculating_expressions(i_list))
            count_expr += 1
        else:
            try:
                question = input(
                    'Обнаружена ошибка в строке: {0}   Хотите исправить? да/нет '
                    .format(list_expressions[count_expr][0] + ' '
                            + list_expressions[count_expr][1] + ' '
                            + list_expressions[count_expr][2])
                    .lower())
                if question == 'да':
                    new_value = input('Введите исправленную строку: ').split()
                    list_expressions[count_expr] = new_value
                    list_result.append(calculating_expressions(new_value))
                elif question == 'нет':
                    list_expressions[count_expr] = 0
                else:
                    raise ValueError

            except ValueError:
                print('Введено некорректное значение')

            count_expr += 1
    return sum(list_result)


file_name = 'calc.txt'
file_dir = Path(Path.cwd(), file_name)
list_exp = from_file_to_list(file_dir)
result = processing_expressions(list_exp)
print('Сумма результатов: {0}'.format(result))





