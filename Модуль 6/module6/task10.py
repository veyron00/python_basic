print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
computer_number = 50
print(f'Твое число равно, меньше или больше, чем число {computer_number}?')
boys_number = int(input('Ведите ваш ответ: '))
lower_value = 0
upper_value = 100
while True:
  if boys_number == 1:
    print(f'Поздравляю вы угадали, это было число {computer_number}!')
    break
  elif boys_number == 2:
    lower_value = computer_number
    computer_number = int((lower_value + upper_value) / 2)
    print(f'Твое число равно, меньше или больше, чем число {computer_number}?')
  elif boys_number == 3:
    upper_value = computer_number
    computer_number = int((lower_value + upper_value) / 2)
    print(f'Твое число равно, меньше или больше, чем число {computer_number}?')
  boys_number = int(input('Ведите ваш ответ: '))
  