print('Задача 3. Функция')

# Учитель математики придумывает каждому своему ученику отдельные функции,
# которые нужно отобразить на графике и посчитать.
# А ещё этот учитель разбирается в программировании.
# Поэтому, чтобы не считать вручную все эти функции,
# он написал программу, которая делает всю работу за него.

# Напишите программу,
# которая получает от пользователя число X и вычисляет значение функции Y

# Напомним, как это работает:
# Если X больше нуля Y = X - 12.
# Если X равных нулю Y равен пяти.
# Если X меньше нуля Y равен квадрату X.

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: -6
# Игрек равен 36

value_x = int(input('Введите значение Х: '))
if value_x > 0:
  y = value_x - 12
  print('Y =', y)
elif value_x == 0:
  y = 5
  print('Y =', y)
elif value_x < 0:
  y = value_x**2
  print('Y =', y)