import os

def create_file(text: str, directory: list):
    ''' Функция создает новый файл, или если файл с таким названием уже
    существует, то перезаписывает его.'''
    directory = os.path.abspath(os.path.join('/', os.path.sep.join(directory)))
    if os.path.exists(directory):
        file_name = input('Введите имя файла: ')
        file_extension = '.txt'
        file_directory = directory + os.path.sep + file_name + file_extension
        if not os.path.exists(file_directory):
            with open(file_directory, 'w') as new_file:
                new_file.write(text)
                print('Файл успешно сохранён!')
        elif os.path.exists(file_directory):
            question = input('Вы действительно хотите перезаписать файл? ').lower()
            if question == 'да':
                with open(file_directory, 'w') as new_file:
                    new_file.write(text)
                print('Файл успешно перезаписан!')

            else:
                pass

    else:
        print('Введена несуществующая директория.')

text = input('Введите строку: ')
directory = input('Куда хотите сохранить документ? '
                  '\nВведите последовательность папок (через пробел): ').split(' ')
create_file(text, directory)

