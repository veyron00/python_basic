print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».
'''
# Вариант №1
time_receipt = int(input('Введите время получения: '))

if (time_receipt >= 8 and time_receipt < 10) or (time_receipt >= 11 and time_receipt < 14) or (time_receipt >= 15 and time_receipt < 18) or (time_receipt >= 19 and time_receipt < 22):
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')
'''
'''
# Вариант №2
time_receipt = int(input('Введите время получения: '))

if (time_receipt >= 10 and time_receipt < 11) or (time_receipt >= 14 and time_receipt < 15) or (time_receipt >= 18 and time_receipt < 19) or (time_receipt >= 22 and time_receipt <= 24) or (time_receipt >= 1 and time_receipt < 8):
  print('Посылку получить нельзя')
else:
  print('Можно получить посылку')
'''
# Вариант №2
time_receipt = int(input('Введите время получения: '))

if (time_receipt >= 8 and time_receipt < 22) and (time_receipt != 10 and time_receipt != 14 and time_receipt != 18):
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')