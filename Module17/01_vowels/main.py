text = input('Введите текст: ')
text_list = [i for i in text]
vowel_letters = ['а', "е", "ё", "и", "о", 'у', 'ю', 'я', 'э', 'ы']
vowels_from_text = [vowel for vowel in text_list if vowel in vowel_letters]

print(f'Список гласных букв: {vowels_from_text}')
print(f'Длина списка: {len(vowels_from_text)}')
