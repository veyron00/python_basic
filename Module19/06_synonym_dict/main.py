def checking_synonyms(synonyms):
    text = input('Введите слово: ').lower()

    for word in synonyms.keys():
        if text == word:
            print('Синоним: {0}'.format(synonyms[word].title()))
            break
        elif text == synonyms[word]:
            print('Синоним: {0}'.format(word.title()))
            break
    else:
        print('Такого слова в словаре нет.')
        checking_synonyms(synonyms)





words_quantity = int(input('Введите количество пар слов: '))
synonyms_dict = dict()
for i in range(words_quantity):
    couple = input('{0}-я пара: '.format(i+1)).lower().split(' - ')
    synonyms_dict[couple[0]] = couple[1]

checking_synonyms(synonyms_dict)

# Привет - Здравствуйте
# Печально - Грустно
# Весело - Радостно