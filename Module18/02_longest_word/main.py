text = input('Введите строку: ').split()
max_len = 0
max_word = ''

for word in text:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print('Самое длинное слово:', max_word)
print('Длина этого слова:', max_len)