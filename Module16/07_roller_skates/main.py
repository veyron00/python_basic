skates_list = []
size_list = []
people_in_skates = 0
num_skates = int(input('Кол-во коньков: '))
for num in range(num_skates):
    size_skate = int(input(f'Размер {num + 1}-й пары: '))
    skates_list.append(size_skate)

num_people = int(input('Кол-во людей: '))
for num in range(num_people):
    leg_size = int(input(f'Размер ноги {num + 1}-го человека: '))
    size_list.append(leg_size)

for size in size_list:
    for i in range(len(skates_list)):
        if size == skates_list[i]:
            people_in_skates += 1
            skates_list.remove(skates_list[i])
            break
        elif size < skates_list[i]:
            people_in_skates += 1
            skates_list.remove(skates_list[i])
            break

print(f'Наибольшее кол-во людей, которые могут взять ролики: {people_in_skates}')

