def checking_for_polydrome(word):
    word_1 = []
    if word == word[::-1]:
        return 'Можно сделать палиндромом'
    else:
        for i_letter in range(len(word)):
            word_1 = word[1:] + word[:1]
            if word_1 == word_1[::-1]:
                return 'Можно сделать палиндромом'
            else:
                word = word_1
                continue
        return  'Нельзя сделать палиндромом'
text = list(input('Введите строку: '))

check = checking_for_polydrome(text)
print(check)

