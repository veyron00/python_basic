import os

def dir_search(new_file: str, file_name: str, dirs: str, new_folder = None) -> str:
    '''Функция поиска директории, где находится файл text.txt

     возвращает эту же директорию для создания нового файла.'''
    if os.path.exists(dirs):
        for i_folder in os.listdir(dirs):
            new_folder = dirs + os.path.sep + i_folder
            if i_folder == file_name:
                return dirs
            elif os.path.isdir(new_folder):
                result = dir_search(new_file, file_name, new_folder)
                if result:
                    break

        else:
            result = None
        return result
    else:
        print('Директории с таким файлом не существует.')


def find_file(directory: str, file_name: str, result: str=str())-> str:
    ''' Функция поиска файла по названию в заданной директории.'''
    if os.path.exists(directory):
        new_folder = None
        for i_folder in os.listdir(directory):
            new_folder = directory + os.path.sep + i_folder
            if i_folder == file_name:
                return new_folder
            if os.path.isdir(directory + os.path.sep + i_folder):
                result = find_file(new_folder, file_name)
                if result:
                    break
        else:
            result = None
        return result
    else:
        print('Директории не существует.')


file_name = 'text2.txt' # Название файла с которого считываем данные
search_directory = 'D:\SKILLBOX' # Начальная директория для поиска файлов
file1_dir = find_file(search_directory, file_name) # Директория для открытия файла с которого считываем данные
file_name2 = 'analysis.txt' # Название файла который создаем и записывает обработанные данные
file2_dir = dir_search(file_name2, file_name, search_directory) + '\\' + file_name2 # Директория в которой создаем новый файл

with open(file1_dir, 'r') as file:
    text = file.read().lower() # Считанные данные присваиваем в эту переменную

text_dict = dict() # Словарь для внесения в него количества каждой буквы
text_len = '' # Переменная для подсчета количества букв, без пробелов и знаков препинания
for i_letter in text:
    if i_letter.isalpha():
        text_len += i_letter # Mamamylaramu
        text_dict[i_letter] = text.count(i_letter) # {'m': 4, 'a': 4, 'y': 1, 'l': 1, 'r': 1, 'u': 1}

frequency_of_letters = dict() # Словарь с частотностью букв в процентах
for key, value in sorted(text_dict.items()):
    frequency_of_letters[key] = round(value / (len(text_len) / 100) / 100, 3) # Вычисление частотности в процентах

sorted_list = sorted(sorted(frequency_of_letters.items()), key=lambda lst: lst[1], reverse=True)
# Сортируем данные согласно заданию "Буквы с равной долей должны следовать в алфавитном порядке."
# [('a', 0.333), ('m', 0.333), ('l', 0.083), ('r', 0.083), ('u', 0.083), ('y', 0.083)]

for i_val in sorted_list:
    with open(file2_dir, 'a') as file: # Создаем новый файл
        file.write(i_val[0] + ' ' + str(i_val[1]) + '\n') # Вносим данные в новый файл


with open(file1_dir, 'r') as file:
    print('Содержимое файла {0}:'.format(file_name))
    print(file.read())

with open(file2_dir, 'r') as file:
    print('Содержимое файла {0}:'.format(file_name2))
    print(file.read())