people_num = int(input('Кол-во человек: '))
retiring = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {retiring}-й человек')
list_people = []
list_people.extend(list(range(1, people_num + 1)))
count = 0
start = 0
print(f'Текущий круг людей: {list_people}')
print(f'Начало счёта с номера {list_people[start]}')
while len(list_people) != 1:
    for i in range(len(list_people)):
        count += 1
        if count % retiring == 0:
            print(f'Выбывает человек под номером {list_people[i]}')
            list_people.remove(list_people[i])
            if i < len(list_people):
                start = i
            else:
                start = 0
            print(f'Текущий круг людей: {list_people}')
            print(f'Начало счёта с номера {list_people[start]}')

