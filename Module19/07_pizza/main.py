
def counting_orders(orders):
    for i_dict in sorted(orders.keys()):
        print('{0}:'.format(i_dict))
        for y in range(len(orders[i_dict])):
            for i in sorted(orders[i_dict][y].keys()):
                print('     {0} : {1}'.format(i, orders[i_dict][y][i]))





orders1 = {'Иванов': [{'Пепперони': 3}, {'Мясная': 3}, {'Мексиканская': 2}], 'Петров': [{'Де-Люкс': 2}, {'Интересная': 5}]}
#counting_orders(orders1)

num_orders = int(input('Введите количество заказов: '))
order_name = dict()
for _ in range(num_orders):
    a = dict()
    order_dict = list()
    order = input('{0}-й заказ: '.format(_ + 1)).split(' ')
    if order[0] not in order_name:
        a[order[1]] = int(order[2])
        order_dict.append(a)
        order_name[order[0]] = order_dict
    else:
        for i in range(len(order_name[order[0]])):
            if order[1] not in order_name[order[0]][i]:
                a[order[1]] = int(order[2])
                order_name[order[0]].append(a)
                break
            else:
                for x in order_name[order[0]][i].keys():
                    order_name[order[0]][i][x] += int(order[2])
                    break
                break
    sorted(order_name)

#print(order_name)
counting_orders(order_name)

# Иванов Пепперони 1
# Петров Де-Люкс 2
# Иванов Мясная 3
# Иванов Мексиканская 2
# Иванов Пепперони 2
# Петров Интересная 5

