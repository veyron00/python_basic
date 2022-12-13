import string

extensions = ('.txt', '.docx')
file_name = input('Название файла: ').lower()
err = 0
correct_ext = False

if file_name[0] in string.punctuation:
    print('Ошибка: название начинается на один из специальных символов')
    err += 1

if err == 0:
    if file_name.endswith(extensions):
        correct_ext = True

    if correct_ext:
        print('Файл назван верно.')
    else:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')