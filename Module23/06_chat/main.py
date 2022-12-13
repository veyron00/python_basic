username_dict = dict()
for i_num in range(1, 4):
    username_dict['user' + str(i_num)] = input('Введите свое имя: ')
action = None
while action != '2':
    for key, name in username_dict.items():
        print('Для выхода из чата наберите 2.')
        action = input('Выберите действие {0}: "0"- посмотреть историю чата '
                           '\n"1"- написать сообщение в чат: '.format(name.title()))
        if action == '0':
                try:
                    with open('chat_history.txt', 'r') as file:
                        if len(file.read()) == 0:
                            raise FileNotFoundError
                        else:
                            with open('chat_history.txt', 'r') as file:
                                print(file.read())
                except FileNotFoundError:
                    print('История чата пуста.')

        elif action == '1':
            message = input('Напишите сообщение: ') + '\n'
            with open('chat_history.txt', 'a') as file:
                file.write('{0}: \n{1}'.format(name, message))

        elif action == '2':
            print('Чат завершен.')
            break
        else:
            try:
                raise ValueError
            except ValueError:
                print('В поле для действия введено не корректное значение. Вводить только 0 или 1.')

