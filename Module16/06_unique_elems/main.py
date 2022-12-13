first_list = []
second_list = []

for i_lst in range(3):
    num = int(input(f'Введите {i_lst  + 1}-е число для первого списка: '))
    first_list.append(num)

for i_lst in range(7):
    num = int(input(f'Введите {i_lst  + 1}-е число для второго списка: '))
    second_list.append(num)

print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')
first_list.extend(second_list)

for num in first_list:
    for num2 in range(first_list.count(num) - 1):
        first_list.remove(num)
print(f'Новый первый список с уникальными элементами: \n{first_list}')