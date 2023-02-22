def check_coordinate(x, y, r):
    return (x * x + y * y) ** 0.5 < r

print('Введите координаты монетки:')
coordinate_x = float(input('X: '))
coordinate_y = float(input('Y: '))
radius = int(input('Введите радиус: '))

if check_coordinate(coordinate_x, coordinate_y, radius):
    print('\nМонетка где-то рядом.')
else:
    print('\nМонетки в области нет.')