print('Задача 7. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math
while True:
    print('Введите местоположение коня: ')
    x_figure = math.floor(float(input('По горизонтали X коня: ')))
    y_figure = math.floor(float(input('По вертикали Y коня: ')))
    print('Введите местоположение точки на доске: ')
    x_board = math.floor(float(input('По горизонтали X доски: ')))
    y_board = math.floor(float(input('По вертикали Y доски: ')))
    if x_board > 8 or y_board > 8 and x_board < 0 or y_board < 0:
        print('Нет, конь не может ходить в эту точку.')
    elif x_board == x_figure + 2 or x_board == x_figure - 2 and y_board == y_figure + 1 or y_board == y_figure - 1:
        print(
            f'Конь в клетке({x_figure},{y_figure}). Точка в клетке ({x_board},{y_board}).'
        )
        print('Да, конь может ходить в эту точку.')
    else:
        print('Нет, конь не может ходить в эту точку.')