def invert(dictionary):
    inverted_dict = dict()
    for i_values in dictionary.values():
        inverted_dict[i_values] = []
    for i in inverted_dict.keys():
        for key in sorted(dictionary.keys()):
            if i == dictionary[key]:
                inverted_dict[i] += key
    return inverted_dict


text = input('Введите текст: ')
text_list = list(text)
text_dict = dict()


for letter in text:
    text_dict[letter] = text.count(letter)

print('Оригинальный словарь частот: ')
for key in sorted(text_dict.keys()):
    print('{0} : {1}'.format(key, text_dict[key]))


new_dict = invert(text_dict)

print('Инвертированный словарь частот: ')
for i in sorted(new_dict.keys()):
    print('{0} : {1}'.format(i, new_dict[i]))
