print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
debtor_name = input('Введите Ваше имя: ')
amount_debt = int(input('Введите сумму долга: '))
repayment_amount = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
while repayment_amount < amount_debt:
  print(f'Маловато, {debtor_name} Давайте ещё раз.')
  repayment_amount = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
print('Отлично, Василий! Вы погасили долг. Спасибо!')
  
