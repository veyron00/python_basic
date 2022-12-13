class Human:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def login_search(self, username, list):
        ''' The method of searching for a similar login,

        gets a login and a list, searches through the list, if there is a similar login,
        returns the index of the list object in which a suitable login was found.
        Метод поиска похожего логина, получает логин и список,
        производит поиск по списку, если находится похожий логин
        возвращает индекс объекта списка в котором нашелся подходящий
        логин
        '''
        name = self.username
        for x in range(len(list)):
            usr = list[x]['username']
            if name.lower() == usr.lower():
                return x
                break
        else:
            print('Пользователя с таким логином не существует.')

    def del_user(self, list):

        del_index = Human.login_search(self, self.username, list)
        if del_index == None:
            pass
        else:
            del list[del_index]
            self.id = None
            self.name = None
            self.username = None
            self.email = None
            del self
            return list

    def receive_user(self, list):
        receive_index = Human.login_search(self, self.username, list)
        if receive_index == None:
            pass
        else:
            return list[receive_index]


class User(Human):
    def __init__(self, id, name, username, email):
        Human.__init__(self, id, name, username, email)
        pass


user_data = []
user = User(1, 'qwerty1', 'qwerty001', 'asd@qwerty.com')
# print(user.name)
print(user_data)
user.add_user(user_data)
# print(user_data)
user2 = User(2, 'qwerty2', 'qwerty002', 'asd@qwerty.com')
# user2.add_user(user_data)
# print(user_data)
user3 = User(3, 'Nikolas', 'Nicopa', 'goose@qwerty.com')

# print(user_data)
# print(user3.name)
user.del_user(user_data)
print(user_data)
# print(user.name)
print(user.receive_user(user_data))