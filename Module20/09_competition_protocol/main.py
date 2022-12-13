protocols = int(input('Сколько записей вносится в протокол? '))
protocols_dict = dict()
print('Записи (результат и имя):')
for num in range(protocols):
    record = input('{0}-я запись: '.format(num + 1)).split()
    record[0] = int(record[0])
    record = tuple(record)
    protocols_dict[num + 1] = record

test_dict = {
    1: (69485, 'Jack'), 2: (95715, 'qwerty'), 3: (95715, 'Alex'),
    4: (83647, 'M'), 5: (197128, 'qwerty'), 6: (95715, 'Jack'),
    7: (93289, 'Alex'), 8: (95715, 'Alex'), 9: (95715, 'M')
 }


score_list = []
for i_value in protocols_dict.values():
    score_list += [i_value[0]]
place_dict = dict()
for place in range(3):
    position = score_list.index(max(score_list))
    place_dict[place + 1] = (protocols_dict[position + 1][1], protocols_dict[position + 1][0])
    score_list[position] = 0
    for key, value in protocols_dict.items():
        for key1 in place_dict[place + 1]:
            if value[1] == key1:
                score_list[key - 1] = 0

print()
print('Итоги соревнований:')
for i_key, i_value in place_dict.items():
    print('{0}-е место. {1} ({2})'.format(i_key, i_value[0], i_value[1]))






