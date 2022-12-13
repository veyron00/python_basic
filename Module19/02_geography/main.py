countrys = int(input('Количество стран: '))
countrys_list = []
countrys_dict = dict()
for i_country in range(1, countrys + 1):
    countrys_list = input('{0} страна: '.format(i_country)).split()
    countrys_dict.update({countrys_list[i_list] : countrys_list[0] for i_list in range(1, len(countrys_list))})


for i_city in range(1, 4):
    city = input('{0}-й город: '.format(i_city))
    #for i in countrys_dict.keys():
    if city in countrys_dict.keys():
        print('Город {0} расположен в стране {1}.'.format(city, countrys_dict[city]))
    else:
        print('По городу {0} данных нет.'.format(city))


