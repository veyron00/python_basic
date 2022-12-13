print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
calc3 = 0
calc4 = 0
calc5 = 0

for assessment in 4,5,3,4,5,4,3,5,5,3,3,3,4,4,4,4,4,5,5,5,3,3,3,5,4:
  if assessment == 3:
    calc3 += 1
  elif assessment == 4:
    calc4 += 1
  elif assessment == 5:
    calc5 += 1
print(calc3)
print(calc4)
print(calc5)

if calc3 > calc4 and calc3 > calc5:
  print('Сегодня больше троечников')
elif calc4 > calc3 and calc4 > calc5:
  print('Сегодня больше хорошистов')
elif calc5 > calc3 and calc5 > calc4:
  print('Сегодня больше отличников')
elif calc3 == calc4 and calc3 > calc5:
  print('Сегодня троечников и хорошистов одинаково')
elif calc4 == calc5 and calc4 > calc3:
  print('Сегодня хорошистов и отличников одинаково')
elif calc3 == calc5 and calc3 > calc4:
  print('Сегодня троечников и отличников одинаково')
elif calc3 == calc4 and calc4 == calc5:
  print('Сегодня всех одинаково') 