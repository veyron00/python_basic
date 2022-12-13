guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
action = ''
while action != 'Пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    action = input('Гость пришёл или ушёл? ')
    if len(guests) < 6 and action == 'пришел':
        visitor = input('Имя гостя: ')
        print(f'Привет, {visitor}!')
        guests.append(visitor)
    elif len(guests) >= 6 and action == 'пришел':
        visitor = input('Имя гостя: ')
        print(f'Прости, {visitor}, но мест нет.')
    elif action == 'ушел':
        visitor = input('Имя гостя: ')
        if visitor in guests:
            guests.remove(visitor)
            print(f'Пока, {visitor}!')
        else:
            print(f'Гостя по имени {visitor} нет')
print('Вечеринка закончилась, все легли спать.')