num_numbers = int(input('Кол-во чисел: '))
sequence = []
add_sequence = []
for _ in range(num_numbers):
    num = int(input('Число: '))
    sequence.append(num)
print(f'Последовательность: {sequence}')

if sequence[-2] == sequence[-1]:
    print(f'Нужно приписать чисел: {len(sequence) - 2}')
    for i in sequence[- 3::-1]:
        add_sequence.append(i)
    print(f'Сами числа: {add_sequence}')
else:
    print(f'Нужно приписать чисел: {len(sequence) - 1}')
    for i in sequence[-2::-1]:
        add_sequence.append(i)
    print(f'Сами числа: {add_sequence}')


