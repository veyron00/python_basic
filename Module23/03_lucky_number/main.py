import random
import pathlib
from pathlib import Path

def output_to_screen(file_dir):
    with open(file_dir, 'r') as file:
        print(file.read())

def clearing_file(file_dir):
    with open(file_dir, 'w') as file:
        file.seek(0)


file_dir = Path(Path.cwd(), 'out_file.txt')
count = 0
attempt_counter = 0
error_list = ['Exception', 'StopIteration', 'ArithmeticError', 'FloatingPointError',
              'OverflowError', 'ZeroDivisionError', 'AttributeError', 'FileExistsError']
try:
    while True:
        num = input('Введите число: ')
        attempt_counter += 1
        count += int(num)
        random_num = random.randint(1, 13)
        if attempt_counter == random_num:
            raise random.choice(error_list)
        with open(file_dir, 'a') as file:
            file.write(num + '\n')
        if count >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            print()
            break
except(Exception, StopIteration, ArithmeticError, FloatingPointError,
              OverflowError, ZeroDivisionError, AttributeError, FileExistsError):
    print('Вас постигла неудача!')
print('Содержимое файла out_file.txt:')
output_to_screen(file_dir)
clearing_file(file_dir)

