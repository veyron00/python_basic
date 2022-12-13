def coin_search(x, y, r):
    if x <= r or y <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки: ')
x_coordinate = float(input('X: '))
y_coordinate = float(input('Y: '))
radius = int(input('Введите радиус: '))
coin_search(x_coordinate, y_coordinate, radius)