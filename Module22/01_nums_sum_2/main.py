import os

with open('numbers.txt', 'r', encoding='utf-8') as file_num:
    count = []
    for i_elem in file_num:
        for i_num in i_elem:
            if i_num.isdigit():
                count += [int(i_num)]
with open('answer.txt', 'w') as new_file:
    new_file.write(str(sum(count)))

with open('numbers.txt', 'r', encoding='utf-8') as file_num:
    print('Содержимое файла numbers.txt')
    print(file_num.read())

with open('answer.txt', 'r') as new_file:
    print('Содержимое файла answer.txt')
    print(new_file.read())