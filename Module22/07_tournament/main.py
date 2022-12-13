import os


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


first_tour_file = 'first_tour.txt'
search_directory = 'D:\SKILLBOX'
first_file_dir = find_file(search_directory, first_tour_file)
second_tour_file = 'second_tour.txt'
second_file_dir = dir_search(second_tour_file, first_tour_file, search_directory) + '\\' + second_tour_file


first_tour_list = list()
with open(first_file_dir, 'r') as file:
    for i_elem in file:
        for x_elem in i_elem.split('\n'):
            if x_elem != '':
                first_tour_list.append(x_elem) # ['80', 'Ivanov Serg 80', 'Sergeev Petr 92', 'Petrov Vasiliy 98', 'Vasiliev Maxim 78']

passing_score = int(first_tour_list.pop(0))
first_tour_list2 = list()
for i_player in first_tour_list:
    player = i_player.split(' ')
    first_tour_list2.append(player)  # [['Ivanov', 'Serg', '80'], ['Sergeev', 'Petr', '92'], ['Petrov', 'Vasiliy', '98'], ['Vasiliev', 'Maxim', '78']]



second_tour_list = list()
for index, i_list in enumerate(first_tour_list2):
    if int(i_list[2]) > passing_score:
        second_tour_list.append(i_list)   # [['Sergeev', 'Petr', '92'], ['Petrov', 'Vasiliy', '98']]

count = 1
for i_elem in sorted(second_tour_list, key=lambda lst: lst[2], reverse=True):
    line_to_write = str(count) + ')' + ' ' + i_elem[1][:1] + '.' + ' ' + i_elem[0] + ' ' + i_elem[2] + '\n'
    count += 1
    with open(second_file_dir, 'a') as file:
        file.write(line_to_write)


with open(first_file_dir, 'r') as file:
    print('Содержимое файла {0}:'.format(first_tour_file))
    print(file.read())


with open(second_file_dir, 'r') as file:
    print('Содержимое файла {0}:'.format(second_tour_file))
    print(file.read())
