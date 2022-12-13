# Задача 2. Соседи
# Дана строка S и номер позиции символа в строке. Напишите программу,
# которая выводит соседей этого символа и сообщение о количестве таких
# же символов среди этих соседей: их нет, есть ровно один или есть два
# таких же.
#
# Пример 1:
# Введите строку: abbc
#
# Номер символа: 3
#
# Символ слева: b
#
# Символ справа: c
#
# Есть ровно один такой же символ.
#
# Пример 2:
# Введите строку: abсd
#
# Номер символа: 3
#
# Символ слева: b
#
# Символ справа: d
#
# Таких же символов нет.

def adjacent_characters(string1, i_symbol):
    string_list = list(string1)
    if i_symbol >= 2 and i_symbol < len(string_list):
        print(f'Символ слева: {string_list[i_symbol - 2]}')
        print(f'Символ справа: {string_list[i_symbol]}')
    elif i_symbol >= len(string_list):
        print('Нет символов!')
    elif i_symbol == len(string_list) and len(string_list) == 2:
        print(f'Символ слева: {string_list[i_symbol - 2]}')
        print(f'Символ справа: нет символа')
    elif i_symbol == 1 and len(string_list) == 2:
        print(f'Символ слева: нет символа')
        print(f'Символ справа: {string_list[i_symbol]}')
    count_similar = 0
    for i in string_list:
        if string_list[i_symbol - 1] == i:
            count_similar += 1

    if count_similar == 2:
        print('Есть ровно один такой же символ.')
    else:
        print('Таких же символов нет.')

line = input('Введите строку: ')
symbol_index = int(input('Номер символа: '))

adjacent_characters(line, symbol_index)