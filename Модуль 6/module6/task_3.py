print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.
 
# Напишите программу,
# которая считала бы для него,
# сколько десятичных цифр (знаков) во вводимом числе.

input_number = int(input('Введите число: '))
digit_counter = 0
while input_number != 0:
  input_number = input_number // 10
  digit_counter += 1
print(f'Введенное число состоит из {digit_counter} цифр.')


