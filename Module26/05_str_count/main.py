import os


def find_python_file(path: str):
    """
    Генерирует пути к файлам с расширением .py.
    :param path: Каталог в котором производится поиск файлов .py.
    :return: str
    """
    for i_file in os.walk(path):
        if len(i_file[2]) > 0:
            for x in i_file[2]:
                if x.endswith('.py'):
                    yield '{0}{1}{2} '.format(i_file[0], '\\', x)


def read_lines_code(path: str):
    """
    Считает количество строчек кода в файле, игнорируя комментарии в '''.
    :param path: Директория с файлом.
    :return: line_count: Количество строк кода в файле.
    """
    line_count = 0
    counting = False
    with open(path, 'r', encoding='utf-8') as file:
        for i_line in file:
            if i_line.startswith('\n'):
                continue
            elif i_line.startswith('#'):
                continue
            elif i_line.startswith('    """'):
                if counting:
                    counting = False
                    continue
                else:
                    counting = True
            if counting:
                continue
            else:
                line_count += 1
    return line_count


file_path = 'D:\\SKILLBOX\\Python_Basic\\Module25'
files = find_python_file(file_path)
files_lines_count = []
count_files = 0
for i in files:
    files_lines_count.append(read_lines_code(i))
    count_files += 1
print('Сумма строчек кода в {0} файле/файлах: {1}.'.format(count_files,
                                                           sum(files_lines_count)))
