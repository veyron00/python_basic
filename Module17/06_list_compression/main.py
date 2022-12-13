import random
number_digits = int(input('Количество чисел в списке: '))
uncompressed_list = [random.randint(0, 2) for _ in range(number_digits)]
print(f'Список до сжатия: {uncompressed_list}')
compressed_list = [num for num in uncompressed_list if num > 0]
print(f'Список после сжатия: {compressed_list}')