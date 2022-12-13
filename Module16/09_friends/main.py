num_friends = int(input('Кол-во друзей: '))
promissory_notes = int(input('Долговых расписок: '))
list_debts = []
for i in range(num_friends):
    list_debts.append(0)


for note in range(promissory_notes):
    print(f'{note + 1}-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    list_debts[to_whom - 1] += how_many
    list_debts[from_whom -1] -= how_many

print('Баланс друзей:')
for i_friend in range(num_friends):
    print(f'{i_friend + 1}: {list_debts[i_friend]}')





