print('Задача 10. Метод бутерброда')

# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |

encrypted_word = 'shacnidw'
first_part_cipher = ''
intermediate_part_cipher = ''
second_part_cipher = ''
count = 0

for symbol in encrypted_word:
  count += 1
  if count % 2 != 0:
    first_part_cipher += symbol
  elif count % 2 == 0:
    intermediate_part_cipher += symbol
for symbol in intermediate_part_cipher[::-1]:
  second_part_cipher += symbol
  
print('Зашифрованное слово это -',first_part_cipher + second_part_cipher)
