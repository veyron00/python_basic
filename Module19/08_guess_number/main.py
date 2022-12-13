import random
max_num = int(input('Введите максимальное число: '))
num_list = set()
hidden_num = random.randint(0, max_num)
lst_with_hidd_num = None
last_list_num = None
dif_set = None
while num_list != 'Помогите!':
    num_list = input('Нужное число есть среди вот этих чисел: ')
    if num_list == 'Помогите!':
        dif_set = lst_with_hidd_num - last_list_num
        print('Артём мог загадать следующие числа: ', end=' ')
        for i in dif_set:
            print(i, end=' ')
        break

    else:
        num_list = num_list.split()
        num_list = {int(num) for num in num_list}
    if hidden_num in num_list:
        lst_with_hidd_num = num_list
        print('Ответ Артёма: Да')
    else:
        print('Ответ Артёма: Нет')
        last_list_num = num_list

