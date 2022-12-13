def output_to_screen(seq):
    count_let = 0
    count_words = 0
    letter_dict = dict()
    letter_list = []
    for i_str in seq:
        for i_word in i_str.lower().split(' '):
            count_words += 1
        for i_letter in i_str.lower():
            if not i_letter.isalpha():
                continue
            else:
                count_let += 1
                letter_list += [i_letter]

    for letter in letter_list:
        letter_dict[letter] = letter_list.count(letter)

    print('Количество букв в файле: {0}'.format(count_let))
    print('Количество слов в файле: {0}'.format(count_words))
    print('Количество строк в файле: {0}'.format(len(seq)))
    print('Наиболее редкая буква: {0} количество - {1}'.format(min(letter_dict.items(), key= lambda letter: letter[1])[0],
                                                                                                min(letter_dict.items(), key= lambda letter: letter[1])[1]))



with open('D:\SKILLBOX\Python_Basic\Module22\\02_zen_of_python\zen.txt', 'r') as text_file:
    text_list = list()
    for string in text_file:
        for elem in string.split('\n'):
            if elem != "":
                text_list += [elem]

output_to_screen(text_list)

