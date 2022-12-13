print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(phrase, number, letter):
  count_num = 0
  count_letter = 0
  for num in phrase:
    if num == number:
      count_num += 1
  for lett in phrase:
    if lett == letter:
      count_letter += 1
  print('Количество цифр', number,':', count_num)
  print('Количество букв', letter,':', count_letter)
  


phrase = input('Введите текст: ')
number = input('Какую цифру ищем? ')
letter = input('Какую букву ищём? ')

count_letters(phrase, number, letter)
  