shop = [
        ['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

part_name = input('Название детали: ')
count_parts = 0
total_cost = 0

for i in range(len(shop)):
        if part_name == shop[i][0]:
                count_parts += 1
                total_cost += shop[i][1]
print(f'Кол-во деталей — {count_parts}')
print(f'Общая стоимость — {total_cost}')


