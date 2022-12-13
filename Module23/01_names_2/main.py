import pathlib
from pathlib import Path
import logging
import  time

def output_to_screen(file_dir):
    '''Функция вывода данных с файла на экран.
    The function of data output from a file to the screen.'''
    with open(file_dir, 'r') as file:
        count = 0
        for i_elem in file:
            count += 1
            print('{0}. {1}'.format(count, i_elem.split('\n')[0]))


def processing_file(file_dir):
    '''Функция подсчета символов в файле.
    The function of counting characters in the file.

    Принимает директорию с файлом, открывает файл, подсчитывает кол-во
    символов в каждой строке (без учета \n) если в строке меньше 3 символов,
    то выбрасывает исключение логирует его в файл и продолжает подсчет,
    и выводит на экран общее кол-во символов.
    Accepts the directory with the file, opens the file, counts the number
    characters in each line (excluding \n) if there are less than 3 characters in
    the line, then throws an exception logs it to a file and continues counting,
    and displays the total number of characters on the screen.'''
    total_number_characters = 0
    count_lines = 0

    with open(file_dir, 'r') as file:
        for i_elem in file:
            count_lines += 1
            count_letters = 0
            for i_letter in i_elem:
                if i_letter != '\n':
                    count_letters += 1
            total_number_characters += count_letters
            try:
                if count_letters < 3:
                    raise ValueError
            except ValueError:
                print('Ошибка: менее трёх символов в строке {0}.'.format(count_lines))
                logging.basicConfig(filename='errors.log',
                                    format='[%(asctime)s] [%(levelname)s] => %(message)s',
                                    level=logging.DEBUG)
                logging.debug('Ошибка: менее трёх символов в строке {0}.'.format(count_lines))
    print('Общее количество символов: {0}'.format(total_number_characters))


file_dir = Path(Path.cwd(), 'people.txt')
print('Содержимое файла people.txt:')
output_to_screen(file_dir)
print()
processing_file(file_dir)


