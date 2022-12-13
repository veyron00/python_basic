str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

if str_1 == str_2:
    print('Строки одинаковые.')
else:
    if len(str_1) != len(str_2):
        print('Строки имеют разную длину.')
    else:
        shift = 1
        flag = False
        for i in range(len(str_1) - 1):
            str_2 = str_2[-1] + str_2[:-1]
            if str_1 == str_2:
                print(f'Первая строка получается из второй со сдвигом {shift}.')
                flag = True
                break
            else:
                shift += 1
        if not flag:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')