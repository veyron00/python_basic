print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

envelope_a = 12
envelope_b = 12
letter_a = int(input('введите длинну стороны А: '))
letter_b = int(input('введите длинну стороны B: '))
count = 0
for quantity in range(letter_a // envelope_a + 1):
    if letter_a > envelope_a and letter_b > envelope_b:
        letter_a /= 2
        letter_b /= 2
        count += 2
    elif letter_a <= envelope_a and letter_b <= envelope_b:
        print(f'Письмо помещается')
        print(f'Письмо сложили {count} раз.')
        break