text =  input('Доступное меню: ').replace('; ', ';').split(';')

print('На данный момент в меню есть:', ', '.join(text))