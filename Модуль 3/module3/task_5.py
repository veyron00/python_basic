print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.

minutes = int(input('Введите количество минут: '))
hours = minutes // 60
remaining_minutes = minutes % 60
print('Количество целых часов -', hours)
print('Остаток минут -', remaining_minutes)