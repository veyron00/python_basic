contacts = dict()
while True:
    print('Введите номер действия:')
    print('1. Добавить контакт  \n2. Найти человека')
    action = int(input('=> '))
    if action == 1:
        full_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
        if full_name in contacts:
            print('Такой контакт уже существует.')
            print('Текущий словарь контактов: {0}'.format(contacts))
            continue
        else:
            telephone = int(input('Введите номер телефона: '))
            contacts[full_name] = telephone
            print('Текущий словарь контактов: {0}'.format(contacts))


    elif action == 2:
        surname = input('Введите фамилию для поиска: ').title()
        count_surname = 0
        for i_key, i_value in contacts.items():
            if surname == i_key[1]:
                count_surname += 1
                print(i_key[0], i_key[1], i_value)

        if count_surname == 0:
            print('Контакта с такой фамилией не существует.')

    elif type(action) != int or action != 1 or action != 2:
        print('Введено не правильное действие!')
