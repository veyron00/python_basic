def print_from_end(seq: list):
    '''Функция печати с конца.
    Принимает список, и выводит содержимое списка на экран начиная с конца'''
    for line in seq[::-1]:
        print(line)

with open('zen.txt', 'r')as text_file:
    text_list = list()
    for string in text_file:
        string = string.split('\n')
        for elem in string:
            if elem != "":
                text_list += [elem]

print_from_end(text_list)
