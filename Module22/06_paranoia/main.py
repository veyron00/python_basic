import os

def data_encryption(data_list: list) -> list:
    '''Функция шифрует полученные данные по методу Цезаря,
    и возвращает список с зашифрованными данными'''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                ]
    encryption_list = list()
    count = 0
    for i_line in data_list:
        word = ''
        count += 1
        for letter in i_line:
            if letter in alphabet:
                if alphabet.index(letter) + count <= len(alphabet):
                    word += alphabet[alphabet.index(letter) + count]
                else:
                    word += alphabet[(alphabet.index(letter) + count) - len(alphabet)]
        encryption_list.append(word)
    return encryption_list



def dir_search(new_file: str, file_name: str, dirs: str, new_folder = None) -> str:
    '''Функция поиска директории, где находится файл text.txt, возвращает
    эту же директорию для создания нового файла.'''
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
        print('Директории не существует.')




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


unencrypted_file = 'text.txt'
disk = 'D:\SKILLBOX'
file_dir = find_file(disk, unencrypted_file)
unencrypted_file_list = list()


with open(file_dir, 'r') as file:
    for i_elem in file:
        for x_elem in i_elem.split('\n'):
            if x_elem != '':
                unencrypted_file_list.append(x_elem)


encrypted_data = data_encryption(unencrypted_file_list)

encrypted_file_name = 'cipher_text.txt' # Название нового файла который нужно создать

new_file_dir = dir_search(encrypted_file_name, unencrypted_file, disk) \
               + os.path.sep + encrypted_file_name  # Директория для создания нового файла

# Создаем файл cipher_text.txt'и вносим в него зашифрованные данные.
for string in encrypted_data:
    with open(new_file_dir, 'a') as file:
        string += '\n'
        file.write(string)

with open(file_dir, 'r') as file:
    print('Содержимое файла {0}:'.format(unencrypted_file))
    print(file.read())

with open(new_file_dir, 'r') as file2:
    print('Содержимое файла {0}:'.format(encrypted_file_name))
    print(file2.read())