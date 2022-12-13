import os
from zipfile import ZipFile

def unpacking_files(dirs: str):
    '''Функция распаковки zip файлов

    Принимает директорию с zip файлом в виде строки и распаковывает файлы из zip файла'''
    with ZipFile(dirs, 'r') as file:
        ZipFile.extractall(file)


def dir_search(new_file: str, file_name, dirs: str, new_folder = None) -> str:
    '''Функция поиска директории,

    где находится запрашиваемый файл возвращает эту же директорию
    с искомым файлом.'''
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



zip_file_name = 'voyna-i-mir.zip'
search_directory = 'D:\SKILLBOX'
dir_with_zipfile = dir_search(zip_file_name, zip_file_name, search_directory) + '\\' + zip_file_name
unpacking_files(dir_with_zipfile) # Распаковка файла из архива


text_file_name = 'voyna-i-mir.txt'
dir_with_textfile = dir_search(zip_file_name, zip_file_name, search_directory) + '\\' + text_file_name


text_list = list() # Сохраняем данные из файла в список.
with open(dir_with_textfile, 'r', encoding='utf-8') as file:
    text_list += [file.read()]


text_dict_eng = dict() # Словарь с количественными данными по английским буквам
text_dict_ru = dict() # Словарь с количественными данными по русским буквам
letters_count_eng = '' # Строка для подсчета английских букв без пробелов
letters_count_ru = '' # Строка для подсчета русских букв без пробелов
for letter in text_list[0]:
    if letter in text_dict_eng or letter in text_dict_ru: # Если такая буква есть в словарях то, пропускаем ее
        continue
    else:
        if letter.isalpha():
            if letter.isascii(): # Если английская буква то в английский словарь
                text_dict_eng[letter] = text_list[0].count(letter)
            else: # Если не английская буква то, в русский словарь
                text_dict_ru[letter] = text_list[0].count(letter)
    if letter.isalpha():
        if letter.isascii():
            letters_count_eng += letter
        else:
            letters_count_ru += letter


frequency_of_letters_eng = dict() # Словарь с частотностью английских букв в процентах
for key, value in sorted(text_dict_eng.items()):
    frequency_of_letters_eng[key] = round(value / (len(letters_count_eng) / 100) / 100, 3)



frequency_of_letters_ru = dict() # Словарь с частотностью русских букв в процентах
for key, value in sorted(text_dict_ru.items()):
    frequency_of_letters_ru[key] = round(value / (len(letters_count_ru) / 100) / 100, 3)

print('Частотность букв английского словаря.')
print('Буква - частотность')
for key, value in frequency_of_letters_eng.items():
    print('{0} - {1}'.format(key, value))



print('Частотность букв русского словаря.')
print('Буква - частотность')
for key, value in frequency_of_letters_ru.items():
    print('{0} - {1}'.format(key, value))

