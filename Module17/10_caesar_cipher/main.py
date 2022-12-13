def encryption(text, num):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' '
    ]
    i_text = [i_letter for letter in text
              for i_letter in range(len(alphabet))
              if letter == alphabet[i_letter]
    ]

    encrypted_message = ''
    for i in i_text:
        if i < 30:
            encrypted_message += alphabet[i + num]
        elif alphabet[i] == ' ':
            encrypted_message += alphabet[i]
        elif i >= 30:
            encrypted_message += alphabet[i - 30]
    print(encrypted_message)
message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
encryption(message, shift)
