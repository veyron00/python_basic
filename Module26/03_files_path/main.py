import os


def gen_files_path(path):
    """
    Генерирует пути ко всем встреченным файлам в каталоге.
    :param path: Путь к каталогу в котором необходимо произвести поиск файлов.
    :return: None
    """
    for i in os.walk(path):
        if len(i[2]) > 0:
            for x in i[2]:
                yield '{0}{1}{2} '.format(i[0], '\\', x)


file_path = 'D:\\SKILLBOX\\Python_Basic'

for i_dir in gen_files_path(file_path):
    print(i_dir)
