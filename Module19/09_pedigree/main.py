def substitution(num):
    if num == 0:
        return num + 1
    else:
        return num - 1

people_quantity = int(input('Введите количество человек: '))
genealogical_dict = dict()
for _ in range(people_quantity - 1):
    couple = input('{0} пара: '.format(_+1)).split()
    if len(genealogical_dict) <= 0:
        for i_name in range(len(couple)):
            genealogical_dict[couple[i_name]] = substitution(i_name)
    else:
        for i_name in range(len(couple)):
            if couple[i_name] in genealogical_dict:
                pass
            else:
                genealogical_dict[couple[i_name]] = genealogical_dict[couple[1]] + 1



print('«Высота» каждого члена семьи:')
for i in sorted(genealogical_dict.keys()):
    print('{0}  {1}'.format(i, genealogical_dict[i]))
