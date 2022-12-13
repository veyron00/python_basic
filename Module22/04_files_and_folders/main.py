import os

def get_files_size_and_folders(directory):
    nested_file = list()
    nested_folders = list()
    files_size = 0
    for i_elem in os.listdir(directory):
        if os.path.isfile(os.path.abspath(directory + os.path.sep + i_elem)):
            files_size += os.path.getsize(os.path.abspath(directory + os.path.sep + i_elem))
            nested_file.append(i_elem)
        elif os.path.isdir(os.path.abspath(directory + os.path.sep + i_elem)):
            nested_folders.append(i_elem)

    print('Директория: {0}'.format(directory))
    print('Размер каталога (в Кб): {0}'.format(round(files_size / 1024, 2)))
    print('Количество подкаталогов: {0}'.format(len(nested_folders)))
    print('Количество файлов: {0}'.format(len(nested_file)))


directory = 'D:\\'

get_files_size_and_folders(directory)