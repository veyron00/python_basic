print('Задача 1. Конвертация')


# При покупках за рубежом 
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, 
# если купить что-то в евро, 
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
# 
# Напишите программу, 
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
# 
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

money = float(input('Введите стоимость покупки в Евро: '))
usd = 1.25
rub = 60.87
change_money = money * usd * rub
print(f'Сумма в рублях Вашей покупки составляет {change_money} руб.')